import yaml
import time
from module import Site

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(login, password, error, submit, result, site):
    input1 = site.find_element('xpath', login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', password)
    input2.send_keys('test')
    btn = site.find_element('css', submit)
    btn.click()
    error_label = site.find_element('xpath', error)
    assert error_label.text == result


def test_step2(login, password, submit, result, site):
    input1 = site.find_element('xpath', login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', submit)
    btn.click()
    hello_text = site.find_element('xpath', '//*[@id="app"]/main/nav/ul/li[3]/a').text
    assert f'Hello, {testdata['login']}' == hello_text


def test_step3(login, password, submit, result, site, create_new_post_btn):
    input1 = site.find_element('xpath', login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', password)
    input2.send_keys(testdata['password'])
    btn1 = site.find_element('css', submit)
    btn1.click()
    btn2 = site.find_element('css', create_new_post_btn)
    btn2.click()
    input3 = site.find_element('xpath', '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    input3.send_keys("My Title")
    btn3 = site.find_element('css', '#create-item > div > div > div:nth-child(7) > div > button > span')
    btn3.click()
    time.sleep(testdata['sleep_time'])
    post_title = site.find_element('xpath', '//*[@id="app"]/main/div/div[1]/h1').text
    assert post_title == 'My Title'
