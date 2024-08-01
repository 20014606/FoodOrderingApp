from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    account_creation_message_xpath = "//h1[text()='ORDER FOOD AND GET THE ITEMS']"

    def retrieve_account_creation_message(self):
        return self.check_display_status_of_element("account_creation_message_xpath",self.account_creation_message_xpath)




