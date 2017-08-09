import time
import sys
import thread

def opspersec(sec=1):
    endtime=time.time()+sec
    i=0
    while time.time()<endtime:
        i+=1
    return i/sec

def multiopspersec(threads=2,sec=1):
    i=thread.start_new_thread(opspersec,(sec,))
    print threading.enumerate()
    return i

def __main__():
    if len(sys.argv)>1:
        for n in range(1,len(sys.argv)):
            print sys.argv[n],": ", str(opspersec(int(sys.argv[n])))
    else:
        n=10
        print n,": ", str(opspersec(n))

print str(multiopspersec(2,10))
