#!/usr/bin/python

import time, sys, os, subprocess
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf

PID_DIR = "/home/arsnova"

# Enforce "Singleton"
pid = str(os.getpid())
pidfile = "/tmp/ars-gui.pid"

if os.path.isfile(pidfile):
    print "%s already exists, exiting" % pidfile
    sys.exit()
file(pidfile, 'w').write(pid)

class ARSWindow(Gtk.Window):

    def __init__(self, click_service, cards_service, voting_service):
        Gtk.Window.__init__(self, title="ARSnova Router")
	
	self.click_service = click_service

	self.set_resizable(False)
	self.set_default_icon_from_file(sys.argv[2])
	self.rowbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)	
	self.add(self.rowbox)

	self.rowbox.pack_start(ARSServiceWidget(self, "arsnova.click", click_service).get_box(), True, True, 0)
	self.rowbox.pack_start(ARSServiceWidget(self, "arsnova.cards", cards_service, update_enabled=False).get_box(), True, True, 0)
	self.rowbox.pack_start(ARSServiceWidget(self, "arsnova.voting", voting_service, update_enabled=False).get_box(), True, True, 0)

	self.votingLabel = Gtk.Label(label="arsnova.voting")

class ARSServiceWidget(object):

    def __init__(self, parent, name, service, update_enabled=True):
	self.parent = parent
	self.name = name
	self.service = service

	self.box = Gtk.Box(spacing=6)

	self.label = Gtk.Label(label=self.name)
	self.box.pack_start(self.label, True, True, 0)
	self.status_label = Gtk.Label(label=self.get_status_string())
	self.box.pack_start(self.status_label, True, True, 0)

        self.start = Gtk.Button(label="Start")
	self.stop = Gtk.Button(label="Stop")
	self.check_update = Gtk.Button(label="Check for Update")
	self.start.connect("clicked", self.on_start_clicked)
        self.stop.connect("clicked", self.on_stop_clicked)
	self.check_update.connect("clicked", self.on_check_update_clicked)
	self.check_update.set_sensitive(update_enabled)
	self.box.pack_start(self.start, True, True, 0)
        self.box.pack_start(self.stop, True, True, 0)
	self.box.pack_start(self.check_update, True, True, 0)

    def get_box(self):
	return self.box

    def on_start_clicked(self, widget):
        self.service.start()
	
	if not self.service.is_running():
		self.error_status()
	else:
		self.refresh_status()

    def on_stop_clicked(self, widget):
        if self.service.stop():
		self.refresh_status()
	else:
		self.error_status()

    def on_check_update_clicked(self, widget):
	# This is actually not drawn because we do updating on the main thread,
	# blocking the UI update. ;-)
	self.update_status()

	md = 1
	result = self.service.update()
	if result.is_okay():
		md = Gtk.MessageDialog(self.parent, Gtk.DialogFlags.MODAL, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, result.get_message())
	else:
		md = Gtk.MessageDialog(self.parent, Gtk.DialogFlags.MODAL, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, result.get_message())
	md.run()
	md.destroy()
	self.refresh_status()

    def refresh_status(self):
	self.status_label.set_label(self.get_status_string())

    def get_status_string(self):
	if self.service.is_running():
		return "RUNNING"
	return "STOPPED"

    def error_status(self):
	self.status_label.set_label("ERROR")

    def update_status(self):
	self.status_label.set_label("UPDATING")

class ARSService(object):

    def __init__(self, name, pid_dir):
	self.name = name
	self.pid_dir = pid_dir

    def is_running(self):
	return os.path.isfile(self.pid_dir + "/" + self.name + ".pid")

    def start(self):
	if self.is_running():
		return True
	res = subprocess.call(["systemctl", "start", "arsnova-"+self.name+".service"])
	if res == 0:
		return True
	return False

    def stop(self):
	if not self.is_running():
		return True
	res = subprocess.call(["systemctl", "stop", "arsnova-"+self.name+".service"])
	if res == 0:
		return True
	return False

    def update(self):
	# TODO: Some threading would be useful...
	cur_path = os.path.dirname(__file__)
	res = subprocess.call(["sh", "download_"+self.name+".sh"], cwd=os.path.realpath(cur_path+"/../pipeline"))
	return ARSUpdateResult(res)

class ARSUpdateResult(object):

    def __init__(self, result):
	self.result = result

    def is_okay(self):
	if self.result == 0:
		return True
	if self.result == 42:
		return True
	return False

    def get_message(self):
	if self.result == 0:
		return "Update successful"
	if self.result == 42:
		return "Already up to date"
	# Errors
	return "Error while updating"

try:
	window = ARSWindow(ARSService("click", PID_DIR), ARSService("cards", PID_DIR), ARSService("voting", PID_DIR))
	window.show_all()
	window.connect("destroy", Gtk.main_quit)
	Gtk.main()
finally:
	# This might not work in case of crashes :/
    	os.unlink(pidfile)

