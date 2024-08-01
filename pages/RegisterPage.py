from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_id = "username"
    email_field_id = "email"
    password_field_id = "password1"
    confirm_password_field_id = "password2"
    continue_button_xpath = "//button[contains(text(), 'Submit')]"
    duplicate_email_warning_xpath = "//span[@id='error_1_id_email']/strong[1]"
    first_name_warning_xpath = "//label[@id='username-error']/em[1]"
    confirm_password_warning_xpath = "//label[@id='password2-error']/em[1]"
    email_warning_xpath = "//label[@id='email-error']/em[1]"
    password_warning_xpath = "//label[@id='password1-error']/em[1]"

    def enter_user_name(self,first_name_text):
        self.type_into_element(first_name_text,"first_name_field_id",self.first_name_field_id)

    # def enter_last_name(self,last_name_text):
    #     self.type_into_element(last_name_text,"last_name_field_id",self.last_name_field_id)

    def enter_email(self,email_text):
        self.type_into_element(email_text,"email_field_id",self.email_field_id)

    def enter_password(self,password_text):
        self.type_into_element(password_text,"password_field_id",self.password_field_id)

    def enter_password_confirm(self,password_text):
        self.type_into_element(password_text,"confirm_password_field_id",self.confirm_password_field_id)

    def click_on_continue_button(self):
        self.element_click("continue_button_xpath",self.continue_button_xpath)
        return AccountSuccessPage(self.driver)

    def register_an_account(self,user_name_text,email_text,password_text,password_confirm_text):
        self.enter_user_name(user_name_text)
        self.enter_email(email_text)
        self.enter_password(password_text)
        self.enter_password_confirm(password_confirm_text)
        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning(self):
        return self.retrieve_element_text("duplicate_email_warning_xpath",self.duplicate_email_warning_xpath)

    def retrieve_first_name_warning(self):
        return self.retrieve_element_text("first_name_warning_xpath",self.first_name_warning_xpath)

    def retrieve_confirm_password_warning(self):
        return self.retrieve_element_text("confirm_password_warning_xpath",self.confirm_password_warning_xpath)

    def retrieve_email_warning(self):
        return self.retrieve_element_text("email_warning_xpath",self.email_warning_xpath)

    def retrieve_password_warning(self):
        return self.retrieve_element_text("password_warning_xpath",self.password_warning_xpath)

    def verify_all_warnings(self,expected_first_name_warning_message, expected_email_warning_message, expected_password_warning_message, expected_confirm_password_warning_message):
        actual_first_name_warning_message = self.retrieve_first_name_warning()
        actual_email_warning_message = self.retrieve_email_warning()
        actual_password_warning_message = self.retrieve_password_warning()
        actual_confirm_password_warning_message = self.retrieve_confirm_password_warning()

        status = False

        if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
            if expected_email_warning_message.__eq__(actual_email_warning_message):
                if expected_password_warning_message.__eq__(actual_password_warning_message):
                    if expected_confirm_password_warning_message.__eq__(actual_confirm_password_warning_message):
                        status = True

        return status






