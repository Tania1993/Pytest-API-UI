import configparser
import pytest
import os


class TestSeleniumMainPage:
    config = configparser.ConfigParser()
    #path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config.read('config.ini')
    link = config['URLs']['selenium_test_page']

    @pytest.mark.UI
    def test_guest_should_see_login_link(self, browser):
        browser.get(self.link)
        browser.find_element_by_css_selector('#login_link')

    @pytest.mark.UI
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(self.link)
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')