import sys


# TODO: Needs lots of work... maybe a gui with Tkinter?  Maybe just really nice CLI
class Menu:

    def __init__(self, course_arr, driver):
        self.driver = driver
        self.courses = course_arr

    def choose_class(self):
        num = 0
        coursekey = {}

        print("=========================\n"
              "Loading Active Courses   \n"
              "=========================")
        for course in self.courses:
            num += 1
            coursekey[num] = course.name
            print(f"{num}) {course.name}")
        print(f"{num+1} All Courses")
        selection = input("Please choose a course: ")
        for numkeyed, coursekeyed in coursekey.items():
            if selection is "Q":
                print("Quitting... ")
                self.user_quit()
            if selection is 4:
                print("All Courses Selected")
                return "ALL"
            if int(selection) is numkeyed:
                print(f"{coursekeyed} selected")
                return coursekeyed

    def user_quit(self):
        self.driver.quit()
        sys.exit("User initiated Quit")