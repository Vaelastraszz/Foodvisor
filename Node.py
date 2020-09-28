# Node class qui sera utilisée ensuite par notre class database
class Node:
    # constructeur
    def __init__(self, label, parent=None):
        self.label = label
        self.parent = parent
        self.images = []
        self.children = []
        self.status = "valid"

    def __eq__(self, other):
        return self.label == other.label

    def is_parent(self, value):  # Méthode pour savoir si le node est parent ou non
        return self.label == value
