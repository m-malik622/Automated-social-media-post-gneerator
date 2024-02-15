from googleapiclient.discovery import build


def Search_For_Youtube_Video(api_key: str, query_terms: list[str], num_of_vids: int) -> list[str]:
    """
    Search for YouTube videos based on one or multiple query terms.

    Args:
        api_key (str): Your API key for YouTube Data API v3. Create a free one at https://console.cloud.google.com/apis/library/youtube.googleapis.com?project=singular-antler-412916
        query_terms (list[str]): List of query terms. These terms will be inserted into the search bar on youtube
        num_of_vids (int): Number of videos to retrieve.

    Returns:
        list[str]: List of video links matching the search query.
    """
    # Set up the YouTube Data API. 
    youtube = build('youtube', 'v3', developerKey=api_key)

    #to convert the tags (input) to a string youtube.search().list() would understand
    if (len(query_terms)==1):
        query_term=query_terms[0]
    else:
        query_term=""
        for term in query_terms:
            query_term += term + '|'
        query_term=query_term[:-1]

    #excecute serch(cutomize to your liking)
    rerequest = youtube.search().list(
        part='id',
        order='relevance',
        q=query_term,
        type='video',
        maxResults=num_of_vids
    ) 
    responce = rerequest.execute()
    
    #to grab video link/s from search
    video_links = []
    for video in responce.get('items', []):
        video = ("https://www.youtube.com/watch?v="+ video['id']['videoId'])
        video_links.append(video)

    return video_links