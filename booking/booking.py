import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(by=By.XPATH,
                                             value='//*[@id="b2indexPage"]/div[2]/div/div/header/nav[1]/div[2]/span[1]/button')
        currency_element.click()
        selected_currency_element = self.find_element(by=By.XPATH,
                                                      value='//*[@id="b2indexPage"]/div[19]/div/div/div/div/div[2]/div/div[3]/div/div/div/ul[1]/li[1]/button')
        selected_currency_element.click()

    def check_popup(self):
        try:
            popup = self.find_element(by=By.XPATH,
                                      value='//*[@id="b2indexPage"]/div[21]/div/div/div/div[1]/div[1]/div/button')
            popup.click()
            print('Popup dismissed')
        except:
            pass

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(by=By.XPATH, value='//*[@id=":re:"]')
        search_field.clear()
        self.check_popup()
        search_field.send_keys(place_to_go)
        search_field.click()
        time.sleep(2)
        first_result = self.find_element(by=By.XPATH, value='//*[@id="autocomplete-result-0"]')
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(by=By.CSS_SELECTOR, value=f'span[data-date="{check_in_date}"]')
        check_in_element.click()
        check_out_element = self.find_element(by=By.CSS_SELECTOR, value=f'span[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(by=By.CSS_SELECTOR, value='button[data-testid="occupancy-config"]')
        selection_element.click()
        while True:
            decrease_adult_element= self.find_element(by=By.XPATH, value='//*[@id=":rf:"]/div/div[1]/div[2]/button[1]')
            decrease_adult_element.click()
            adults_value_element = self.find_element(by=By.ID,value='group_adults')
            adults_value = adults_value_element.get_attribute('value')  #gets count for adults
            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(by=By.XPATH, value='//*[@id=":rf:"]/div/div[1]/div[2]/button[2]')

        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]')
        search_button.click()