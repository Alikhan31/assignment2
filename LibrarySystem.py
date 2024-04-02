from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, title):
        self.title = title
        self.checked_out = False

    @abstractmethod
    def checkout(self, user):
        pass

    @abstractmethod
    def return_item(self):
        pass

class Book(Item):
    def checkout(self, user):
        if user.can_checkout():
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print("User cannot check out items.")

    def return_item(self):
        self.checked_out = False
        print(f"{self.title} has been returned.")

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def can_checkout(self):
        pass

    @abstractmethod
    def can_return(self):
        pass

class Librarian(User):
    def can_checkout(self):
        return True

    def can_return(self):
        return True

class Catalog:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

def list_items(catalog):
    if catalog.items:
        for item in catalog.items:
            status = "Checked out" if item.checked_out else "Available"
            print(f"{item.title} - {status}")
    else:
        print("No items in the catalog.")

def list_users(user_manager):
    if user_manager.users:
        for user in user_manager.users:
            print(f"{user.name}")
    else:
        print("No users.")

def checkout_item(catalog, user_manager):
    item_title = input("Enter item title to checkout: ")
    user_name = input("Enter user name: ")
    user = next((u for u in user_manager.users if u.name == user_name), None)
    if user:
        item = next((i for i in catalog.items if i.title == item_title and not i.checked_out), None)
        if item:
            item.checkout(user)
        else:
            print("Item not available or already checked out.")
    else:
        print("User not found.")

def return_item(catalog):
    item_title = input("Enter item title to return: ")
    item = next((i for i in catalog.items if i.title == item_title and i.checked_out), None)
    if item:
        item.return_item()
    else:
        print("Item not found or not checked out.")

def add_book(catalog):
    title = input("Enter book title: ")
    catalog.add_item(Book(title))
    print("Book added to the catalog.")

def add_librarian(user_manager):
    name = input("Enter librarian name: ")
    user_manager.add_user(Librarian(name))
    print("Librarian added.")

def main_cli():
    catalog = Catalog()
    user_manager = UserManager()

    commands = {
        "add_book": lambda: add_book(catalog),
        "add_librarian": lambda: add_librarian(user_manager),
        "list_items": lambda: list_items(catalog),
        "list_users": lambda: list_users(user_manager),
        "checkout_item": lambda: checkout_item(catalog, user_manager),
        "return_item": lambda: return_item(catalog),
    }

    while True:
        command = input("Enter command: \nadd_book:\nadd_librarian:\nlist_items:\nlist_users:\ncheckout_item:\nreturn_item:")
        action = commands.get(command)
        if action:
            action()
        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main_cli()
