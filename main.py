import time

from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency()
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date='2024-04-02', check_out_date='2024-04-07')
    bot.select_adults(10)
    bot.click_search()
    time.sleep(5)

    input("Press Enter to exit...")


