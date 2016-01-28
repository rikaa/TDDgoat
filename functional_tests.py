from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith tries a new to-do web app she heard about
        # She visits the website
        self.browser.get('http://localhost:8000')

        # and indeed, the site exists
        self.assertIn('To-do', self.browser.title) 
        self.fail('Finsih the test!')

        # She inserts her first to-do item and press enter

        # the item is added to her list

        # entering a second item extends the list

        # the next day, she checks the website again wondering
        # whether her list was stored. Happily, the list is still 
        # available

if __name__ == '__main__':  #7
    unittest.main()  #8
