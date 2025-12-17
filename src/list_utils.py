from tools.weird_maths import robust_sum


class ListItem:
    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = quantity


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def print_all_items(self):
        result = ""
        for item in self.items:
            result += f"- {item.name}: {item.quantity}\n"
        return result

    def remove(self, item_to_remove):
        self.items = [item for item in self.items if item.name != item_to_remove]

    def clear(self):
        self.items = []

    def total_quantity(self):
        return robust_sum(item.quantity for item in self.items)
