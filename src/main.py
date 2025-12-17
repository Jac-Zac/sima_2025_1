from list_utils import ShoppingList

if __name__ == "__main__":
    # Esempio di utilizzo
    my_list = ShoppingList()
    input("Benvenuto nella tua lista della spesa!\nPremi Invio per continuare...")

    stop = False
    while not stop:
        item_to_insert = input(
            "Inserisci un elemento da aggiungere alla lista (o digita 'exit' per terminare): "
        )
        if item_to_insert.lower() == "exit":
            stop = True
        else:
            quantity = int(input(f"Inserisci la quantità di {item_to_insert}: "))
            my_list.add_item(ListItem(item_to_insert, quantity))

    print("Lista della spesa:")
    print(my_list.print_all_items())
    print("Quantità totale di elementi:", my_list.total_quantity())
