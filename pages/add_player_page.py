from pages.base_page import BasePage

class AddPlayer(BasePage):
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    mainPosition_field_xpath = "//*[@name='mainPosition']"
    age_field_xpath = "//*[@name='age']"
    submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]"
    language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    email_field_xpath = "//*[@name='email']"

    def click_on_the_add_player_button(self) -> object:
        self.click_on_the_element(self.add_player_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_mainPosition(self, mainPosition):
        self.field_send_keys(self.mainPosition_field_xpath,  mainPosition)

    def type_in_age_field(self, age_field):
        self.field_send_keys(self.age_field_xpath,  age_field)

    def click_on_the_add_submit_button(self) -> object:
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_language_button(self) -> object:
        self.click_on_the_element(self.language_button_xpath)

    def click_on_the_sign_out_button(self) -> object:
        self.click_on_the_element(self. sign_out_button_xpath)

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

# "//span[@class='MuiButton-label']"