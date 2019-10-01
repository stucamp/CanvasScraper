from canvasscraper.fileops.LinkScraper import LinkScraper as LS
import sys


class NavTool(object):

    def __init__(self, base_url, driver):
        self.scraper = LS(base_url, driver)

# Helper functions to ensure appropriate selections are made by user.  Interface - ish
    def _for_what_course(self, operation):
        count = 0
        print(f"================================================\n"
              f"Selected which Course you'd like to {operation} \n"
              f"=================================================")
        print(f"{count}) All Courses")
        for course in self.scraper.courses:
            count += 1
            print(f"{count}) {course.name}")
        print(f"================================================")
        return int(input("Enter Selection: "))

    def _plz_get_courses(self):
        print(f"No Course list found!  Get Course list first? [Y/n]")
        choice = input()
        if choice is 'y' or 'Y' or '':
            self.get_courses()
        else:
            sys.exit("User has elected to exit, rather than make a decent decision.")

    def _plz_get_pages(self):
        print(f"No Page list found!  Get Page list first? [Y/n]")
        choice = input()
        if choice is 'y' or 'Y' or '':
            self.get_pages()
        else:
            sys.exit("User has elected to exit, rather than make a decent decision.")

    def _plz_make_good_choice(self):
        print(f"Improper Selection of Course!  Choose again? [Y/n]")
        choice = input()
        if choice is 'y' or 'Y' or '':
            self.get_courses()
        else:
            sys.exit("User has elected to exit, rather than make a decent decision.")

# Function to retrieve list of courses currently enrolled in.
    def get_courses(self):
        if not self.scraper.has_class_list:
            self.scraper.get_class_list()
        else:
            print("Already have a list of courses, search again? [y/N]")
            choice = input()
            if choice is 'y' or 'Y':
                self.scraper.has_class_list = False
                self.scraper.get_class_list()
            else:
                sys.exit("User has elected to exit, rather than make a decent decision.")

# Functions to determine how many courses retrieving pages for.
    def get_pages(self):
        choice = self._for_what_course('get pages lists?')
        if self._is_ready_for_pages():
            self._go_for_pages(choice)

    def _get_all_pages(self):
        self.scraper.get_all_pages()

    def _get_one_pages(self, choice):
        self.scraper.get_page_list(self.scraper.courses[choice-1])

    def _go_for_pages(self, choice):
        if self._is_valid_course(choice):
            if choice is '0':
                self._get_all_pages()
            elif choice in range(1, len(self.scraper.courses)):
                self._get_one_pages(choice)

# Functions to determine how many courses retrieving videos for.
    def get_vids(self):
        choice = self._for_what_course('get video links?')
        if self._is_ready_for_pages() and self._is_ready_for_vids(choice):
            self._go_for_vids(choice)

    def _get_all_vids(self):
        self.scraper.get_all_pages()

    def _get_one_vids(self, choice):
        self.scraper.get_page_list(self.scraper.courses[choice-1])

    def _go_for_vids(self, choice):
        if self._is_valid_course(choice):
            if choice is '0':
                self._get_all_vids()
            elif choice in range(1, len(self.scraper.courses)):
                self._get_one_vids(choice)

# Logic to test if ready for certain tasks
    def _is_valid_course(self, choice):
        if choice in range(len(self.scraper.courses)):
            return True
        else:
            self._plz_make_good_choice()
            self._is_valid_course(choice)

    def _is_ready_for_pages(self):
        if self.scraper.has_class_list:
            return True
        else:
            self._plz_get_courses()
            self._is_ready_for_pages()

    def _is_ready_for_vids(self, choice):
        if self.scraper.courses[choice-1].has_pages():
            return True
        else:
            self._plz_get_pages()
            self._is_ready_for_vids(choice)
