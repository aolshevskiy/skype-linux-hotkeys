#!/usr/bin/python2
import dbus
bus = dbus.SessionBus()
skype = bus.get_object('com.Skype.API', '/com/Skype')
skype.Invoke('NAME linux-hotkeys')
skype.Invoke('PROTOCOL 5')
import sys
args = sys.argv[1:]
command = args[0]
if command == '-m':
    command = "MUTE ON"
    if skype.Invoke('GET MUTE') == "MUTE ON":
        command = "MUTE OFF"
    skype.Invoke(command)
elif command == '-c':
    import ConfigParser
    config = ConfigParser.ConfigParser()
    from os.path import join, expanduser
    config.read(join(expanduser('~'), 'bin', 'skype-hotkeys.cfg'))
    (number, code) = config.get('skype-hotkeys', ' '.join(args[1:])).split()
    res = skype.Invoke('CALL ' + number).split()
    call_id = res[1]
    import time
    status = res[3]
    while status != 'INPROGRESS':
        time.sleep(1)
        res = skype.Invoke('GET CALL ' + call_id + ' STATUS').split()
        status = res[3]
    time.sleep(1)
    for c in code:
        time.sleep(0.4)
        skype.Invoke('SET CALL ' + call_id + ' DTMF ' + c)
