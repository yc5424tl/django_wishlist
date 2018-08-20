from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TitleTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_shown_on_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Travel Wishlist' in self.browser.title


class PageViewTests(LiveServerTestCase):

    fixtures = ['test_places']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_get_home_page_list_of_places(self):
        self.browser.get(self.live_server_url)
        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source
        assert 'San Fransisco' not in self.browser.page_source
        assert 'Moab' not in self.browser.page_source

    def test_get_list_of_visited_places(self):
        self.browser.get(self.live_server_url + '/visited')
        assert 'Wishlist' in self.browser.title
        assert 'Tokyo' not in self.browser.page_source
        assert 'New York' not in self.browser.page_source
        assert 'Moab' in self.browser.page_source


# noinspection PyUnusedLocal
class FunctionalityTests(LiveServerTestCase):

    fixtures = ['test_places']

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_add_new_place(self):
        self.browser.get(self.live_server_url)
        input_name = self.browser.find_element_by_id('id_name')
        input_name.send_keys('Denver')
        add_button = self.browser.find_element_by_id('add-new-place')
        add_button.click()
        wait_for_denver = self.browser.find_element_by_id('place-name-5')
        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source
        assert 'Denver' in self.browser.page_source

    def test_mark_place_as_visited(self):
        self.browser.get(self.live_server_url)
        visited_button = self.browser.find_element_by_id('mark-visited-2')
        ny_gone = self.browser.find_element_by_id('place-name-2')
        visited_button.click()
        wait = WebDriverWait(self.browser, 3)
        ny_has_gone = wait.until(EC.invisibility_of_element_located((By.ID, 'place-name-2')))
        assert 'Tokyo' in self.browser.page_source
        assert 'New York' not in self.browser.page_source
        self.browser.get(self.live_server_url + '/visited')
        assert 'New York' in self.browser.page_source
        assert 'San Fransisco' in self.browser.page_source
        assert 'Moab' in self.browser.page_source
