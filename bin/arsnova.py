#!/usr/bin/python -p

# import the library
from appJar import gui
import subprocess

label_created = 0

# top slice - CREATE the GUI
def press(btn):
  global label_created

  if label_created==0:
    app.addLabel("l1", "ARSnova.click Stopped")
    app.addLabel("l2", "ARSnova.vote Stopped")
    app.setLabelBg("l1", "red")
    app.setLabelBg("l2", "red")
    label_created=1

  if btn=="Cancel":
    subprocess.run("sudo systemctl stop arsnova-click.service",
        shell=True,
        check=True)
    app.stop()
  elif btn=="ARSnova.click Start":
    app.setLabel("l1", "ARSnova.click started")
    app.setLabelBg("l1", "green")
    subprocess.run("sudo systemctl start arsnova-click.service",
        shell=True,
        check=True)
  elif btn=="ARSnova.click Stop":
    app.setLabel("l1", "ARSnova.click stoped")
    app.setLabelBg("l1", "red")
    subprocess.run("sudo systemctl stop arsnova-click.service",
        shell=True,
        check=True)
  elif btn=="ARSnova.vote Start":
    app.setLabel("l2", "ARSnova.vote stoped")
    app.setLabelBg("l2", "green")
#    subprocess.run("sudo systemctl stop arsnova-vote.service",
#        shell=True,
#        check=True)
  elif btn=="ARSnova.vote Stop":
    app.setLabel("l2", "ARSnova.vote stoped")
    app.setLabelBg("l2", "red")
#    subprocess.run("sudo systemctl stop arsnova-vote.service",
#        shell=True,
#        check=True)
  else:
    print("What happened here!!!")

app = gui()

### create Buttons ###
app.addButtons(["ARSnova.click Start", "ARSnova.click Stop"], press)
app.addButtons(["ARSnova.vote Start", "ARSnova.vote Stop"], press)
app.addButton("Cancel", press);

# bottom slice - START the GUI
app.go()
