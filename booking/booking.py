from selenium import webdriver
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
