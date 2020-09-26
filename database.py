from Node import Node


class Database:

    def __init__(self, node=None):
        self.db = []
        self.db.append(Node(node))
        self.extract = {}

    def __getitem__(self, item):
        return self.db[item]

    @property
    def display(self):
        return print([(element.label, element.parent.label, element.status) for element in self.db if element.parent is not None])

    def add_nodes(self, l_nodes):
        for idx, element in enumerate(l_nodes):
            self.db.append(Node(l_nodes[idx][0], self.get_parent(l_nodes[idx][1])))
            self.db[len(self.db)-1].parent.children.append(self.db[len(self.db)-1])
            if not self.extract:
                continue
            else:
                self.update_status(self.db[len(self.db)-1].parent)

    def update_status(self, node, status="granularity_staged"):
        node.status = status
        for child in node.children:
            child.status = "coverage_staged"

    def get_parent(self, value):
        for element in self.db:
            if element.is_parent(value):
                return element

    def add_extract(self, extract):
        self.extract = extract

    @property
    def get_extract(self):
        status = {}

        for img, nodes in self.extract.items():
            status.setdefault(img, [])
            for node in nodes:
                if self.find_status(node) is not None:
                    status[img].append(self.find_status(node))
                else:
                    status[img] = "invalid"
                    break

            if "invalid" in status[img]:
                continue
            elif "coverage_staged" in status[img]:
                status[img] = "coverage_staged"
            elif "granularity_staged" in status[img]:
                status[img] = "granularity_staged"
            else:
                status[img] = "valid"

        return print(status)

    def find_status(self, tag):
        return next((x for x in self.db if x.label == tag), None).status \
            if next((x for x in self.db if x.label == tag), None) is not None else None





