import unittest
import time
from selenium import webdriver


class LoginPageTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe")
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        self.driver.get(url)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_check_header_text(self):
        driver = self.driver

        header = driver.find_element_by_css_selector('.wborder')
        header_text = header.text
        self.assertEqual('Wersja demonstracyjna serwisu demobank', header_text, f'expected header on page {url} is differ ')

    def test_button_id_disabled_when_input_is_empty(self):
        driver = self.driver

        login_input = driver.find_element_by_xpath('//div[@id= "login_id_container"]//input')
        clear_login_input = login_input.clear()
        disabled_button = driver.find_element_by_id('login_next')
        disabled_button_value = disabled_button.get_attribute('disabled')
        self.assertEqual('true', disabled_button_value, f'expected value is differ')

    def test_error_alert_is_display_when_user_enter_too_few_letters_in_input(self):
        driver = self.driver

        login_input = driver.find_element_by_xpath('//div[@id= "login_id_container"]//input')
        clear_login_input = login_input.clear()
        type_login = login_input.send_keys('kasia')

        question_mark = driver.find_element_by_css_selector('#login_id_container > div.login-tooltip-wrapper > div > i')
        click_question_mark = question_mark.click()

        error_msg = driver.find_element_by_css_selector('.error')
        error_msg_text = error_msg.text
        self.assertEqual('identyfikator ma min. 8 znaków', error_msg_text, f'expected error msg is differ than actual')

    def test_check_if_password_input_is_display(self):
        driver = self.driver

        login_input = driver.find_element_by_xpath('//div[@id= "login_id_container"]//input')
        clear_login_input = login_input.clear()
        type_login = login_input.send_keys('kasia123')

        next_button = driver.find_element_by_id('login_next')
        next_button.click()
        time.sleep(3)
        header = driver.find_element_by_xpath('//form[@id="login_form"]/h1')
        header_text = header.text
        self.assertEqual('Wersja demonstracyjna serwisu demobank online', header_text, f'expected input name is differ than actual')



