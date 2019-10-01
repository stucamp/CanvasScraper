from canvasscraper.objects.Video import Video


class Page(object):

    def __init__(self, name, url, course):
        self.name = name
        self.url = url
        self.course = course
        self.videos = []

    def __str__(self):
        return self.name

    def add_vid(self, name, url):
        self.videos.append(Video(name, url, self.name, self.course))

    def has_vids(self):
        return len(self.videos) > 0

    def print_info(self):
        print("-------------------------------------------------------------------------------------------------------")
        print(f"\tPage: {self.name} at {self.url}\n\tContains these videos:")
        print("-------------------------------------------------------------------------------------------------------")
        if len(self.videos) is 0:
            print("\t\t-=No Videos Found=-")
        else:
            for vid in self.videos:
                vid.print_info()
