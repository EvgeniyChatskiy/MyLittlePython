import time
from testpage import OperationsHelper, ContactPage, TestSearchLocators, TestApi

import yaml
import logging


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
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    hello_text = testpage.find_element(TestSearchLocators.LOCATOR_HELLO_TEXT).text
    assert f"Hello, {testdata['login']}" == hello_text


def test_user_can_create_post(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.create_post_btn()
    testpage.enter_title(testdata['title'])
    testpage.enter_description(testdata['description'])
    testpage.enter_content(testdata['content'])
    testpage.save_post()
    testpage.find_element(TestSearchLocators.LOCATOR_POST_IMAGE)
    time.sleep(3)
    post_title = testpage.find_element(TestSearchLocators.LOCATOR_POST_TITLE).text
    logging.info(f"We found text {post_title} on the page of the post")
    assert post_title == testdata['title']


def test_check_contact_us(browser):
    login_page = OperationsHelper(browser)
    login_page.go_to_site()
    login_page.login(testdata['login'], testdata['password'])
    login_page.contact_btn()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.input_name(testdata['contact_name'])
    contact_page.input_email(testdata['contact_email'])
    contact_page.input_content(testdata['contact_content'])
    contact_page.submit_form()
    time.sleep(2)
    text = contact_page.get_text_from_alert()
    assert text == 'Form successfully submitted'


def test_api_get_posts(login):
    response = TestApi.get_response_get_posts(login, order='DESC')
    titles = [i["title"] for i in response.json()['data']]
    logging.info(f"We have got posts")
    assert response.status_code == 200 and testdata['title_test_rest'] in titles


def test_api_create_post(login):
    response = TestApi.create_post(login)
    logging.info(f'New post was created')
    response2 = TestApi.get_response_get_posts(login)
    descriptions = [i["description"] for i in response2.json()['data']]
    if response.status_code == response2.status_code == 200:
        assert testdata['description_create_rest'] in descriptions
