
class Node:

    def __init__(self, label, parent=None):
        self.label = label
        self.parent = parent
        self.images = []
        self.children = []
        self.status = "valid"

    def __eq__(self, other):
        return self.label == other.label

    def is_parent(self, value):
        return self.label == value

    def get_children(self):
        pass
