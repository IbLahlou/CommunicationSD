class Paxos:
    def __init__(self):
        self.proposals = []

    def propose(self, value):
        self.proposals.append(value)

    def get_consensus(self):
        if len(self.proposals) > 0:
            return self.proposals[0]
        else:
            return None

# Exemple d'utilisation
paxos = Paxos()
paxos.propose("Option 1")
paxos.propose("Option 2")
print("Consensus decision:", paxos.get_consensus())
