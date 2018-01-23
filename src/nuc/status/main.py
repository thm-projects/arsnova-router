import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

PID_DIR = "/home/arsnova"

class ARSWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ARSnova Router")

	self.rowbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)	
	self.add(self.rowbox)

	self.add_click_row()
	self.add_cards_row()

	self.votingLabel = Gtk.Label(label="arsnova.voting")

    def add_click_row(self):
	self.clickBox = Gtk.Box(spacing=6)
	self.rowbox.pack_start(self.clickBox, True, True, 0)

	self.clickLabel = Gtk.Label(label="arsnova.click")
	self.clickBox.pack_start(self.clickLabel, True, True, 0)
	self.clickStatusLabel = Gtk.Label(label=self.get_status_string("click"))
	self.clickBox.pack_start(self.clickStatusLabel, True, True, 0)

        self.clickStart = Gtk.Button(label="Start")
	self.clickStop = Gtk.Button(label="Stop")
	self.clickCheckUpdate = Gtk.Button(label="Check for Update")
	self.clickStart.connect("clicked", self.on_click_start_clicked)
        self.clickStop.connect("clicked", self.on_click_stop_clicked)
	self.clickBox.pack_start(self.clickStart, True, True, 0)
        self.clickBox.pack_start(self.clickStop, True, True, 0)
	self.clickBox.pack_start(self.clickCheckUpdate, True, True, 0)

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
	self.clickBox.pack_start(self.cardsCheckUpdate, True, True, 0)

    def on_click_start_clicked(self, widget):
        print("Start arsnova.click")

    def on_click_stop_clicked(self, widget):
        print("Stop arsnova.click")

    def on_cards_start_clicked(self, widget):
        print("Start arsnova.cards")

    def on_cards_stop_clicked(self, widget):
        print("Stop arsnova.cards")

    def get_status_string(self, serviceName):
	if self.is_running(serviceName):
		return "RUNNING"
	return "STOPPED"

    def is_running(self, serviceName):
	return os.path.isfile(PID_DIR + "/" + serviceName + ".pid")

window = ARSWindow()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
