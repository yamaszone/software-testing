import unittest
from selenium import webdriver

class TestSeleniumUsingPhantomJS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def test_page_title_exists(self):
        self.driver.get('http://stackoverflow.com/')

        #f = open('out.txt', 'w')
        #f.write(self.driver.current_url)
        #f.close()
        assert "Stack Overflow" in self.driver.title

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
