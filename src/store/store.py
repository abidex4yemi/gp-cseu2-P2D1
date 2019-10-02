import category

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
            print(category)
            output += " " + str(i) + "." + category.name + "\n"
            i += 1

        output += " " + str(i) + "." + "Press 4 for exit"
        return output


all_product_category = ["shoes", "Hat", "Helicopters", "Belts"]

for each_category in all_product_category:
    all_product_category.append(category.Category(each_category))

my_store = Store("Bob's store", all_product_category)
print(my_store)


# # Create basic interactive commandline app
# selection = 0
# while int(selection) != len(my_store.categories):
#     try:
#         selection = int(input("Select the number of the department."))
#         if selection == len(my_store.categories) + 1:
#             print("Thanks for shopping at" + my_store.name)
#         elif selection > 0 and selection <= len(my_store.categories):
#             print(my_store.categories[selection - 1])
#         else:
#             print("Select a valid number")
#     except ValueError:
#         print("Please enter your choice as a number")
