from bs4 import BeautifulSoup
import threading

error_list = []

def parse(page, id, item):

    print("Parsing item: "+str(item)+" data for: "+id)
    data = {}
    try:
        soup = BeautifulSoup(page, 'html.parser')
        # basic_info = soup.find_all("div", class_="watch-main-col")
        video_id = str(soup.find_all("meta", itemprop="videoId")[0]).split("=")[1].split('"')[1]
        channel_title = str(soup.find_all("link", itemprop="name")[0]).split("=")[1].split('"')[1]
        channel_id = str(soup.find_all("meta", itemprop="channelId")[0]).split("=")[1].split('"')[1]
        video_title = str(soup.find_all("meta", itemprop="name")[0]).split("=")[1].split('"')[1]
        video_genre = str(soup.find_all("meta", itemprop="genre")[0]).split("=")[1].split('"')[1]
        views = str(soup.find_all("meta", itemprop="interactionCount")[0]).split("=")[1].split('"')[1].replace(".", "")
        views = int(views)
        likes = str(soup).split("Me gusta:")[2].split('"')[4].replace(".", "")
        likes = int(likes)
        dislikes = str(soup).split('No me gusta"}},"simpleText":"')[1].split('"')[0].replace(".", "")
        dislikes = int(dislikes)
        comments = "null"
        video_duration = str(soup.find_all("meta", itemprop="duration")[0]).split("=")[1].split('"')[1]
        published_at = str(soup.find_all("meta", itemprop="datePublished")[0]).split("=")[1].split('"')[1]
        family = str(soup.find_all("meta", itemprop="isFamilyFriendly")[0]).split("=")[1].split('"')[1]
        paid = str(soup.find_all("meta", itemprop="paid")[0]).split("=")[1].split('"')[1]

        # It's live content exception!
        try:
            live = str(soup.find_all("meta", itemprop="isLiveBroadcast")[0]).split("=")[1].split('"')[1]
        except IndexError:
            live = "false"
        if live == "True":
            live_start = str(soup.find_all("meta", itemprop="startDate")[0]).split("=")[1].split('"')[1]
            live_end = str(soup.find_all("meta", itemprop="endDate")[0]).split("=")[1].split('"')[1]
        else:
            live_start = "false"
            live_end = "false"
        # Video Keywords Meta-tag

        keywords = str(soup).split('name="description"/>')[1].split('"')[1].split(",")
        clean_keywords_list = []
        for element in keywords:
            clean = element.strip()
            clean_keywords_list.append(clean)

        data["video_id"] = video_id
        data["channel_title"] = channel_title
        data["channel_id"] = channel_id
        data["video_title"] = video_title
        data["video_genre"] = video_genre
        data["video_views"] = views
        data["video_likes"] = likes
        data["video_dislikes"] = dislikes
        data["video_comment"] = comments
        data["video_duration"] = video_duration
        data["published_at"] = published_at
        data["family"] = family
        data["paid"] = paid
        data["live"] = live
        data["live_start"] = live_start
        data["live_end"] = live_end
        data["keywords"] = clean_keywords_list
        return data

    except IndexError:
        data["video_id"] = str(id)
        data["channel_title"] = "null"
        data["channel_id"] = "null"
        data["video_title"] = "video not avaliable"
        data["video_genre"] = "null"
        data["video_views"] = "null"
        data["video_likes"] = "null"
        data["video_dislikes"] = "null"
        data["video_comment"] = "null"
        data["video_duration"] = "null"
        data["published_at"] = "null"
        data["family"] = "null"
        data["paid"] = "null"
        data["live"] = "null"
        data["live_start"] = "null"
        data["live_end"] = "null"
        data["keywords"] = "null"
        print("Work ended by worker: "+threading.current_thread().name+" | reason: Not avaliable")

        return data

