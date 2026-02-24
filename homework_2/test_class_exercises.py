# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from homework_2.class_exercises import (
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


class TestNumberStatus(unittest.TestCase):
    """Tests for number status functions."""

    def test_check_number_status_positive(self):
        """Test that positive numbers return 'Positive'."""
        self.assertEqual(check_number_status(10), "Positive")

    def test_check_number_status_negative(self):
        """Test that negative numbers return 'Negative'."""
        self.assertEqual(check_number_status(-5), "Negative")

    def test_check_number_status_zero(self):
        """Test that zero returns 'Zero'."""
        self.assertEqual(check_number_status(0), "Zero")


class TestTemperatureConversion(unittest.TestCase):
    """Tests for temperature conversion."""

    def test_celsius_to_fahrenheit_valid(self):
        """Test valid Celsius to Fahrenheit conversion."""
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_celsius_to_fahrenheit_below_min(self):
        """Test temperature below -100 returns 'Invalid Temperature'."""
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_above_max(self):
        """Test temperature above 100 returns 'Invalid Temperature'."""
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestPasswordValidation(unittest.TestCase):
    """Tests for password validation."""

    def test_validate_password_valid(self):
        """Test valid password meets all criteria."""
        self.assertTrue(validate_password("Pass123!@#"))

    def test_validate_password_too_short(self):
        """Test password too short returns False."""
        self.assertFalse(validate_password("Pa1!"))

    def test_validate_password_no_uppercase(self):
        """Test password with no uppercase returns False."""
        self.assertFalse(validate_password("pass123!@#"))

    def test_validate_password_no_lowercase(self):
        """Test password with no lowercase returns False."""
        self.assertFalse(validate_password("PASS123!@#"))

    def test_validate_password_no_digit(self):
        """Test password with no digit returns False."""
        self.assertFalse(validate_password("Pass!@#"))

    def test_validate_password_no_special(self):
        """Test password with no special character returns False."""
        self.assertFalse(validate_password("Pass1234"))


class TestLoginValidation(unittest.TestCase):
    """Tests for login validation."""

    def test_validate_login_successful(self):
        """Test successful login with valid credentials."""
        self.assertEqual(validate_login("username", "password12"), "Login Successful")

    def test_validate_login_username_too_short(self):
        """Test login fails when username is too short."""
        self.assertEqual(validate_login("usr", "password12"), "Login Failed")

    def test_validate_login_username_too_long(self):
        """Test login fails when username is too long."""
        self.assertEqual(validate_login("u" * 21, "password12"), "Login Failed")

    def test_validate_login_password_too_short(self):
        """Test login fails when password is too short."""
        self.assertEqual(validate_login("username", "pass"), "Login Failed")

    def test_validate_login_password_too_long(self):
        """Test login fails when password is too long."""
        self.assertEqual(validate_login("username", "p" * 16), "Login Failed")


class TestEmailValidation(unittest.TestCase):
    """Tests for email validation."""

    def test_validate_email_valid(self):
        """Test valid email returns 'Valid Email'."""
        self.assertEqual(validate_email("test@example.com"), "Valid Email")
        self.assertEqual(validate_email("a@b.co"), "Valid Email")

    def test_validate_email_too_short(self):
        """Test email too short returns 'Invalid Email'."""
        self.assertEqual(validate_email("a@b."), "Invalid Email")

    def test_validate_email_too_long(self):
        """Test email too long returns 'Invalid Email'."""
        self.assertEqual(validate_email("a" * 40 + "@example.com"), "Invalid Email")

    def test_validate_email_no_at_symbol(self):
        """Test email with no @ returns 'Invalid Email'."""
        self.assertEqual(validate_email("testexample.com"), "Invalid Email")

    def test_validate_email_no_dot(self):
        """Test email with no dot returns 'Invalid Email'."""
        self.assertEqual(validate_email("test@examplecom"), "Invalid Email")


class TestCreditCardValidation(unittest.TestCase):
    """Tests for credit card validation."""

    def test_validate_credit_card_valid(self):
        """Test valid card number returns 'Valid Card'."""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_too_short(self):
        """Test card too short returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_too_long(self):
        """Test card too long returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_non_digit(self):
        """Test card with non-digits returns 'Invalid Card'."""
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")


class TestDateValidation(unittest.TestCase):
    """Tests for date validation."""

    def test_validate_date_valid(self):
        """Test valid date returns 'Valid Date'."""
        self.assertEqual(validate_date(2000, 5, 15), "Valid Date")
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_validate_date_year_too_low(self):
        """Test year below 1900 returns 'Invalid Date'."""
        self.assertEqual(validate_date(1899, 5, 15), "Invalid Date")

    def test_validate_date_year_too_high(self):
        """Test year above 2100 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2101, 5, 15), "Invalid Date")

    def test_validate_date_month_too_low(self):
        """Test month below 1 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 0, 15), "Invalid Date")

    def test_validate_date_month_too_high(self):
        """Test month above 12 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 13, 15), "Invalid Date")

    def test_validate_date_day_too_low(self):
        """Test day below 1 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 5, 0), "Invalid Date")

    def test_validate_date_day_too_high(self):
        """Test day above 31 returns 'Invalid Date'."""
        self.assertEqual(validate_date(2000, 5, 32), "Invalid Date")


class TestURLValidation(unittest.TestCase):
    """Tests for URL validation."""

    def test_validate_url_valid_http(self):
        """Test valid http URL returns 'Valid URL'."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_valid_https(self):
        """Test valid https URL returns 'Valid URL'."""
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_too_long(self):
        """Test URL too long returns 'Invalid URL'."""
        self.assertEqual(validate_url("http://" + "a" * 250), "Invalid URL")

    def test_validate_url_no_protocol(self):
        """Test URL with no protocol returns 'Invalid URL'."""
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_validate_url_wrong_protocol(self):
        """Test URL with wrong protocol returns 'Invalid URL'."""
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")


class TestDiscountCalculations(unittest.TestCase):
    """Tests for discount calculation functions."""

    def test_calculate_total_discount_under_100(self):
        """Test no discount for amount under 100."""
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_between_100_and_500(self):
        """Test 10% discount for amount between 100 and 500."""
        self.assertEqual(calculate_total_discount(200), 20)

    def test_calculate_total_discount_over_500(self):
        """Test 20% discount for amount over 500."""
        self.assertEqual(calculate_total_discount(600), 120)


class TestOrderTotal(unittest.TestCase):
    """Tests for order total calculations."""

    def test_calculate_order_total_quantity_1_to_5(self):
        """Test no discount for quantity 1-5."""
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_calculate_order_total_quantity_6_to_10(self):
        """Test 5% discount for quantity 6-10."""
        items = [{"quantity": 8, "price": 10}]
        self.assertEqual(calculate_order_total(items), 76)

    def test_calculate_order_total_quantity_over_10(self):
        """Test 10% discount for quantity over 10."""
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 135)

    def test_calculate_order_total_multiple_items(self):
        """Test total with multiple items."""
        items = [
            {"quantity": 3, "price": 10},
            {"quantity": 8, "price": 10},
            {"quantity": 15, "price": 10},
        ]
        self.assertEqual(calculate_order_total(items), 241)


class TestQuantityDiscount(unittest.TestCase):
    """Tests for quantity-based discounts."""

    def test_calculate_quantity_discount_1_to_5(self):
        """Test quantity 1-5 gives 'No Discount'."""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(3), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_calculate_quantity_discount_6_to_10(self):
        """Test quantity 6-10 gives '5% Discount'."""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_calculate_quantity_discount_over_10(self):
        """Test quantity over 10 gives '10% Discount'."""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(calculate_quantity_discount(20), "10% Discount")


class TestShippingCosts(unittest.TestCase):
    """Tests for shipping cost calculations."""

    def test_calculate_items_shipping_cost_standard_under_5(self):
        """Test standard shipping cost for weight <=5."""
        items = [{"weight": 2}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_5_to_10(self):
        """Test standard shipping cost for weight 5-10."""
        items = [{"weight": 4}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_over_10(self):
        """Test standard shipping cost for weight >10."""
        items = [{"weight": 6}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_under_5(self):
        """Test express shipping cost for weight <=5."""
        items = [{"weight": 2}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_5_to_10(self):
        """Test express shipping cost for weight 5-10."""
        items = [{"weight": 4}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_over_10(self):
        """Test express shipping cost for weight >10."""
        items = [{"weight": 6}, {"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_invalid_method(self):
        """Test invalid shipping method raises ValueError."""
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "invalid")


class TestPackageShipping(unittest.TestCase):
    """Tests for package shipping calculations."""

    def test_calculate_shipping_cost_small_package(self):
        """Test small package cost is 5."""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_medium_package(self):
        """Test medium package cost is 10."""
        self.assertEqual(calculate_shipping_cost(3, 20, 20, 20), 10)

    def test_calculate_shipping_cost_large_package(self):
        """Test large package cost is 20."""
        self.assertEqual(calculate_shipping_cost(6, 20, 20, 20), 20)
        self.assertEqual(calculate_shipping_cost(3, 40, 20, 20), 20)


class TestAgeVerification(unittest.TestCase):
    """Tests for age verification."""

    def test_verify_age_eligible(self):
        """Test age within 18-65 is eligible."""
        self.assertEqual(verify_age(25), "Eligible")
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_not_eligible_under_18(self):
        """Test age under 18 is not eligible."""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_not_eligible_over_65(self):
        """Test age over 65 is not eligible."""
        self.assertEqual(verify_age(66), "Not Eligible")


class TestFlightEligibility(unittest.TestCase):
    """Tests for flight eligibility."""

    def test_check_flight_eligibility_age_eligible_only(self):
        """Test age 18-65 is eligible even if not frequent flyer."""
        self.assertEqual(check_flight_eligibility(25, False), "Eligible to Book")

    def test_check_flight_eligibility_frequent_flyer_only(self):
        """Test frequent flyer is eligible even if age out of range."""
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_check_flight_eligibility_not_eligible(self):
        """Test not eligible when age out of range and not frequent flyer."""
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


class TestFileSize(unittest.TestCase):
    """Tests for file size validation."""

    def test_check_file_size_valid(self):
        """Test file size within 0-1MB is valid."""
        self.assertEqual(check_file_size(0), "Valid File Size")
        self.assertEqual(check_file_size(500000), "Valid File Size")
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_negative(self):
        """Test negative file size is invalid."""
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_check_file_size_too_large(self):
        """Test file size over 1MB is invalid."""
        self.assertEqual(check_file_size(1048577), "Invalid File Size")


class TestLoanEligibility(unittest.TestCase):
    """Tests for loan eligibility."""

    def test_check_loan_eligibility_income_below_30k(self):
        """Test income <30000 returns Not Eligible."""
        self.assertEqual(check_loan_eligibility(25000, 800), "Not Eligible")
        self.assertEqual(check_loan_eligibility(25000, 600), "Not Eligible")

    def test_check_loan_eligibility_income_30k_to_60k_with_good_credit(self):
        """Test income 30-60k with credit >700 gives Standard Loan."""
        self.assertEqual(check_loan_eligibility(45000, 750), "Standard Loan")

    def test_check_loan_eligibility_income_30k_to_60k_with_bad_credit(self):
        """Test income 30-60k with credit <=700 gives Secured Loan."""
        self.assertEqual(check_loan_eligibility(45000, 700), "Secured Loan")

    def test_check_loan_eligibility_income_above_60k_with_excellent_credit(self):
        """Test income >60k with credit >750 gives Premium Loan."""
        self.assertEqual(check_loan_eligibility(80000, 800), "Premium Loan")

    def test_check_loan_eligibility_income_above_60k_with_good_credit(self):
        """Test income >60k with credit <=750 gives Standard Loan."""
        self.assertEqual(check_loan_eligibility(80000, 750), "Standard Loan")


class TestProductCategorization(unittest.TestCase):
    """Tests for product categorization."""

    def test_categorize_product_category_a(self):
        """Test price 10-50 is Category A."""
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(30), "Category A")
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_category_b(self):
        """Test price 51-100 is Category B."""
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(75), "Category B")
        self.assertEqual(categorize_product(100), "Category B")

    def test_categorize_product_category_c(self):
        """Test price 101-200 is Category C."""
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(150), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    def test_categorize_product_category_d(self):
        """Test price below 10 or above 200 is Category D."""
        self.assertEqual(categorize_product(5), "Category D")
        self.assertEqual(categorize_product(250), "Category D")


class TestQuizGrading(unittest.TestCase):
    """Tests for quiz grading."""

    def test_grade_quiz_pass(self):
        """Test pass with >=7 correct and <=2 incorrect."""
        self.assertEqual(grade_quiz(7, 2), "Pass")
        self.assertEqual(grade_quiz(8, 1), "Pass")
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_grade_quiz_conditional_pass(self):
        """Test conditional pass with >=5 correct and <=3 incorrect."""
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(6, 2), "Conditional Pass")

    def test_grade_quiz_fail_too_few_correct(self):
        """Test fail with <5 correct."""
        self.assertEqual(grade_quiz(4, 2), "Fail")

    def test_grade_quiz_fail_too_many_incorrect(self):
        """Test fail with >3 incorrect."""
        self.assertEqual(grade_quiz(7, 4), "Fail")
        self.assertEqual(grade_quiz(5, 4), "Fail")


class TestUserAuthentication(unittest.TestCase):
    """Tests for user authentication."""

    def test_authenticate_user_admin(self):
        """Test admin credentials return Admin."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_valid_user(self):
        """Test valid user credentials return User."""
        self.assertEqual(authenticate_user("username", "password12"), "User")

    def test_authenticate_user_username_too_short(self):
        """Test username too short returns Invalid."""
        self.assertEqual(authenticate_user("user", "password12"), "Invalid")

    def test_authenticate_user_password_too_short(self):
        """Test password too short returns Invalid."""
        self.assertEqual(authenticate_user("username", "pass"), "Invalid")


class TestWeatherAdvisory(unittest.TestCase):
    """Tests for weather advisory."""

    def test_get_weather_advisory_high_temp_high_humidity(self):
        """Test high temperature and humidity advisory."""
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_low_temperature(self):
        """Test low temperature advisory."""
        self.assertEqual(get_weather_advisory(-5, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_no_specific(self):
        """Test no specific advisory for normal conditions."""
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")
        self.assertEqual(get_weather_advisory(35, 60), "No Specific Advisory")
        self.assertEqual(get_weather_advisory(10, 80), "No Specific Advisory")


if __name__ == "__main__":
    unittest.main()
