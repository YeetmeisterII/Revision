import os

from django.test import TestCase
from selenium import webdriver


class TestChrome(TestCase):
    # TODO: The starting page for all tests in this TestCase should be on a main landing page. Not the physics index or
    #  maths index pages
    @classmethod
    def setUpClass(cls):
        driver_path = f'{os.getcwd()}/study_site/selenium_drivers/chromedriver'
        cls.driver = webdriver.Chrome(driver_path)

    def test_global_link_to_maths(self):
        self.driver.get("http://localhost:8000/physics/")
        self.driver.find_element_by_link_text('Maths').click()
        self.assertEqual(self.driver.title, 'Maths Index')

    def test_global_link_to_physics(self):
        self.driver.get("http://localhost:8000/maths/")
        self.driver.find_element_by_link_text('Physics').click()
        self.assertEqual(self.driver.title, 'Physics Index')

    def test_global_link_to_computer_science(self):
        self.driver.get("http://localhost:8000/physics/")
        self.driver.find_element_by_link_text('Computer Science').click()
        self.assertEqual(self.driver.title, 'Computer Science Index')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
