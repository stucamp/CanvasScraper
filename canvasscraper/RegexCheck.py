import re


class Regex:

    # TODO: As more/varied video hosting sites are discovered, regex will need to be expanded.
    def __init__(self):
        self.url = ""
        self.regex_dict = {
            "wistia": r'https?://(?:fast\.)?wistia\.(?:net|com)/embed/(?:iframe|medias)/(?P<id>[a-z0-9]+)',
            "mslgoee": r'https?://(?:mslgoee\.)?asu\.(?:edu|com)/Mediasite/Play/*',
        }

    def check(self, url):
        self.url = url
        for vid_type, url in self.regex_dict.items():
            if re.match(url, self.url):
                return vid_type

    def is_valid(self, url):
        self.url = url
        for site, url in self.regex_dict.items():
            if re.match(url, self.url):
                print(f"Regex: Found {site} Video")
                return True
        print("Regex: No Match")
        return False


