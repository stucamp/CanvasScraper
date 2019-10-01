  # CanvasScraper (Lecture Downloader) [![badge](https://action-badges.now.sh/stucamp/canvasscraper)](https://github.com/stucamp/canvasscraper/actions)

### Description

A simple program that facilitates the downloading of course materials hosted on Canvas Online Learning Platform.  Using Google Chrome (chromedriver) or Firefox (geckodriver), either with or without GUI, after logging-in, it will traverse your courses, finding video links and download them as videos you can watch off-line or mp3 for you to listen on the go.

### Installation

To install the library, run:

```
pip install canvasscraper
```

### Configuration

Then either call it in your code like so:

```python
from canvasscraper.fileops import XXXX
from canvasscraper.objects import XXXX
```

Or run it as a CLI program using (coming soon):

```bash
canvasscraper -f audio -school asu
canvasscraper -f video -school asu
```

There will options for the output directory structure, saving of URL list, potentially saving of slide, and 
maybe even page text saved to file.

This is an example of download file structure/options:
```python
blank
```

### Requirements

https://github.com/shadowmoose/pyderman

https://github.com/SeleniumHQ/selenium

https://github.com/ytdl-org/youtube-dl

### Useful Resources
