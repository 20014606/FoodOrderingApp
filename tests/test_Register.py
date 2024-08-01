from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):
    def test_register_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/FoodApp.xlsx","RegisterTest",2,1),
            self.generate_email_with_time_stamp(),"Rakesh123","Rakesh123")
        assert account_success_page.retrieve_account_creation_message()

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Sonu",self.generate_email_with_time_stamp(),"Rajju123","Rajju123")
        assert account_success_page.retrieve_account_creation_message()

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("rohit","ro@gmail.com","Daksh123","Daksh123")
        expected_warning_message = "User with this Email already exists."
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("","","","")
        assert register_page.verify_all_warnings("**username field is required**", "**Email field is required**", "**Password field is required**", "**Confirm password field is required**")



