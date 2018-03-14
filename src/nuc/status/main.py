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

    def __init__(self, click_service):
        Gtk.Window.__init__(self, title="ARSnova Router")
	
	self.click_service = click_service

	self.set_resizable(False)
	self.set_default_icon_from_file(sys.argv[2])
	self.rowbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)	
	self.add(self.rowbox)

	self.add_click_row()
	#self.add_cards_row()

	self.votingLabel = Gtk.Label(label="arsnova.voting")

    def add_click_row(self):
	self.clickBox = Gtk.Box(spacing=6)
	self.rowbox.pack_start(self.clickBox, True, True, 5)

	self.clickLabel = Gtk.Label(label="arsnova.click")
	self.clickBox.pack_start(self.clickLabel, True, True, 0)
	self.clickStatusLabel = Gtk.Label(label=self.get_status_string("click"))
	self.clickBox.pack_start(self.clickStatusLabel, True, True, 0)

        self.clickStart = Gtk.Button(label="Start")
	self.clickStop = Gtk.Button(label="Stop")
	self.clickCheckUpdate = Gtk.Button(label="Check for Update")
	self.clickStart.connect("clicked", self.on_click_start_clicked)
        self.clickStop.connect("clicked", self.on_click_stop_clicked)
	self.clickCheckUpdate.connect("clicked", self.on_click_check_update_clicked)
	self.clickBox.pack_start(self.clickStart, True, True, 0)
        self.clickBox.pack_start(self.clickStop, True, True, 0)
	self.clickBox.pack_start(self.clickCheckUpdate, True, True, 0)

    # TODO: Will get refactored into its own "Widget"
    def add_cards_row(self):
	self.cardsBox = Gtk.Box(spacing=6)
	self.rowbox.pack_start(self.cardsBox, True, True, 0)

	self.cardsLabel = Gtk.Label(label="arsnova.cards")
	self.cardsBox.pack_start(self.cardsLabel, True, True, 0)
	self.cardsStatusLabel = Gtk.Label(label=self.get_status_string("cards"))
	self.cardsBox.pack_start(self.cardsStatusLabel, True, True, 0)

        self.cardsStart = Gtk.Button(label="Start")
	self.cardsStop = Gtk.Button(label="Stop")
	self.cardsCheckUpdate = Gtk.Button(label="Check for Update")
	self.cardsStart.connect("clicked", self.on_cards_start_clicked)
        self.cardsStop.connect("clicked", self.on_cards_stop_clicked)
	self.cardsBox.pack_start(self.cardsStart, True, True, 0)
        self.cardsBox.pack_start(self.cardsStop, True, True, 0)
	self.cardsBox.pack_start(self.cardsCheckUpdate, True, True, 0)

    def on_click_start_clicked(self, widget):
        self.click_service.start()
	
	if not self.click_service.is_running():
		self.error_status()
	else:
		self.refresh_status()

    def on_click_stop_clicked(self, widget):
        if self.click_service.stop():
		self.refresh_status()
	else:
		self.error_status()

    def on_click_check_update_clicked(self, widget):
	# This is actually not drawn because we do updating on the main thread,
	# blocking the UI update. ;-)
	self.update_status()

	result = self.click_service.update()
	if result.is_okay():
		md = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, result.get_message())
		md.run()
		md.destroy()
		self.refresh_status()
	else:
		md = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK, result.get_message())
		md.run()
		md.destroy()
		self.error_status()

    def on_cards_start_clicked(self, widget):
        print("Start arsnova.cards")

    def on_cards_stop_clicked(self, widget):
        print("Stop arsnova.cards")

    def refresh_status(self):
	self.clickStatusLabel.set_label(self.get_status_string("click"))

    def get_status_string(self, serviceName):
	if self.click_service.is_running():
		return "RUNNING"
	return "STOPPED"

    def error_status(self):
	self.clickStatusLabel.set_label("ERROR")

    def update_status(self):
	self.clickStatusLabel.set_label("UPDATING")

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
    	window = ARSWindow(ARSService("click", PID_DIR))
	window.show_all()
	window.connect("destroy", Gtk.main_quit)
	Gtk.main()
finally:
	# This might not work in case of crashes :/
    	os.unlink(pidfile)

