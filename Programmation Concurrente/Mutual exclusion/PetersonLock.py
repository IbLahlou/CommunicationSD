class PetersonLock:
    def __init__(self):
        self.flag = [False, False]
        self.turn = 0

    def acquire(self, thread_id):
        self.flag[thread_id] = True
        self.turn = 1 - thread_id
        while self.flag[1 - thread_id] and self.turn == 1 - thread_id:
            pass

    def release(self, thread_id):
        self.flag[thread_id] = False

# Exemple d'utilisation avec deux threads ayant les IDs 0 et 1
lock = PetersonLock()
# Dans le thread 0
lock.acquire(0)
# Code en section critique
lock.release(0)
