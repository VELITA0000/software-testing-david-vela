# -*- coding: utf-8 -*-

"""
Unit tests for state‑based classes (exercises 22‑26).
"""
import unittest

from homework_3.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
)


class TestVendingMachine(unittest.TestCase):
    """Tests for the VendingMachine class (exercise 22)."""

    def setUp(self):
        """Create a fresh vending machine before each test."""
        self.vm = VendingMachine()

    def test_initial_state(self):
        """Verify the machine starts in Ready state."""
        self.assertEqual(self.vm.state, "Ready")

    def test_insert_coin_when_ready(self):
        """Insert coin in Ready state should transition to Dispensing"""
        result = self.vm.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(self.vm.state, "Dispensing")

    def test_insert_coin_when_dispensing(self):
        """Insert coin in Dispensing state should be invalid."""
        self.vm.state = "Dispensing"  # set directly for test
        result = self.vm.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.vm.state, "Dispensing")  # state unchanged

    def test_select_drink_when_dispensing(self):
        """Select drink in Dispensing state should transition to Ready"""
        self.vm.state = "Dispensing"
        result = self.vm.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(self.vm.state, "Ready")

    def test_select_drink_when_ready(self):
        """Select drink in Ready state should be invalid."""
        self.vm.state = "Ready"
        result = self.vm.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.vm.state, "Ready")

    def test_full_cycle(self):
        """Test a complete purchase cycle: insert coin then select drink."""
        self.assertEqual(self.vm.insert_coin(), "Coin Inserted. Select your drink.")
        self.assertEqual(self.vm.select_drink(), "Drink Dispensed. Thank you!")
        self.assertEqual(self.vm.state, "Ready")


class TestTrafficLight(unittest.TestCase):
    """Tests for the TrafficLight class (exercise 23)."""

    def setUp(self):
        """Create a fresh traffic light before each test."""
        self.tl = TrafficLight()

    def test_initial_state(self):
        """Verify the light starts in Red state."""
        self.assertEqual(self.tl.get_current_state(), "Red")

    def test_change_state_from_red(self):
        """Changing from Red should go to Green."""
        self.tl.change_state()
        self.assertEqual(self.tl.get_current_state(), "Green")

    def test_change_state_from_green(self):
        """Changing from Green should go to Yellow."""
        self.tl.state = "Green"
        self.tl.change_state()
        self.assertEqual(self.tl.get_current_state(), "Yellow")

    def test_change_state_from_yellow(self):
        """Changing from Yellow should go to Red."""
        self.tl.state = "Yellow"
        self.tl.change_state()
        self.assertEqual(self.tl.get_current_state(), "Red")

    def test_full_cycle(self):
        """Test that three changes return to Red."""
        self.tl.change_state()  # Red -> Green
        self.tl.change_state()  # Green -> Yellow
        self.tl.change_state()  # Yellow -> Red
        self.assertEqual(self.tl.get_current_state(), "Red")


class TestUserAuthentication(unittest.TestCase):
    """Tests for the UserAuthentication class (exercise 24)."""

    def setUp(self):
        """Create a fresh auth system before each test."""
        self.auth = UserAuthentication()

    def test_initial_state(self):
        """Verify the system starts in Logged Out state."""
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_when_logged_out(self):
        """Login from Logged Out should succeed and move to Logged In."""
        result = self.auth.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_login_when_logged_in(self):
        """Login from Logged In should be invalid."""
        self.auth.state = "Logged In"
        result = self.auth.login()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged In")

    def test_logout_when_logged_in(self):
        """Logout from Logged In should succeed and move to Logged Out."""
        self.auth.state = "Logged In"
        result = self.auth.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_logout_when_logged_out(self):
        """Logout from Logged Out should be invalid."""
        self.auth.state = "Logged Out"
        result = self.auth.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_full_cycle(self):
        """Test login then logout."""
        self.assertEqual(self.auth.login(), "Login successful")
        self.assertEqual(self.auth.state, "Logged In")
        self.assertEqual(self.auth.logout(), "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")


class TestDocumentEditingSystem(unittest.TestCase):
    """Tests for the DocumentEditingSystem class (exercise 25)."""

    def setUp(self):
        """Create a fresh document system before each test."""
        self.doc = DocumentEditingSystem()

    def test_initial_state(self):
        """Verify the system starts in Editing state."""
        self.assertEqual(self.doc.state, "Editing")

    def test_save_when_editing(self):
        """Save from Editing should succeed and move to Saved."""
        result = self.doc.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.doc.state, "Saved")

    def test_save_when_saved(self):
        """Save from Saved should be invalid."""
        self.doc.state = "Saved"
        result = self.doc.save_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Saved")

    def test_edit_when_saved(self):
        """Edit from Saved should succeed and move to Editing."""
        self.doc.state = "Saved"
        result = self.doc.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.doc.state, "Editing")

    def test_edit_when_editing(self):
        """Edit from Editing should be invalid."""
        self.doc.state = "Editing"
        result = self.doc.edit_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Editing")

    def test_full_cycle(self):
        """Test save then edit."""
        self.assertEqual(self.doc.save_document(), "Document saved successfully")
        self.assertEqual(self.doc.state, "Saved")
        self.assertEqual(self.doc.edit_document(), "Editing resumed")
        self.assertEqual(self.doc.state, "Editing")


class TestElevatorSystem(unittest.TestCase):
    """Tests for the ElevatorSystem class (exercise 26)."""

    def setUp(self):
        """Create a fresh elevator before each test."""
        self.elev = ElevatorSystem()

    def test_initial_state(self):
        """Verify the elevator starts in Idle state."""
        self.assertEqual(self.elev.state, "Idle")

    def test_move_up_when_idle(self):
        """Move up from Idle should succeed and move to Moving Up."""
        result = self.elev.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elev.state, "Moving Up")

    def test_move_up_when_moving_up(self):
        """Move up from Moving Up should be invalid."""
        self.elev.state = "Moving Up"
        result = self.elev.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elev.state, "Moving Up")

    def test_move_up_when_moving_down(self):
        """Move up from Moving Down should be invalid."""
        self.elev.state = "Moving Down"
        result = self.elev.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elev.state, "Moving Down")

    def test_move_down_when_idle(self):
        """Move down from Idle should succeed and move to Moving Down."""
        result = self.elev.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elev.state, "Moving Down")

    def test_move_down_when_moving_down(self):
        """Move down from Moving Down should be invalid."""
        self.elev.state = "Moving Down"
        result = self.elev.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elev.state, "Moving Down")

    def test_move_down_when_moving_up(self):
        """Move down from Moving Up should be invalid."""
        self.elev.state = "Moving Up"
        result = self.elev.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elev.state, "Moving Up")

    def test_stop_when_moving_up(self):
        """Stop from Moving Up should succeed and move to Idle."""
        self.elev.state = "Moving Up"
        result = self.elev.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elev.state, "Idle")

    def test_stop_when_moving_down(self):
        """Stop from Moving Down should succeed and move to Idle."""
        self.elev.state = "Moving Down"
        result = self.elev.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elev.state, "Idle")

    def test_stop_when_idle(self):
        """Stop from Idle should be invalid."""
        self.elev.state = "Idle"
        result = self.elev.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elev.state, "Idle")

    def test_full_cycle_up(self):
        """Test moving up then stopping."""
        self.assertEqual(self.elev.move_up(), "Elevator moving up")
        self.assertEqual(self.elev.state, "Moving Up")
        self.assertEqual(self.elev.stop(), "Elevator stopped")
        self.assertEqual(self.elev.state, "Idle")

    def test_full_cycle_down(self):
        """Test moving down then stopping."""
        self.assertEqual(self.elev.move_down(), "Elevator moving down")
        self.assertEqual(self.elev.state, "Moving Down")
        self.assertEqual(self.elev.stop(), "Elevator stopped")
        self.assertEqual(self.elev.state, "Idle")


if __name__ == "__main__":
    unittest.main()
