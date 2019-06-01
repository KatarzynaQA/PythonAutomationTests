import unittest
from selenium import webdriver


class MainTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe")

    def test_demo_login(self):
        driver = self.driver
        url = "https://autodemo.testoneo.com/en/"
        driver.get(url)
        title = driver.title
        print(f'aktualny tytuł strony z pierwszego testu to {title}')
        self.assertEqual('Lost Hat', title)

    def test_demo_account(self):
        driver = self.driver
        url = "https://demobank.jaktestowac.pl/konta.html"
        driver.get(url)
        title = driver.title
        print(f'aktualny tytuł strony z drugiego testu to {title}')
        self.assertEqual('Dmobank - Bankowość Internetowa - Konta', title,
                         f'Expected title differ from actual for page url: {url}')
        #ctr alt L format too long tekst

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
