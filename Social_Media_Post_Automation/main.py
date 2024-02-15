import os #for enviornment variables if you would like to have one for the api_key
from Search_For_Youtube_Video import *
from Download_Youtube_Vid import *
from Overlap_Videos import *


def Social_Media_Post_Automation(api_key: str, top_vid_query_terms: list[str], num_of_top_vids: int, bottom_vid_query_terms: list[str], num_of_bottom_vids: int, top_vid_download_destination: str, bottom_vid_download_destination: str, result_vid_path:str, start_time:int, end_time:int, have_top_vid_stretched:bool):
     """
    Automates the process of creating social media posts by overlaying top and bottom videos.

    Args:
        api_key (str): Your API key for YouTube Data API v3. Create a free one at https://console.cloud.google.com/apis/library/youtube.googleapis.com?project=singular-antler-412916
        top_vid_query_terms (list[str]): List of search terms to find top videos.
        num_of_top_vids (int): Number of top videos to download.
        bottom_vid_query_terms (list[str]): List of search terms to find bottom videos.
        num_of_bottom_vids (int): Number of bottom videos to download.
        top_vid_download_destination (str): Path to download top videos.
        bottom_vid_download_destination (str): Path to download bottom videos.
        result_vid_path (str): Path to save the resulting video.
        start_time (int): Start time (in seconds) of both clips.
        end_time (int): End time (in seconds) of both clips.
        have_top_vid_stretched (bool): Whether to stretch the top video to takeup more space or have it appear smaller with a truer aspect ratio.
    Note:
        - The function is not fully implemented and requires additional functionality for accessing social media platforms.
        - It currently handles downloading top and bottom videos and overlaying them based on specified parameters.
    """   
    top_video_links = Search_For_Youtube_Video(api_key, top_vid_query_terms, num_of_top_vids)
    for top_video_link in top_video_links:
        top_vid_path = Download_Youtube_Vid(top_video_link, top_vid_download_destination)
    print("the top video has been succesfully downloaded")

    bottom_video_links = Search_For_Youtube_Video(api_key, bottom_vid_query_terms, num_of_bottom_vids)
    for bottom_video_link in bottom_video_links:
        bottom_vid_path = Download_Youtube_Vid(bottom_video_link, bottom_vid_download_destination)
    print("the bottom video has been succesfully downloaded")

    Overlap_Videos(top_vid_path, bottom_vid_path, result_vid_path, start_time, end_time, have_top_vid_stretched)
