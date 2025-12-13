def test_shopping_list_exists():
    "la shopping list esiste"
    from main import ShoppingList
    my_list = ShoppingList()
    assert my_list is not None

def test_shopping_list_add_item():
    "si può aggiungere un elemento alla shopping list"
    from main import ShoppingList
    my_list = ShoppingList()
    my_list.add_item("mele")
    
def test_add_item_and_it_is_saved():
    "dopo aver aggiunto un elemento, questo è salvato nella lista"
    from main import ShoppingList
    my_list = ShoppingList()
    my_list.add_item("banane")
    assert "banane" in my_list.items