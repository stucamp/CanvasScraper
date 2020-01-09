from __future__ import unicode_literals
import youtube_dl


class Downloader:

    @staticmethod
    def download_as_video(vid_obj, path):
        ydl_opts = {
            'outtmpl': f'{path}/{vid_obj.course} - {vid_obj.page} {vid_obj.name}',
            'preferredquality': 'bestvideo/best',
            'preferredencoding': 'mp4',
            'replace_extension': 'yes',
            'maxfilesize': '300M',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([vid_obj.url])

    # TODO: Need to sort out the audio post processing a bit.
    # @staticmethod
    # def download_as_mp3(vid_obj, path):
    #     ydl_opts = {
    #         'preferredquality': 'bestaudio/best',
    #         'maxfilesize': '300M',
    #         'postprocessors': [{
    #             'key': 'FFmpegExtractAudio',
    #             'outtmpl': f'{path}/{vid_obj.course} - {vid_obj.page} {vid_obj.name}',
    #             'preferredcodec': 'mp3',
    #             'preferredquality': '128',
    #         }],
    #     }
    #     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #         ydl.download([vid_obj.url])
