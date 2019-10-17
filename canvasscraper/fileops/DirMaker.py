import os
from canvasscraper.fileops.Downloader import Downloader


class DirMaker:

    def __init__(self, formattype, root_dir):
        self.root_dir = root_dir
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

    def save_course(self, course_obj):
        self.__make_base_dir()
        if course_obj.has_pages:
            print(f"{course_obj.name} has pages, making Course directory")
            self.__make_course_dir(course_obj.name)
            for name, obj in course_obj.pages.items():
                if obj.has_vids():
                    print(f"\tPage: {name} has links, downloading content...")
                    for vid in obj.videos:
                        # print(f"D/L {vid.course} video on {vid.page}:\n{vid.name} at {vid.url}")
                        if self.formattype == 'mp4':
                            print(f"\t\tDownloading Video from: {vid.url}")
                            Downloader.download_as_video(vid, self.new_base_dir)
                        elif self.formattype == 'mp3':
                            print(f"\t\tDownloading Audio from: {vid.url}")
                            Downloader.download_as_mp3(vid, self.new_base_dir)
                else:
                    print(f"\tPage: {name} has no videos, nothing to save!")
        else:
            print(f"{course_obj.name} has no pages, nothing to save!")

    def save_all(self, course_arr):

        for course in course_arr:
            self.save_course(course)




