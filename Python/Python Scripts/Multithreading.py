# """ THREAD """ #
import time
import thread

def pri(id):
	print 'hai',id
	time.sleep(5)
	print 'hello',id
	time.sleep(5)
	print 'bye',id

try:	
	thread.start_new_thread(pri,('rama',))	
	thread.start_new_thread(pri,('bheema',))	
except Exception as e:
	print "some error",e
while 1:
	pass


# """ THREADING """ #
import time
import threading

class Mythread(threading.Thread):
	def __init__(self,thread_name,id):
		threading.Thread.__init__(self)
		self.thread_name=thread_name
		self.id=id
	def run(self):
		print "starting : "+self.thread_name+'\n'
		pri(self.id)
		print "ending : "+self.thread_name+'\n'

def pri(id):
	print 'hai'+id+'\n'
	time.sleep(5)
	print 'hello'+id+'\n'
	time.sleep(5)
	print 'bye'+id+'\n'

thread1=Mythread('rama','USA')
thread2=Mythread('bheema','CAD')

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print "main thread exection completed"


# """ THREADING LOCK """ #
import time
import threading

class Mythread(threading.Thread):
	def __init__(self,thread_name,id):
		threading.Thread.__init__(self)
		self.thread_name=thread_name
		self.id=id
	def run(self):
		print "starting : "+self.thread_name+'\n'
		thraedLock.acquire()
		pri(self.id)
		thraedLock.release()
		print "ending : "+self.thread_name+'\n'

def pri(id):
	print 'hai'+id+'\n'
	time.sleep(5)
	print 'hello'+id+'\n'
	time.sleep(5)
	print 'bye'+id+'\n'

thraedLock=threading.Lock()
thread1=Mythread('rama','USA')
thread2=Mythread('bheema','CAD')

thread2.start()
thread1.start()

thread1.join()
thread2.join()

print "main thread exection completed"


# """ THREADQUEUE """ #
import time
import Queue
import threading

exitflag=0
class Mythread(threading.Thread):
	def __init__(self,thread_name,id,q):
		threading.Thread.__init__(self)
		self.thread_name=thread_name
		self.id=id
		self.q=q
	def run(self):
		print "starting : "+self.thread_name+'\n'
		pri(self.id,self.q)
		print "ending : "+self.thread_name+'\n'

def pri(id,q):
	while not exitflag:
		queueLock.acquire()
		if not workQueue.empty():
			data=q.get()
			queueLock.release()
			print 'hai'+id+' '+data+'\n'
			time.sleep(5)
			print 'hello'+id+' '+data+'\n'
			time.sleep(5)
			print 'bye'+id+' '+data+'\n'
		else:
			queueLock.release()	

queueLock=threading.Lock()
workQueue=Queue.Queue(10)

thread1=Mythread('rama','USA',workQueue)
thread2=Mythread('bheema','CAD',workQueue)

thread2.start()
thread1.start()
queueLock.acquire()
workQueue.put('one')
workQueue.put('two')
workQueue.put('three')
workQueue.put('four')
queueLock.release()
while not workQueue.empty():
	pass

exitflag=1
thread1.join()
thread2.join()

print "main thread exection completed"
