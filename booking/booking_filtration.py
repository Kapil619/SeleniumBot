# For Applying filtrations
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        try:
            
            star_filtration_box = self.driver.find_element(by=By.ID, value='filter_group_popular_:rj:')
            star_child_elements = star_filtration_box.find_elements(by=By.CSS_SELECTOR, value='*')

            for star_value in star_values:
                for star_element in star_child_elements:
                    if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                        star_element.click()
                        # print('Filters applied')
        except Exception as e:
            print('Error in applying filtration: ', e)

    def sort_price_lowest_first(self):
        try:
            element = self.driver.find_element(by=By.CSS_SELECTOR, value='button[data-testid="sorters-dropdown-trigger"]')
            element.click()
            btn = self.driver.find_element(by=By.CSS_SELECTOR, value='button[data-id="price"]')
            btn.click()
        except Exception as e:
            print('Error in sorting: ', e)


