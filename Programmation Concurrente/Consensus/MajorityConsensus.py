class MajorityConsensus:
    def __init__(self):
        self.decisions = []

    def decide(self, value):
        self.decisions.append(value)

    def get_consensus(self):
        return max(set(self.decisions), key=self.decisions.count)

# Exemple d'utilisation
consensus = MajorityConsensus()
consensus.decide("Option 1")
consensus.decide("Option 2")
consensus.decide("Option 1")
print("Consensus decision:", consensus.get_consensus())
