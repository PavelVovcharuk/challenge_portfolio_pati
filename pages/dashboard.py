import driver

from pages.base_page import BasePage

class Dashboard(BasePage):
    Main_page_button_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]")
    Players_button_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]")
    Polski_button_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]")
    Sign_out_button_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]")
    Add_player_hyperlink_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button")
    Dev_team_contact_hyperlink_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a")
    Super_man_hyperlink_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a/button")
    Submit_button_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]")
    Add_language_button_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a")
    Clear_button_xpath = driver.find_element_by_xpath("//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]")
    pass