class RingAlgorithm:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.coordinator = num_processes - 1

    def election(self, process_id):
        next_process = (process_id + 1) % self.num_processes
        while next_process != process_id:
            if next_process > process_id:
                print(f"Process {process_id} sends election message to process {next_process}")
            next_process = (next_process + 1) % self.num_processes

    def coordinator_elected(self, process_id):
        print(f"Process {process_id} acknowledges process {self.coordinator} as coordinator")

# Exemple d'utilisation avec 4 processus ayant les IDs de 0 à 3
ring = RingAlgorithm(4)
# Dans le processus 1
ring.election(1)
# Dans le processus 3 (élection réussie)
ring.coordinator_elected(3)
