def test_shopping_list_exists():
    "la shopping list esiste"
    from src.main import ShoppingList
    my_list = ShoppingList()
    assert my_list is not None

def test_shopping_list_add_item():
    "si può aggiungere un elemento alla shopping list"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    mele = ListItem("mele")
    my_list.add_item(mele)
    
def test_add_item_and_it_is_saved():
    "dopo aver aggiunto un elemento, questo è salvato nella lista"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    banane = ListItem("banane")
    my_list.add_item(banane)
    banane_in_list = my_list.items[0]
    assert isinstance(banane_in_list, ListItem)
    assert banane_in_list.name == "banane"
    assert banane_in_list.quantity == 1

def test_add_item_and_quantity():
    "dopo aver aggiunto un elemento con quantità, questo è salvato correttamente"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    my_list.add_item(ListItem("arance", 5))
    assert any(item.name == "arance" and item.quantity == 5 for item in my_list.items)

def test_list_current_items():
    "si possono elencare gli elementi attualmente nella lista"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    my_list.add_item(ListItem("pere", 2))
    my_list.add_item(ListItem("uva", 3))
    elenco = my_list.print_all_items()
    assert elenco == """- pere: 2\n- uva: 3\n"""

def test_list_current_other_items():
    "si possono elencare altri elementi attualmente nella lista"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    my_list.add_item(ListItem("latte", 1))
    my_list.add_item(ListItem("pane", 4))
    elenco = my_list.print_all_items()
    assert elenco == """- latte: 1\n- pane: 4\n"""

def test_remove_item():
    "si può rimuovere un elemento dalla lista"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    my_list.add_item(ListItem("yogurt", 2))
    my_list.add_item(ListItem("formaggio", 1))  
    # Rimuovi l'elemento "yogurt"
    my_list.remove("yogurt")
    elenco = my_list.print_all_items()
    assert elenco == """- formaggio: 1\n"""

def test_create_listitem():
    "si può creare un oggetto ListItem"
    from src.main import ListItem
    item = ListItem("cioccolato", 3)
    assert item.name == "cioccolato"
    assert item.quantity == 3

def test_clear_list():
    "si possono rimuovere tutti gli elementi dalla lista"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    my_list.add_item(ListItem("uova", 12))
    my_list.add_item(ListItem("burro", 1))
    # Rimuovi tutti gli elementi
    my_list.clear()
    elenco = my_list.print_all_items()
    assert elenco == ""

def test_total_quantity():
    "si può calcolare la quantità totale degli elementi nella lista"
    from src.main import ShoppingList, ListItem
    my_list = ShoppingList()
    my_list.add_item(ListItem("pomodori", 4))
    my_list.add_item(ListItem("cetrioli", 3))
    my_list.add_item(ListItem("peperoni", 5))
    total = my_list.total_quantity()
    assert total == 12
    