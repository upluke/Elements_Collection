# a semaphore is a very powerful synchronization construct. Concepturally, a semaphore maintians a self of permits.
# A thread calling acquire() on a semaphore waits, if necessary, until a permit is available, and then takes it.
# A thread calling release() on a semaphore adds a permit and notifies threads waiting on that semaphore,
# potentially releasing a blocking acquirer.

class Semaphore():
    def __init__(self, max_available):
        self.cv = threading.Condition()
        self.MAX_AVAILABLE = max_available
        self.taken = 0

    def acquire(self):
        self.cv.acquire()
        while(self.taken == self.MAX_AVAILABLE):
            self.cv.wait()
        self.taken += 1
        self.cv.release()

    def release(self):
        self.cv.acquire()
        self.taken -= 1
        self.cv.notify()
        self.cv.release()
