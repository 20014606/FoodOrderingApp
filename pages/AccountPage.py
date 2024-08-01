from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    edit_your_account_information_option_xpath = "//h1[text()='ORDER FOOD AND GET THE ITEMS']"

    def display_status_of_edit_your_account_information_option(self):
        return self.check_display_status_of_element("edit_your_account_information_option_xpath",self.edit_your_account_information_option_xpath)

