# Create a store class with a name and categories


class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        output = ""
        i = 1

        output += self.name + "\n"
        for category in self.categories:
            output += " " + str(i) + "." + category + "\n"
            i += 1

        return output


my_store = Store("Bob's store", ["shoes", "Hat", "Helicopters"])
print(my_store)
