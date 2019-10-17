  # CanvasScraper (Lecture Downloader) 
  [![pipeline status](https://gitlab.com/stucamp/canvasscraper/badges/master/pipeline.svg)](https://gitlab.com/stucamp/canvasscraper/commits/master)
  [![coverage report](https://gitlab.com/stucamp/canvasscraper/badges/master/coverage.svg)](https://gitlab.com/stucamp/canvasscraper/commits/master)

### Description

A simple program that facilitates the downloading of course materials hosted on Canvas Online Learning Platform.  Using Google Chrome (chromedriver) or Firefox (geckodriver), either with or without GUI, after logging-in, it will traverse your courses, finding video links and download them as videos you can watch off-line or mp3 for you to listen on the go.

### Installation

To install the library, run:

```
pip3 install canvasscraper
```

### Configuration

Then either call it in your code like so:

```python
from canvasscraper.fileops import XXXX
from canvasscraper.objects import XXXX
```

Or run it as a CLI program using (coming soon):

```bash
-b broswer
-gui is flagged will show browser as functions
-up username password
-sch school subdomain (asu by default)
```

There will options for the output directory structure, saving of URL list, potentially saving of slide, and 
maybe even page text saved to file.

This is an example of download file structure/options:
```python
root_dir
|__Courses
    | __Class1
        |__Vids
    |__Class2
        |__Vids
```

### Requirements

https://github.com/shadowmoose/pyderman

https://github.com/SeleniumHQ/selenium

https://github.com/ytdl-org/youtube-dl

### Useful Resources
