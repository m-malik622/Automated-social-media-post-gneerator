import os #for enviornment variables if you would like to have one for the api_key
from Search_For_Youtube_Video import *
from Download_Youtube_Vid import *
from Overlap_Videos import *


def Social_Media_Post_Automation(api_key: str, top_vid_query_terms: list[str], num_of_top_vids: int, bottom_vid_query_terms: list[str], num_of_bottom_vids: int, top_vid_download_destination: str, bottom_vid_download_destination: str, result_vid_path:str, start_time:int, end_time:int, have_top_vid_stretched:bool):
    top_video_links = Search_For_Youtube_Video(api_key, top_vid_query_terms, num_of_top_vids)
    for top_video_link in top_video_links:
        top_vid_path = Download_Youtube_Vid(top_video_link, top_vid_download_destination)

    print("the top video has been succesfully downloaded")

    bottom_video_links = Search_For_Youtube_Video(api_key, bottom_vid_query_terms, num_of_bottom_vids)
    for bottom_video_link in bottom_video_links:
        bottom_vid_path = Download_Youtube_Vid(bottom_video_link, bottom_vid_download_destination)
    print("the bottom video has been succesfully downloaded")

    Overlap_Videos(top_vid_path, bottom_vid_path, result_vid_path, start_time, end_time, have_top_vid_stretched)



Social_Media_Post_Automation(os.environ.get('API_KEY'), ["family guy funny moments"], 1, ["gta5 mega ramp gameplay"], 1, r"Video_Folders\top_video", r"Video_Folders\bottom_video", r"Video_Folders\result_video\final_video2.mp4", 60, 120, False)




#os.environ.get('API_KEY')