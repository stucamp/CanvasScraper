import sys
import getpass

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


class InvalidBrowserException(Exception):
    pass


def install_browser_driver(args):
    if args.browser.lower() == 'firefox':
        path = dr.install(browser=dr.firefox, file_directory='./lib/', verbose=True, chmod=True, overwrite=False,
                          version=None, filename=None, return_info=False)
    elif args.browser.lower() == 'chrome':
        path = dr.install(browser=dr.chrome, file_directory='./lib/', verbose=True, chmod=True, overwrite=False,
                          version=None, filename=None, return_info=False)
    else:
        raise InvalidBrowserException(f"{args.browser} is not an expected browser")
    return path


def set_driver(path, args):
    if args.browser.lower() == 'chrome':
        try:
            print("Chrome Driver")
            option = CHop()
            option.add_argument(('--none', '--headless')[not args.use_gui])
            return CHdr.WebDriver(executable_path=path, options=option)
        except SessionNotCreatedException:
            _exception_print('Chrome', 'ChromeDriver', 'https://chromedriver.chromium.org/downloads')
    elif args.browser.lower() == 'firefox':
        try:
            print("Gecko Driver")
            option = FFop()
            option.add_argument(('-none', '-headless')[not args.use_gui])
            return FFdr.WebDriver(executable_path=path, options=option)
        except SessionNotCreatedException:
            _exception_print('Firefox', 'GeckoDriver', 'https://github.com/mozilla/geckodriver/releases')
    else:
        raise InvalidBrowserException("No Appropriate webdriver found!")


def set_format(args):
    if args.format.lower() == 'mp4':
        print(f"Video Selected")
    elif args.format.lower() == 'mp3':
        print(f"Audio Only Selected")



def _exception_print(browser, driver, link):
    print(f"============================================================================\n"
          f"{browser} Version does not match driver version.  Please ensure they match. \n"
          f"For now just ensure that the right {driver} version is install in the       \n"
          f"./CanvasScraper/canvasscraper/lib/{driver}_executable                       \n"
          f"{browser} Driver Download Link: {link}                                      \n"
          f"============================================================================\n")


def login(driver, args):
    base_url = "https://" + args.school + ".instructure.com"
    url = base_url + "/login"

    driver.get(url)
    WebDriverWait(driver, 10).until(EC.title_contains("ASURITE Sign-In"))

    username, password = args.username_password[0], args.username_password[1]
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_class_name('submit').click()

    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))

    print(f"================================\n"
          f"Printing to confirm function.   \n"
          f"================================\n"
          f"Title:{driver.title}   \n"
          f"URL: {driver.current_url}")

    return base_url


def _test_link_scraper(url, driver):

    course_arr = []

    link_scraper = LinkScraper(url, driver)

    print("\nTesting Class Finder\n")

    link_scraper.get_class_list()

    print("\nTesting Page Finder\n")

    link_scraper.get_all_pages()

    print("\nTesting Video Link Finder\n")

    link_scraper.get_all_vids()

    print("\nTesting Return of Objects\n")
    for course in link_scraper.return_data():
        course_arr.append(course)
    for course in course_arr:
        course.print_info()

    return course_arr


def _test_dir_maker(course_arr, args):
    print("\nTesting DirMaker\n")
    saver = DirMaker(None, args.format)
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
def main(args):
    driver_path = install_browser_driver(args)
    print(driver_path)
    driver = set_driver(driver_path, args)
    base_url = login(driver, args)
    print(f"Base URL Recorded as: {base_url}")
    courses = _test_link_scraper(base_url, driver)
    _test_dir_maker(courses, args)
    _test_URL_logger(courses)
    _user_quit(driver)
