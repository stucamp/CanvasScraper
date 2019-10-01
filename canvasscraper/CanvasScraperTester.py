import sys
import pyderman as dr
from selenium.webdriver.chrome import webdriver as CHdr
from selenium.webdriver.firefox import webdriver as FFdr
from selenium.webdriver.chrome.options import Options as CHop
from selenium.webdriver.firefox.options import Options as FFop

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import SessionNotCreatedException

from canvasscraper.fileops.LinkScraper import LinkScraper
from canvasscraper.fileops.DirMaker import DirMaker
from canvasscraper.fileops.URLLogger import URLLogger


AUTHOR = "stucampbell.git@gmail.com"


def _browser_select():

    browsers = {'1': 'Chrome',
                '2': 'Firefox',
                '3': 'Other',
                'Q': 'Quit',
                }

    print("=====================================================\n"
          "Please select your system Browser:                   \n"
          "=====================================================\n")
    for key, choice in browsers.items():
        print(f"{key}) {choice}")
    pick_em = input("Enter wisely: ")

    if pick_em is 'Q':
        sys.exit("User elected to quit")
    elif pick_em is '3':
        _get_out()
    elif pick_em is '2':
        path = dr.install(browser=dr.firefox, file_directory='./lib/', verbose=True, chmod=True, overwrite=False,
                          version=None, filename=None, return_info=False)
        return path, pick_em
    elif pick_em is '1':
        path = dr.install(browser=dr.chrome, file_directory='./lib/', verbose=True, chmod=True, overwrite=False,
                          version=None, filename=None, return_info=False)
        return path, pick_em
    else:
        _im_out()


def _run_headless():
    gui = input(f"Do you want to run the browser with GUI? [y/N]")
    if gui is "" or 'n' or "N":
        return True
    elif gui is "y" or "Y":
        return False
    else:
        _im_out()


def _get_out():
    print("You're a Software Engineering student...\n"
          "You should know Chrome or FireFox is the only acceptable response.")
    sys.exit("Program refuses to work for a user with such poor judgement.  Exiting...")


def _im_out():
    print("No valid selection")
    sys.exit("User failed a simple 'Pick-One' scenario... Yikes... I'm out.  Exiting...")


def _set_driver(path, choice):
    if choice is '1':
        try:
            print("Chrome Driver")
            option = CHop()
            option.add_argument(('--none', '--headless')[_run_headless()])
            return CHdr.WebDriver(executable_path=path, options=option)
        except SessionNotCreatedException:
            _exception_print('Chrome', 'ChromeDriver', 'https://chromedriver.chromium.org/downloads')
    elif choice is '2':
        try:
            print("Gecko Driver")
            option = FFop()
            option.add_argument(('-none', '-headless')[_run_headless()])
            return FFdr.WebDriver(executable_path=path, options=option)
        except SessionNotCreatedException:
            _exception_print('Firefox', 'GeckoDriver', 'https://github.com/mozilla/geckodriver/releases')
    else:
        print("====================================\n"
              "No Appropriate webdriver found!!!!!!\n"
              "====================================\n")
        sys.exit(1)


def _exception_print(browser, driver, link):
    print(f"============================================================================\n"
          f"{browser} Version does not match driver version.  Please ensure they match. \n"
          f"For now just ensure that the right {driver} version is install in the       \n"
          f"./CanvasScraper/canvasscraper/lib/{driver}_executable                       \n"
          f"{browser} Driver Download Link: {link}                                      \n"
          f"============================================================================\n")


# TODO: Maybe obscure the log-in details... all just plain text at the moment
def _login(driver):

    un = input("Enter username: ")
    pw = input("Enter password: ")
    sub = input("Enter school subdomain, [asu] by default: ")

    if sub == "":
        sub = 'asu'

    base_url = "https://" + sub + ".instructure.com"
    url = base_url + "/login"

    driver.get(url)
    WebDriverWait(driver, 10).until(EC.title_contains("ASURITE Sign-In"))

    driver.find_element_by_id('username').send_keys(un)
    driver.find_element_by_id('password').send_keys(pw)
    driver.find_element_by_class_name('submit').click()

    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

    print(f"================================\n"
          f"Printing to confirm function.   \n"
          f"================================\n"
          f"Title:{driver.title}   \n"
          f"URL: {driver.current_url}")

    return base_url


def _test_link_scraper(driver, url):

    course_arr = []

    link_scraper = LinkScraper(url, driver)

    print("\nTesting Class Finder\n")
    if not link_scraper.has_class_list:
        link_scraper.get_class_list()

    print("\nTesting Page Finder\n")
    if link_scraper.has_class_list and not link_scraper.has_page_list:
        link_scraper.get_page_list()

    print("\nTesting Video Link Finder\n")
    if link_scraper.has_class_list and link_scraper.has_page_list and not link_scraper.has_vid_list:
        link_scraper.get_vid_list()

    print("\nTesting Return of Objects\n")
    for course in link_scraper.return_data():
        course_arr.append(course)
    for course in course_arr:
        course.print_info()


def _test_dir_maker(course_arr):
    print("\nTesting DirMaker\n")
    saver = DirMaker()
    saver.save_all(course_arr)


def _test_URL_logger(course_arr):
    print("\nTesting URLLogger\n")
    logger = URLLogger(course_arr)
    logger.write_URLs_to_file()


def _user_quit(driver):
    print("Quitting...")
    driver.quit()
    sys.exit("User initiated Quit")


# TODO: Finish user interface options to include loading an existing file, selection of classes to download, etc.
def main():
    # print("Functions currently commented out for testing purposes.")
    driver_path, browser = _browser_select()
    print(driver_path, browser)
    driver = _set_driver(driver_path, browser)
    base_url = _login(driver)
    print(f"Base URL Recorded as: {base_url}")
    # _test_link_scraper()
    # _test_dir_maker()
    # _test_URL_logger()
    _user_quit(driver)


if __name__ == '__main__':
    main()
