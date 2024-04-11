import time
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        # bot.change_currency()
        bot.check_popup()
        bot.select_place_to_go('New York')
        bot.select_dates(check_in_date='2024-04-20', check_out_date='2024-04-23')
        bot.select_adults(2)
        bot.click_search()
        if bot.check_popup():
            pass
        bot.apply_filtration()
        bot.report_results()
        time.sleep(5)
        input("Press Enter to exit...")
except Exception as e:
    print('Theres is a problem with the code: ', e)


