import unittest
from selenium import webdriver
import time


class CheckKnowledge(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe")
        self.driver.maximize_window()
        self.base_url = 'https://autodemo.testoneo.com/en/'
        self.login_url = self.base_url + 'login'
        self.sample_product_url = self.base_url + 'men/1-1-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDown(self):
        self.driver.quit()


    def test_check_header_on_login_form_page(self):
        driver = self.driver
        driver.get(self.login_url)
        time.sleep(2)

        header = driver.find_element_by_css_selector('.page-header > h1')
        header_text = header.text
        print(header_text)
        self.assertEqual('Log in to your account', header_text, f'expected header is differ than acctual {self.login_url}')

    def user_login(self, driver, user_email, user_password):
        driver = self.driver
        login_input = driver.find_element_by_xpath('//input[@class="form-control"]').send_keys(user_email)
        password_input = driver.find_element_by_xpath('//input[@type="password"]').send_keys(user_password)
        sign_in_btn = driver.find_element_by_id('submit-login').click()

    def assert_element_text(self, driver, locator, expected_header):
        header_on_page = driver.find_element_by_css_selector(locator)
        header_on_page_text = header_on_page.text

        self.assertEqual(expected_header, header_on_page_text,
                         f'expected element text is differ that actual')

    def test_correct_login(self):
        driver = self.driver
        driver.get(self.login_url)
        user_email = 'kasiatesterkaqa@gmail.com'
        user_password = '123Admin'
        locator = '.logout.hidden-sm-down > i'
        expected_header = 'Sign in'

        self.user_login(driver, user_email, user_password)
        self.assert_element_text(driver, locator,expected_header)

    def test_incorrect_login(self):
        driver = self.driver
        driver.get(self.login_url)
        user_email = 'kasitesterkaqa@gmail.com'
        user_password = '123Admin'
        locator = '.alert.alert-danger'
        expected_header = 'Authentication failed.'

        self.user_login(driver, user_email, user_password)
        self.assert_element_text(driver, locator, expected_header)

    def test_check_product_name(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        locator = '.h1'
        expected_header = 'HUMMINGBIRD PRINTED T-SHIRT'

        self.assert_element_text(driver, locator, expected_header)

    def test_check_product_price(self):
        driver = self.driver
        driver.get(self.sample_product_url)
        locator = '.current-price > span:nth-child(1)'
        expected_header = 'PLN23.52'

        self.assert_element_text(driver, locator, expected_header)

