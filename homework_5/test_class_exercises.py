# -*- coding: utf-8 -*-

"""
Unit tests for class_exercises.py (exercises 27, 28, and book store classes).
"""
import io
import unittest
from unittest.mock import patch

from homework_5.class_exercises import (
    BankingSystem,
    Book,
    BookStore,
    Product,
    ShoppingCart,
)


class TestBankingSystem(unittest.TestCase):
    """Test cases for exercise 27: BankingSystem class."""

    def setUp(self):
        """Create a fresh BankingSystem instance for each test."""
        self.bank = BankingSystem()

    def test_authenticate_success(self):
        """Valid credentials and not logged in should succeed."""
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.authenticate("user123", "pass123")
        self.assertTrue(result)
        self.assertIn("user123", self.bank.logged_in_users)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "User user123 authenticated successfully.")

    def test_authenticate_wrong_password(self):
        """Invalid password should fail."""
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.authenticate("user123", "wrong")
        self.assertFalse(result)
        self.assertNotIn("user123", self.bank.logged_in_users)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Authentication failed.")

    def test_authenticate_user_already_logged_in(self):
        """Already logged in user cannot authenticate again."""
        self.bank.authenticate("user123", "pass123")
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.authenticate("user123", "pass123")
        self.assertFalse(result)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "User already logged in.")

    def test_transfer_money_sender_not_authenticated(self):
        """Transfer from a user not logged in should be rejected."""
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.transfer_money("user123", "receiver", 100, "regular")
        self.assertFalse(result)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Sender not authenticated.")

    def test_transfer_money_insufficient_funds(self):
        """Transfer with amount + fee > 1000 should fail."""
        self.bank.authenticate("user123", "pass123")
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.transfer_money("user123", "receiver", 1000, "regular")
        self.assertFalse(result)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Insufficient funds.")

    def test_transfer_money_successful_regular(self):
        """Successful regular transfer with sufficient funds."""
        self.bank.authenticate("user123", "pass123")
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.transfer_money("user123", "receiver", 500, "regular")
        self.assertTrue(result)
        output = mock_stdout.getvalue().strip()
        expected = (
            "Money transfer of $500 (regular transfer) "
            "from user123 to receiver processed successfully."
        )
        self.assertEqual(output, expected)

    def test_transfer_money_successful_express(self):
        """Successful express transfer."""
        self.bank.authenticate("user123", "pass123")
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.transfer_money("user123", "receiver", 500, "express")
        self.assertTrue(result)
        output = mock_stdout.getvalue().strip()
        expected = (
            "Money transfer of $500 (express transfer) "
            "from user123 to receiver processed successfully."
        )
        self.assertEqual(output, expected)

    def test_transfer_money_successful_scheduled(self):
        """Successful scheduled transfer."""
        self.bank.authenticate("user123", "pass123")
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.transfer_money("user123", "receiver", 500, "scheduled")
        self.assertTrue(result)
        output = mock_stdout.getvalue().strip()
        expected = (
            "Money transfer of $500 (scheduled transfer) "
            "from user123 to receiver processed successfully."
        )
        self.assertEqual(output, expected)

    def test_transfer_money_invalid_transaction_type(self):
        """Invalid transaction type should be rejected."""
        self.bank.authenticate("user123", "pass123")
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            result = self.bank.transfer_money("user123", "receiver", 500, "invalid")
        self.assertFalse(result)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Invalid transaction type.")


class TestShoppingCart(unittest.TestCase):
    """Test cases for exercise 28: Product and ShoppingCart classes."""

    def setUp(self):
        """Create products and a cart for testing."""
        self.product1 = Product("Laptop", 1000)
        self.product2 = Product("Mouse", 20)
        self.cart = ShoppingCart()

    def test_add_product_new(self):
        """Add a new product to cart with default quantity."""
        self.cart.add_product(self.product1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)
        self.assertEqual(self.cart.items[0]["quantity"], 1)

    def test_add_product_new_with_quantity(self):
        """Add a new product with explicit quantity."""
        self.cart.add_product(self.product2, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_add_product_existing(self):
        """Add more of an existing product."""
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product1, 3)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 5)

    def test_remove_product_decrease_quantity(self):
        """Remove part of the quantity of an existing product."""
        self.cart.add_product(self.product1, 5)
        self.cart.remove_product(self.product1, 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["quantity"], 3)

    def test_remove_product_remove_item(self):
        """Remove all quantity of a product should delete the item."""
        self.cart.add_product(self.product1, 3)
        self.cart.remove_product(self.product1, 3)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_more_than_available(self):
        """Remove more than available should remove the item completely."""
        self.cart.add_product(self.product1, 2)
        self.cart.remove_product(self.product1, 5)
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_product_nonexistent(self):
        """Removing a product not in cart does nothing."""
        self.cart.add_product(self.product1, 2)
        self.cart.remove_product(self.product2, 1)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["product"], self.product1)

    def test_view_cart(self):
        """view_cart should print each item's details."""
        self.cart.add_product(self.product1, 2)
        self.cart.add_product(self.product2, 5)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.cart.view_cart()
        output = mock_stdout.getvalue().strip().split("\n")
        expected = ["2 x Laptop - $2000", "5 x Mouse - $100"]
        self.assertEqual(output, expected)

    def test_checkout(self):
        """checkout should print total and thank you message."""
        self.cart.add_product(self.product1, 2)  # 2*1000 = 2000
        self.cart.add_product(self.product2, 5)  # 5*20 = 100
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.cart.checkout()
        output = mock_stdout.getvalue().strip().split("\n")
        self.assertEqual(output[0], "Total: $2100")
        self.assertEqual(output[1], "Checkout completed. Thank you for shopping!")


class TestBook(unittest.TestCase):
    """Test cases for Book class from book store."""

    def setUp(self):
        self.book = Book("The Hobbit", "J.R.R. Tolkien", 15.99, 10)

    def test_init(self):
        """Test that attributes are set correctly."""
        self.assertEqual(self.book.title, "The Hobbit")
        self.assertEqual(self.book.author, "J.R.R. Tolkien")
        self.assertEqual(self.book.price, 15.99)
        self.assertEqual(self.book.quantity, 10)

    def test_display(self):
        """Test that display prints the correct information."""
        expected_output = (
            "Title: The Hobbit\n"
            "Author: J.R.R. Tolkien\n"
            "Price: $15.99\n"
            "Quantity: 10"
        )
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.book.display()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, expected_output)


class TestBookStore(unittest.TestCase):
    """Test cases for BookStore class from book store."""

    def setUp(self):
        self.store = BookStore()
        self.book1 = Book("Book One", "Author A", 10.0, 5)
        self.book2 = Book("Book Two", "Author B", 20.0, 3)

    def test_add_book(self):
        """Test that add_book adds a book to the store."""
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.store.add_book(self.book1)
        self.assertEqual(len(self.store.books), 1)
        self.assertIn(self.book1, self.store.books)
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Book 'Book One' added to the store.")

    def test_display_books_empty(self):
        """Test display_books when no books exist."""
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.store.display_books()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "No books in the store.")

    def test_display_books_with_books(self):
        """Test display_books with one or more books."""
        self.store.add_book(self.book1)
        self.store.add_book(self.book2)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.store.display_books()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Books available in the store:", output)
        self.assertIn("Title: Book One", output)
        self.assertIn("Title: Book Two", output)

    def test_search_book_found(self):
        """Test searching for a book that exists (case insensitive)."""
        self.store.add_book(self.book1)
        self.store.add_book(self.book2)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.store.search_book("book one")
        output = mock_stdout.getvalue().strip()
        self.assertIn("Found 1 book(s) with title 'book one':", output)
        self.assertIn("Title: Book One", output)

    def test_search_book_not_found(self):
        """Test searching for a book that does not exist."""
        self.store.add_book(self.book1)
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.store.search_book("Nonexistent")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "No book found with title 'Nonexistent'.")


if __name__ == "__main__":
    unittest.main()
