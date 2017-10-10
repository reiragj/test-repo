import receiverhandler
import os
import sys

receiver = receiverhandler.controller()

if len(sys.argv) == 1:
    print "(function, filename) Insert arguments!!"
    exit(1)
elif sys.argv[1] == "-s":
    '''Run receiver'''
    if sys.argv[2] is None:
        "Please insert filename. ex) PacketReceiver.py -s <filename>"    
    else:
        print receiver.run_process(sys.argv[2])
    
elif sys.argv[1] == "-k":
    '''Stop receiver'''
    if sys.argv[2] is None:
        "Please insert name of receiver. ex) PacketReceiver.py -t <receiver name>"
    receiver.kill_process(sys.argv[2])
    
elif sys.argv[1] == "-ta":
    '''Stop all receiver'''

elif sys.argv[1] == "-re":
    '''Refresh receiver'''

elif sys.argv[1] == "--help":
    print("No help kkkk!!")

elif sys.argv[1] == "-l":
    _plist = receiver.get_list()
    for k,v in _plist.items():
        print "Filename : %s || ProcessId : %s" % (k,v)

