import pytest
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):

    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("Water")
        assert search_page.display_status_of_valid_item()

    def test_search_for_an_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("Honda")
        expected_text = "Restaurant List"
        assert search_page.retrieve_no_item_message().__eq__(expected_text)

    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        expected_text = "Restaurant List.ABC"
        assert search_page.retrieve_no_item_message().__eq__(expected_text)

