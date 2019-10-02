# create a category class with a name for now
# and build upon it further in future iterations


class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"No product available in {self.name}"
