import unittest
from selenium import webdriver


class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe")


    def test_demo_login(self):
        driver = self.driver
        driver.get("https://autodemo.testoneo.com/en/")
        title = driver.title
        print(title)
        assert 'Lost Hat' == title


    def test_demo_account(self):
        driver = self.driver
        driver.get("https://demobank.jaktestowac.pl/konta.html")
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Konta' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


