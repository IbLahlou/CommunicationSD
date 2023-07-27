class DijkstraLock:
    def __init__(self, num_threads):
        self.flag = [False] * num_threads
        self.turn = 0

    def acquire(self, thread_id):
        for other_thread in range(len(self.flag)):
            self.flag[thread_id] = True
            self.turn = other_thread
            while self.flag[other_thread] and self.turn == other_thread:
                pass

    def release(self, thread_id):
        self.flag[thread_id] = False

# Exemple d'utilisation avec 3 threads ayant les IDs 0, 1 et 2
lock = DijkstraLock(3)
# Dans le thread 0
lock.acquire(0)
# Code en section critique
lock.release(0)
