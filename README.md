
# Shopping List CLI Toy Project

## Project Overview

This project is a simple command-line interface (CLI) application for managing a shopping list. It is designed for beginners and uses only the Python standard library. The user can add, view, and remove items from their shopping list directly from the terminal.

## Specifications

- **Add Item**: The user can add an item to the shopping list by specifying its name (and optionally a quantity).
- **View List**: The user can display all items currently in the shopping list, showing item names and quantities.
- **Remove Item**: The user can remove an item from the shopping list by specifying its name.
- **Clear List**: The user can clear all items from the shopping list.
- **Persistence**: The shopping list is saved to a file (e.g., `shopping_list.txt`) so that it is available the next time the program is run.
- **Help**: The CLI provides a help message describing available commands.
- **Exit**: The user can exit the program gracefully.

## Example CLI Usage

```
$ python shopping_list.py add milk 2
Added 2 x milk to the shopping list.

$ python shopping_list.py list
Shopping List:
- milk (2)

$ python shopping_list.py remove milk
Removed milk from the shopping list.

$ python shopping_list.py clear
Shopping list cleared.

$ python shopping_list.py help
Usage: python shopping_list.py [command] [arguments]
Commands:
	add <item> [quantity]   Add an item (default quantity is 1)
	list                   Show all items
	remove <item>          Remove an item
	clear                  Remove all items
	help                   Show this help message
	exit                   Exit the program
```

## Requirements

- Python 3.7+
- Only standard library modules (e.g., `argparse`, `sys`, `os`)

## Possible Extensions

- Edit item quantities
- Sort items alphabetically
- Mark items as purchased
- Support for categories (e.g., dairy, produce)

---
This project is intended for educational and demonstration purposes in a basic programming course.

