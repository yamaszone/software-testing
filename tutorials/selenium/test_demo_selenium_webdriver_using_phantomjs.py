import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

class TestSeleniumUsingPhantomJS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_page_title_exists(self):
        self.driver.get('http://stackoverflow.com/')

        #f = open('out.txt', 'w')
        #f.write(self.driver.current_url)
        #f.close()
        assert "Stack Overflowing" in self.driver.title

    def test_google_search_works(self):
        # go to the google home page
        self.driver.get("http://www.google.com")

        # find the element that's name attribute is q (the google search box)
        inputElement = self.driver.find_element_by_name("q")

        # type in the search
        inputElement.send_keys("Mazedur Rahman")

        # submit the form (although google automatically searches now without submitting)
        inputElement.submit()

        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(self.driver, 10).until(EC.title_contains("Mazedur Rahman"))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
