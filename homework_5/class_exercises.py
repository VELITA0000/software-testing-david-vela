# -*- coding: utf-8 -*-

"""
Banking, shopping cart, and book store examples (exercises 27, 28, and book store).
"""

# pylint: disable=too-few-public-methods


# 27
class BankAccount:  # pylint: disable=too-few-public-methods
    """
    Bank account class.
    """

    def __init__(self, account_number, balance):
        """
        Set the bank account details.
        """
        self.account_number = account_number
        self.balance = balance

    def view_account(self):
        """
        Function to display the account details.
        """
        print(f"The account {self.account_number} has a balance of {self.balance}")


# 27
class BankingSystem:
    """
    Banking system class.
    """

    def __init__(self):
        """
        Mock users.
        """
        self.users = {"user123": "pass123"}  # Simplified user database
        self.logged_in_users = set()

    def authenticate(self, username, password):
        """
        User authentication function.
        """
        if username in self.users and self.users[username] == password:
            if username not in self.logged_in_users:
                self.logged_in_users.add(username)
                print(f"User {username} authenticated successfully.")
                return True

            print("User already logged in.")
        else:
            print("Authentication failed.")

        return False

    def transfer_money(self, sender, receiver, amount, transaction_type):
        """
        Function to perform a money transfer.
        """
        if sender not in self.logged_in_users:
            print("Sender not authenticated.")
            return False

        # Simulate transaction processing logic
        if transaction_type == "regular":
            fee = 0.02 * amount
        elif transaction_type == "express":
            fee = 0.05 * amount
        elif transaction_type == "scheduled":
            fee = 0.01 * amount
        else:
            print("Invalid transaction type.")
            return False

        # Simulate checking for sufficient funds
        if BankAccount(sender, 1000).balance < (amount + fee):
            print("Insufficient funds.")
            return False

        print(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {sender} to {receiver} processed successfully."
        )
        return True


# 28
class Product:  # pylint: disable=too-few-public-methods
    """
    Product class.
    """

    def __init__(self, name, price):
        """
        Set the product details.
        """
        self.name = name
        self.price = price

    def view_product(self):
        """
        Function to display the product details.
        """
        msg = f"The product {self.name} has a price of {self.price}"
        print(msg)
        return msg


# 28
class ShoppingCart:
    """
    Shopping cart class.
    """

    def __init__(self):
        """
        Initialize the shopping cart.
        """
        self.items = []

    def add_product(self, product, quantity=1):
        """
        Function to add a product to the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                break
        else:
            self.items.append({"product": product, "quantity": quantity})

    def remove_product(self, product, quantity=1):
        """
        Function to remove a product from the shopping cart.
        """
        for item in self.items:
            if item["product"] == product:
                if item["quantity"] <= quantity:
                    self.items.remove(item)
                else:
                    item["quantity"] -= quantity
                break

    def view_cart(self):
        """
        Function to display the shopping cart content.
        """
        for item in self.items:
            print(
                f"{item['quantity']} x {item['product'].name}"
                f" - ${item['product'].price * item['quantity']}"
            )

    def checkout(self):
        """
        Function to checkout the items from the shopping cart.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        print(f"Total: ${total}")
        print("Checkout completed. Thank you for shopping!")


# Book store classes (from original book_store.py)
class Book:  # pylint: disable=too-few-public-methods
    """
    Book class.
    """

    def __init__(self, title, author, price, quantity):
        """Book init."""
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def display(self):
        """Displays the book information."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")
        print(f"Quantity: {self.quantity}")


class BookStore:
    """
    Book store class.
    """

    def __init__(self):
        """Book class init."""
        self.books = []

    def add_book(self, book):
        """Adds a book to the store."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the store.")

    def display_books(self):
        """Displays all books available in the store."""
        if not self.books:
            print("No books in the store.")
        else:
            print("Books available in the store:")
            for book in self.books:
                book.display()

    def search_book(self, title):
        """Searches a books in the store."""
        found_books = [
            book for book in self.books if book.title.lower() == title.lower()
        ]
        if not found_books:
            print(f"No book found with title '{title}'.")
        else:
            print(f"Found {len(found_books)} book(s) with title '{title}':")
            for book in found_books:
                book.display()
