# Youtube Video Downloader
# This is a little training project
# From "Internet Made Coder" on Youtube
# sudo pip3 install pytube
from pytube import YouTube
from sys import argv


def start():
    e_link = argv[1]
    e_yt = YouTube(e_link)
    print("Titre : ", e_yt.title)
    print("Vues :", e_yt.views)

    e_yd = e_yt.streams.get_highest_resolution()
    e_yd.download("./videos_downloaded")


if __name__ == '__main__':
    start()
