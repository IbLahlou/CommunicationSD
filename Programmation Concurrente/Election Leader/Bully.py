class BullyAlgorithm:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.coordinator = num_processes - 1

    def election(self, process_id):
        for i in range(process_id + 1, self.num_processes):
            if i > process_id:
                print(f"Process {process_id} sends election message to process {i}")

    def coordinator_elected(self, process_id):
        print(f"Process {process_id} acknowledges process {self.coordinator} as coordinator")

# Exemple d'utilisation avec 5 processus ayant les IDs de 0 à 4
bully = BullyAlgorithm(5)
# Dans le processus 2
bully.election(2)
# Dans le processus 4 (élection réussie)
bully.coordinator_elected(4)
