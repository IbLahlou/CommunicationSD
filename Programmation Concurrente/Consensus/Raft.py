class Raft:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.leader = None

    def elect_leader(self, node_id):
        if self.leader is None:
            self.leader = node_id

    def get_leader(self):
        return self.leader

# Exemple d'utilisation avec 5 nœuds ayant les IDs de 0 à 4
raft = Raft(5)
# Dans le nœud 3
raft.elect_leader(3)
# Dans le nœud 1
raft.elect_leader(1)
print("Current leader:", raft.get_leader())
