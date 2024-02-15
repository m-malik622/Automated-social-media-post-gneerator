import os
from pytube import YouTube

def Download_Youtube_Vid(link: str, video_output_path: str):
    """
    Download a YouTube video given its link and save it to the specified output path.

    Args:
        link (str): The YouTube video link.
        video_output_path (str): The path where the downloaded video will be saved.
    """
    try:
        video = YouTube(link)
        video = video.streams.get_highest_resolution()
        downloaded_vid_path = video.download(output_path=video_output_path)
        return downloaded_vid_path
    except:
        print("En error has occured while downloading the video %s" % link)
        return 0    