from canvasscraper.objects.Page import Page


class Course(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = {}

    def __str__(self):
        return self.name

    def add_page(self, name, url):
        self.pages[name] = Page(name, url, self.name)

    def has_pages(self):
        return len(self.pages) > 0

    def print_info(self):
        print("======================================================================================================")
        print(f"{self.name} at {self.url}\nThis course has {len(self.pages)} Pages.  They are as follows:")
        print("======================================================================================================")
        if len(self.pages) is 0:
            print("\t\t-=No Pages Found=-")
        else:
            for page in self.pages:
                self.pages[page].print_info()
