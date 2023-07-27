class TokenRing:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.coordinator = num_processes - 1

    def pass_token(self, process_id):
        next_process = (process_id + 1) % self.num_processes
        if next_process == self.coordinator:
            print(f"Process {self.coordinator} is the coordinator and terminates the election.")
            return
        else:
            print(f"Process {process_id} passes the token to process {next_process}.")
            self.pass_token(next_process)

# Exemple d'utilisation avec 3 processus ayant les IDs de 0 à 2
token_ring = TokenRing(3)
# Dans le processus 0
token_ring.pass_token(0)
