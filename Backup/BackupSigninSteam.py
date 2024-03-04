from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

global driver
global wait
# Create a flag to control whether the WebDriver should be closed
close_browser = False


def run_webdriver(menu_ready):
    global wait
    global close_browser
    global driver
    profile_path = r"C:\Users\Timon\AppData\Local\Google\Chrome\User Data\Default\Network"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--user-data-dir={profile_path}")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')  # May be necessary in some cases

    #driver_path = "D:\Backup\Cs2\Python scripts trading\My project\seleniumpython\venv\Lib\site-packages\seleniumbase\drivers\chromedriver.exe"
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 60)
    driver.get("https://buff.163.com/")
    startupsigninsteam()
    # Wait for the menu thread to signal that it's ready
    menu_ready.wait()


# Function to close the WebDriver
def close_webdriver():
    driver.quit()


def startupsigninsteam():
    def wait_for_element_clickable(xpath, timeout=50):
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
    login_button = wait_for_element_clickable("//a[@href='javascript:void(0)' and contains(@onclick, 'loginModule.showLogin()')]")
    login_button.click()
    steam_login = wait_for_element_clickable("//p [@id='j_login_other']")
    steam_login.click()
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    windows = driver.window_handles
    # Switch to the Steam OpenID login pop-up window
    driver.switch_to.window(windows[1])
    wait.until(EC.visibility_of_element_located((By.ID, "imageLogin")))
    steam_login2 = driver.find_element(By.ID,"imageLogin")
    steam_login2.click()
    driver.switch_to.window(windows[0])
    #wait till logged in on buff by verifying username on top
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='navbar-user-name']")))
    print("Signed in Successfully!")


def floatpuller(goods_id, min_float, max_float):
    driver.get(
        f"https://buff.163.com/goods/{goods_id}?from=market#tab=selling&min_paintwear={min_float}&max_paintwear={max_float}&page_num=1")
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div[1]/div[2]/div[1]/h1")))
    print(goods_id,min_float, max_float)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='market-selling-list']/tbody")))
    parent_element = driver.find_element(By.XPATH, "//*[@id='market-selling-list']/tbody")
    tr_elements = parent_element.find_elements(By.TAG_NAME, "tr")
    second_tr_id = tr_elements[1].get_attribute("id")
    try:
        element1 = driver.find_element(By.XPATH, f"//*[@id='{second_tr_id}']/td[5]/div[1]/strong")
        print("Element found: ", element1.text)
        extracted_value = re.search(r'¥ (\d+)', element1.text).group(1)
        print(f"Extracted numbers for {goods_id} with float {min_float} and {max_float}:", extracted_value)
        if extracted_value is not None:
            return extracted_value
        else:
            return float('nan')
    except NoSuchElementException:
        print("Element not found")
        return float('nan')


    #Make another same version for when adding line to table in menu so it takes just that one through same steps
