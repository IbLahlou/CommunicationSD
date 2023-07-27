class BinaryLock:
    def __init__(self):
        self.lock = False

    def acquire(self):
        while self.lock:
            pass
        self.lock = True

    def release(self):
        self.lock = False

# Exemple d'utilisation
lock = BinaryLock()
lock.acquire()
# Code en section critique
lock.release()
