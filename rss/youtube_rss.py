import urllib.request, urllib.error, urllib.parse
from urllib.parse import urlparse

def fixup_youtube_subscription_link(log, url):
    try:
        parsed_uri = urlparse(url)
        hostname = '{uri.netloc}'.format(uri=parsed_uri)
        if hostname.endswith("youtube.com") and not "youtube.com/feeds" in url:
            yt_id = get_youtube_channel_id(url)
            if yt_id != None:
                return "https://www.youtube.com/feeds/videos.xml?channel_id={}".format(yt_id)
    except:
        log.exception(f"Processing YouTube URL '{url}' failed")
    return url

# https://stackoverflow.com/a/16326307
def get_youtube_channel_id(url):
    response = urllib.request.urlopen(url)
    webContent = response.read().decode()
    searches = ['"externalId":"', 'data-channel-external-id="']
    for search in searches:
        try:
            index = webContent.index(search)
            index1 = index + len(search)
            index2 = webContent.index('"', index1)
            return webContent[index1:index2]
        except ValueError:
            pass
    return None
