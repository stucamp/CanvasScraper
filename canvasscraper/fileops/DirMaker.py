import os
from canvasscraper.fileops.Downloader import Downloader


class DirMaker:

    def __init__(self, root_dir=None, formattype=None):
        if root_dir is None:
            self.root_dir = os.getcwd()
        else:
            self.root_dir = root_dir
        if formattype is None:
            self.formattype = 'mp4'
        else:
            self.formattype = formattype
        self.new_base_dir = self.root_dir + "/Courses"

    def __make_base_dir(self):
        try:
            os.mkdir(self.new_base_dir)
        except FileExistsError:
            print("Base Folder Already Exists!")

    def __make_course_dir(self, course_name):
        try:
            os.makedirs(self.new_base_dir + f"/{course_name}")
        except FileExistsError:
            print("Folder Already Exists for this Course!")

    def __make_page_dir(self, course_name, page_name):
        try:
            os.chdir(self.new_base_dir + f"/{course_name}")
        except FileNotFoundError:
            self.__make_course_dir(course_name)
            print("Creating Course Folder, First")
        try:
            os.mkdir(self.new_base_dir + f"/{course_name}/{page_name}")
        except FileExistsError:
            print("Folder Already Exists for this Page!")

    def save_course(self, course_obj):
        self.__make_base_dir()
        if course_obj.has_pages:
            print(f"{course_obj.name} has pages, making Course directory")
            self.__make_course_dir(course_obj.name)
            for name, obj in course_obj.pages.items():
                if obj.has_vids():
                    print(f"Page: {name} has links, downloading content...")
                    for vid in obj.videos:
                        # print(f"Pretending to D/L {vid.course} video on {vid.page}:\n{vid.name} at {vid.url}")
                        if self.formattype is "mp4":
                            Downloader.download_as_video(vid, os.getcwd())
                        elif self.formattype is "mp3":
                            Downloader.download_as_mp3(vid, os.getcwd())
                        # download_function_not_yet_made(vid.name, vid.url)
        os.chdir(self.root_dir)
        #         else:
        #             print(f"Page: {name} has no videos, nothing to save!")
        # else:
        #     print(f"{course_obj.name} has no pages, nothing to save!")

    def save_all(self, course_arr):

        for course in course_arr:
            self.save_course(course)




