from canvasscraper.objects.Course import Course
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from canvasscraper.RegexCheck import Regex


# TODO: Will probably want to break this down further, permitting scrap of individual courses/pages (of course)
# TODO: you can current just provide the functions with a single index array.
class LinkScraper:

    def __init__(self, base_url, driver):
        self.base_url = base_url
        self.driver = driver
        self.courses = []
        self.has_class_list = False

    def get_class_list(self):
        url = self.base_url + "/courses"
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.title_contains("Courses"))
        print(f"=========================\n"
              f"Retrieving Active Courses\n"
              f"=========================")
        for course in self.driver.find_elements_by_tag_name('a'):
            self._if_class_get_class(course, self.courses)
        self.has_class_list = True

    @staticmethod
    def _if_class_get_class(link, arr):
        if "/courses/" in link.get_attribute('href'):
            print(f"Found class: {link.get_attribute('title')[0:7]}")
            arr.append(Course(link.get_attribute('title')[0:7], link.get_attribute('href')))

    def get_all_pages(self):
        for course in self.courses:
            self.get_page_list(course)

    def get_page_list(self, course_obj):
        if course_obj.has_pages():
            print(f"=============================================\n"
                  f"Retrieving Course Pages for: " + course_obj.name + "  \n"
                  f"=============================================")
            url = course_obj.url + "/modules"
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(EC.title_contains(course_obj.name))
            for page in self.driver.find_elements_by_tag_name('a'):
                self._if_page_get_page(page, course_obj)
        else:
            print(f"=============================================\n"
                  f"No Course Pages for: " + course_obj.name + "  \n"
                  f"=============================================")

    @staticmethod
    def _if_page_get_page(page, course_obj):
        if "for-nvda" in page.get_attribute('class'):
            if page.get_attribute('aria-label') is not "":
                print(f"Found Page at: {page.get_attribute('href')}")
                course_obj.add_page(page.get_attribute('aria-label'), page.get_attribute('href'))

    def get_all_vids(self):
        for course in self.courses:
            self.get_vid_list(course)

    def get_vid_list(self, course_obj):
        regex_checker = Regex()
        print(f"================================\n"
              f"Searching {course_obj.name} Pages for Videos \n"
              f"================================")
        for name, obj in course_obj.pages.items():
            count = 0
            print(f'___________________________\n'
                  f'Currently Checking: {obj.course} {name}')
            self.driver.get(obj.url)
            iframes = self.driver.find_elements_by_xpath("//iframe")
            for frame in iframes:
                if regex_checker.is_valid(frame.get_attribute('src')):
                    count += 1
                    print(f"Found Video at: {frame.get_attribute('src')}")
                    obj.add_vid(count, frame.get_attribute('src'))

    def return_data(self):
        return self.courses

