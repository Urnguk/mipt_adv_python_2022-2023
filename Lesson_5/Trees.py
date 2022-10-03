class Tree:
    def __init__(self, roots, branches):
        self._roots = roots
        self._branches = branches
        self._type = "Tree"

    def photosynthesis(self):
        print("CO2 -> O2")

    def grow(self):
        print("^")

    def __str__(self):
        return (self._type + " " + str(self._roots)
                + " " + str(self._branches))

class Pine(Tree):
    def __init__(self, roots,
                 branches, needles):
        self._needles = needles
        # super().__init__(roots, branches)
        self._type = "Pine"

    # def __str__(self):
    #     return (super().__str__() + " "
    #             + str(self._needles))

    def grow_cones(self):
        print("shut up and give me some water")


a = Tree(3, 5)
b = Pine(3, 6, 0)
print(a)
print(b._needles)
b.grow_cones()




