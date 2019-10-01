class Video(object):

    def __init__(self, name, url, page, course):
        self.name = name
        self.url = url
        self.page = page
        self.course = course
        self.vid_type = ""

    def __str__(self):
        return self.name

    def print_info(self):
        print(f"\t\t{self.name} at {self.url}")

