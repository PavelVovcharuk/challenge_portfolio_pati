import driver

from pages.base_page import BasePage
#
#
class LoginPage(BasePage):
 login_field_xpath = driver.find_element_by_id("//*[@id='login']")
 password_field_xpath = driver.find_element_by_id("//*[@id='password']")
 sign_in_button_xpath = driver.find_element_by_id("//*[@id='Sign in']")

def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
