#!/usr/bin/python2
import dbus
bus = dbus.SessionBus()
skype = bus.get_object('com.Skype.API', '/com/Skype')
skype.Invoke('NAME linux-hotkeys')
skype.Invoke('PROTOCOL 5')
import sys
command = " ".join(sys.argv[1:])
if(command == '-m'):
    command = "MUTE ON"
    if skype.Invoke('GET MUTE') == "MUTE ON":
        command = "MUTE OFF"
    skype.Invoke(command)
