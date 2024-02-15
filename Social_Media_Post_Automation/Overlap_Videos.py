from moviepy.editor import *
from moviepy.video.fx.all import *

def Overlap_Videos(top_vid_path: str, bottom_vid_path: str, result_vid_path: str, start_time: int, end_time: int, have_top_vid_stretched: bool):
    """
    Places one video on top of the other

    Args:
        top_vid_path (str): Path of the video you would like to display on top.
        bottom_vid_path (str): Path of the video you would like to display on bottom.
        result_vid_path (str): Path to save the resulting video.
        start_time (int): Start time (in seconds) of both clips.
        end_time (int): End time (in seconds) of both clips.
        have_top_vid_stretched (bool): Whether to stretch the top video to takeup more space or have it appear smaller with a truer aspect ratio.
    """
    top_clip = VideoFileClip(top_vid_path).subclip(start_time,end_time).fx(afx.audio_normalize).resize((720, 405))
    if (have_top_vid_stretched==True):
        bottom_clip = VideoFileClip(bottom_vid_path, audio=False).subclip(start_time,end_time).resize(width=720)
    else:
        bottom_clip = VideoFileClip(bottom_vid_path, audio=False).subclip(start_time,end_time).resize((720, 875))

    final_clip = clips_array([[top_clip],[bottom_clip]]).resize((720, 1280))        
    final_clip.write_videofile(result_vid_path)
    final_clip.close
