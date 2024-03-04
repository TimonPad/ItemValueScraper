import threading
from Classes.SignInSteam import run_webdriver
from Classes.Menu import menustart
from Classes.stop_threads import stop_threads

menu_ready = threading.Event()


if __name__ == '__main__':
    print('Initiated script from main')
    #Create two threads, one for the WebDriver and one for other code
    webdriver_thread = threading.Thread(target=run_webdriver, args=(menu_ready,))
    menu_thread = threading.Thread(target=menustart, args=(menu_ready,))
    # Start both threads
    webdriver_thread.start()
    menu_thread.start()
    # Wait for both threads to finish
    webdriver_thread.join()
    menu_thread.join()
    print("Both threads have finished.")

# to do list
#quit in menu has to stop thread
#addline in menu should also get rest of items and not only goods_id -> buffpricesmanger -> def linepricespull()
#make an if float empty then input is "nan", then skip at BuffPricespull then skip rest. also implement at update selection
#if statement for currencyconverter checked time hour and then make it do automatically every hour
#dict with timestamp key currency and value in conversion rate


