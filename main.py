import time
from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        # bot.change_currency()
        bot.check_popup()
        bot.select_place_to_go(input('Where are you going? '))
        bot.select_dates(check_in_date=input('Where is check-in-date? (yyyy-mm-dd): '), check_out_date=input('Where is check-out-date? (yyyy-mm-dd): '))
        bot.select_adults(int(input('How many people? ')))
        bot.click_search()
        if bot.check_popup():
            pass
        bot.apply_filtration()
        bot.report_results()
        time.sleep(5)
        input("Press Enter to exit...")
except Exception as e:
    print('Theres is a problem with the code: ', e)


