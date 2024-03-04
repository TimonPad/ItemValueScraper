from Classes.SignInSteam import run_webdriver
from Classes.Menu import menustart
import threading

# Create an event to synchronize the threads
menu_ready = threading.Event()

if __name__ == '__main__':
    print('Initiated script from main')
    # Create two threads, one for the WebDriver and one for other code
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
#cancel moet terug naar menu gaan en quit in menu moet thread stoppen
#if statement om currencyconverter checked tijd uur en dan per uur moet doen.
#dict met timestamp key currency en value is conversie rate


