from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    valid_water_item_xpath = "//h5[contains(text(),'Water')]"
    no_item_message_xpath = "//h3[contains(text(),'Restaurant List')]"

    def display_status_of_valid_item(self):
        return self.check_display_status_of_element("valid_water_item_xpath",self.valid_water_item_xpath)

    def retrieve_no_item_message(self):
        return self.retrieve_element_text("no_item_message_xpath",self.no_item_message_xpath)


