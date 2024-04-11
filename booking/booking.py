import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\chromedriver.exe", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(by=By.XPATH,
                                             value='//*[@id="b2searchresultsPage"]/div[3]/div/div/header/nav[1]/div[2]/span[1]/button')
        currency_element.click()
        selected_currency_element = self.find_element(by=By.XPATH,
                                                      value='//*[@id="b2indexPage"]/div[19]/div/div/div/div/div[2]/div/div[3]/div/div/div/ul[1]/li[1]/button')
        selected_currency_element.click()

    def check_popup(self):
        try:
            # print('Entered popup function')
            # popup = self.find_element(by=By.XPATH,
            #                           value='//*[@id="b2indexPage"]/div[21]/div/div/div/div[1]/div[1]/div/button')
            popup = self.find_element(by=By.CSS_SELECTOR, value='button[aria-label="Dismiss sign-in info."]')
            # print('Located element')

            popup.click()
            # print('Popup dismissed')
            return True
        except:
            return False
            pass

    def select_place_to_go(self, place_to_go):
        try:
            # print('Entered select_place_to_go function')
            search_field = self.find_element(by=By.XPATH, value='//*[@id=":re:"]')
            # print('Located search field')
            search_field.clear()
            search_field.send_keys(place_to_go)
            search_field.click()
            # print('Clicked search field')
            time.sleep(2)
            first_result = self.find_element(by=By.XPATH, value='//*[@id="autocomplete-result-0"]')
            first_result.click()
        except Exception as e:
            print('Error in Select places: ', e)

    def select_dates(self, check_in_date, check_out_date):
        try:
            check_in_element = self.find_element(by=By.CSS_SELECTOR, value=f'span[data-date="{check_in_date}"]')
            check_in_element.click()
            check_out_element = self.find_element(by=By.CSS_SELECTOR, value=f'span[data-date="{check_out_date}"]')
            check_out_element.click()
        except Exception as e:
            print('Error in selecting dates: ', e)

    def select_adults(self, count=1):
        try:
            selection_element = self.find_element(by=By.CSS_SELECTOR, value='button[data-testid="occupancy-config"]')
            selection_element.click()
            while True:
                decrease_adult_element = self.find_element(by=By.XPATH,
                                                           value='//*[@id=":rf:"]/div/div[1]/div[2]/button[1]')
                decrease_adult_element.click()
                adults_value_element = self.find_element(by=By.ID, value='group_adults')
                adults_value = adults_value_element.get_attribute('value')  # gets count for adults
                if int(adults_value) == 1:
                    break

            increase_button_element = self.find_element(by=By.XPATH,
                                                        value='//*[@id=":rf:"]/div/div[1]/div[2]/button[2]')
            for _ in range(count - 1):
                increase_button_element.click()
        except Exception as e:
            print('Error in selecting adults: ', e)

    def click_search(self):
        try:

            search_button = self.find_element(by=By.CSS_SELECTOR, value='button[type="submit"]')
            search_button.click()
        except Exception as e:
            print('Error in clicking search: ', e)

    def apply_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3, 4, 5)
        filtration.sort_price_lowest_first()

    def report_results(self):
        hotels = self.find_element(by=By.CLASS_NAME, value='d4924c9e74').find_elements(by=By.CSS_SELECTOR,
                                                                                       value='div[data-testid="property-card"]')
        # print(len(hotels))
        hotel_data = []
        for hotel in hotels:
            name = hotel.find_element(by=By.CSS_SELECTOR, value='div[data-testid="title"]').get_attribute(
                'innerHTML').strip()
            # print(name)
            hotel_price = hotel.find_element(by=By.CSS_SELECTOR,
                                             value='span[data-testid="price-and-discounted-price"]').get_attribute(
                'innerHTML').strip()
            hotel_price = hotel_price.replace('₹&nbsp;', '₹')  # remove '₹&nbsp;'
            # hotel_score = hotel.find_element(by=By.CLASS_NAME, value='ac4a7896c7 ').get_attribute('innerHTML').strip()
            # hotel_score = hotel_score.replace('Scored ', '')  # remove 'Scored '
            hotel_data.append((name, hotel_price))
        table = PrettyTable(field_names=['Hotel Name', 'Hotel Price'])
        table.add_rows(hotel_data)
        print(table)
        # return hotel_data
