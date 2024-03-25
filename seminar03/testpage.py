from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_HELLO_TEXT = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    LOCATOR_CREATE_POST_BTN = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_TITLE_INPUT = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label')
    LOCATOR_DESCRIPTION_INPUT = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label')
    LOCATOR_CONTENT_INPUT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label')
    LOCATOR_ATTACH_IMAGE = (By.XPATH, '//*[@id="create-item"]/div/div/div[6]/div/div/label/input')
    LOCATOR_SAVE_POST_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_POST_IMAGE = (By.TAG_NAME, 'img')
    LOCATOR_POST_TITLE = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_MENU = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    LOCATOR_LOGOUT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/div/ul/li[3]/span[1]')
    LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')


class ContactPageLocators:
    LOCATOR_CONTACT_NAME_INPUT = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_CONTACT_EMAIL_INPUT = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTACT_CONTENT_INPUT = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_SUBMIT_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()


    def login(self, login, passwd):
        self.enter_login(login)
        self.enter_pass(passwd)
        self.click_login_button()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def create_post_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def enter_title(self, title):
        self.find_element(TestSearchLocators.LOCATOR_TITLE_INPUT).send_keys(title)

    def enter_description(self, description):
        self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_INPUT).send_keys(description)

    def enter_content(self, content):
        self.find_element(TestSearchLocators.LOCATOR_CONTENT_INPUT).send_keys(content)

    def attach_image(self, path):
        self.find_element(TestSearchLocators.LOCATOR_ATTACH_IMAGE).send_keys(path)

    def save_post(self):
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def contact_btn(self):
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()


class ContactPage(BasePage):
    def input_name(self, name):
        self.find_element(ContactPageLocators.LOCATOR_CONTACT_NAME_INPUT).send_keys(name)

    def input_email(self, email):
        self.find_element(ContactPageLocators.LOCATOR_CONTACT_EMAIL_INPUT).send_keys(email)

    def input_content(self, content):
        self.find_element(ContactPageLocators.LOCATOR_CONTACT_CONTENT_INPUT).send_keys(content)

    def submit_form(self):
        self.find_element(ContactPageLocators.LOCATOR_CONTACT_SUBMIT_BTN).click()