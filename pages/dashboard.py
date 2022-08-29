import time
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver
from pages.base_page import BasePage

players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
name_field_xpath = "//*[@name='name']"
surname_field_xpath = "//*[@name='surname']"
mainPosition_field_xpath = "//*[@name='mainPosition']"
age_field_xpath = "//*[@name='age']"
submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]"
language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
email_field_xpath = "//*[@name='email']"

class Dashboard(BasePage):
    futbol_kolektyw_title_xpath = '//*[@title ="Logo Scouts Panel"]'
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
