from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.assertIn('To-Do', self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # There is an input field asking for a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        # She inserts her first to-do item and press enter
        inputbox.send_keys('buy milk')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        
        # she enters a second itom
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy more milk')
        inputbox.send_keys(Keys.ENTER)



        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: buy milk', [row.text for row in rows])
        self.assertIn('2: buy more milk', [row.text for row in rows])
        # entering a second item extends the list

        # the next day, she checks the website again wondering
        # whether her list was stored. Happily, the list is still 
        # available
        self.fail('Finsih the test!')

if __name__ == '__main__':  #7
    unittest.main()  #8
