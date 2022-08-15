from pages.base_page import BasePage
#
#
class LoginPage(BasePage):
     login_field_xpath = //*[@id="Login"]
     password_field_xpath = //*[@id="__next"]/form/div/div[1]/div[2]
     sign_in_button_xpath = //*[@id="__next"]/form/div/div[2]/button/span[1]

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
