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


if __name__ == "__main__":
    # Esempio di utilizzo
    my_list = ShoppingList()
    input("Benvenuto nella tua lista della spesa!\nPremi Invio per continuare...")
    stop = False
    while not stop:
        item_to_insert = input("Inserisci un elemento da aggiungere alla lista (o digita 'exit' per terminare): ")
        if item_to_insert.lower() == "exit":
            stop = True
        else:
            quantity = int(input(f"Inserisci la quantità di {item_to_insert}: "))
            my_list.add_item(ListItem(item_to_insert, quantity))
    
    print("Lista della spesa:")
    print(my_list.print_all_items())
    print("Quantità totale di elementi:", my_list.total_quantity())
