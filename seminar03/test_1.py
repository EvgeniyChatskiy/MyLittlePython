import time

from testpage import OperationsHelper, ContactPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import yaml
import logging
from testpage import TestSearchLocators

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'img.jpg')

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_unsuccessful_login(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_successful_login(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['email'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    hello_text = testpage.find_element(TestSearchLocators.LOCATOR_HELLO_TEXT).text
    assert f"Hello, {testdata['email']}" == hello_text


def test_user_can_create_post(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['email'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.create_post_btn()
    testpage.enter_title(testdata['title'])
    testpage.enter_description(testdata['description'])
    testpage.enter_content(testdata['content'])
    testpage.attach_image(file_path)
    testpage.save_post()
    testpage.find_element(TestSearchLocators.LOCATOR_POST_IMAGE)
    post_title = testpage.find_element(TestSearchLocators.LOCATOR_POST_TITLE).text
    logging.info(f"We found text {post_title} on the page of the post")
    assert post_title == testdata['title']


def test_check_contact_us(browser):
    login_page = OperationsHelper(browser)
    login_page.go_to_site()
    login_page.login(testdata['email'], testdata['password'])
    login_page.contact_btn()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.input_name(testdata['contact_name'])
    contact_page.input_email(testdata['contact_email'])
    contact_page.input_content(testdata['contact_content'])
    contact_page.submit_form()
    time.sleep(2)
    text = contact_page.get_text_from_alert()
    assert text == 'Form successfully submitted'
