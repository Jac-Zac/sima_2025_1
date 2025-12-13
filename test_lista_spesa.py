def test_shopping_list_exists():
    from main import ShoppingList
    my_list = ShoppingList()
    assert my_list is not None