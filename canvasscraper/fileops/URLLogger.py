import os


class URLLogger:

    def __init__(self, course_arr, path=None):
        self.courses = course_arr
        self.vid_list = {}
        self.vid_arr = []
        self.cwd = os.getcwd()
        if path is None:
            self.path = os.getcwd()
        else:
            self.path = path

    def write_URLs_to_file(self):
        writer = open(f"{self.path}/videoList.txt", 'w+')
        for course in self.courses:
            for name, page_obj in course.pages.items():
                for vid in page_obj.videos:
                    writer.write(f"{vid.course} {vid.page} {vid.name} - {vid.url}\n")

        writer.close()
        os.chdir(self.cwd)

# TODO: Needs testing/ironing out
    def load_file_to_dict(self):
        with open(f"{self.path}/videoList.txt", 'r') as reader:
            for cnt, line in enumerate(reader):
                lines = line.split(" - ")
                self.vid_list[lines[0]] = lines[1]
        reader.close()
        return self.vid_list

# TODO: Needs testings/ironing out
    def load_file_to_arr(self):
        with open(f"{self.path}/videoList.txt", 'r') as reader:
            for line in reader:
                lines = line.split(" - ")
                self.vid_arr.append(lines[1])
        reader.close()
        return self.vid_list
