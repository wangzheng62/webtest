import time,threading
def looptimer(func,n=1,steptime=0):
    if n==0:
        t = threading.Timer(steptime,looptimer,args=(func,0,steptime))
        t.start()
        func()
    elif n==1:
        func()
    else:
        t = t = threading.Timer(steptime,looptimer,args=(func,n-1,steptime))
        t.start()
        func()
def alarmclock(starttime,func,n=1,steptime=0):
    now=time.time()
    start=starttime-now
    t=threading.Timer(start,looptimer,args=(func,n,steptime))
    t.start()
if __name__=='__main__':
    def printnote():
        print("闹钟响了,%s" % (time.time()))
    now=time.time()
    alarmclock(now+10,printnote,0,2)
    print(now)