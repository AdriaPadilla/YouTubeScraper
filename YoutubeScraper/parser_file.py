from bs4 import BeautifulSoup
import threading

error_list = []

def parse(page, id, item):

    print("Parsing item: "+str(item)+" data for: "+str(id))
    data = {}
    try:
        soup = BeautifulSoup(page, 'html.parser')
        # basic_info = soup.find_all("div", class_="watch-main-col")
        try:
            video_id = str(soup.find_all("meta", itemprop="videoId")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_id = "null"
        try:
            channel_title = str(soup.find_all("link", itemprop="name")[0]).split("=")[1].split('"')[1]
        except IndexError:
            channel_title = "null"
        try:
            channel_id = str(soup.find_all("meta", itemprop="channelId")[0]).split("=")[1].split('"')[1]
        except IndexError:
            channel_id = "null"
        try:
            video_title = str(soup.find_all("meta", itemprop="name")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_title = "null"
        try:
            video_genre = str(soup.find_all("meta", itemprop="genre")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_genre = "null"
        try:
            views = str(soup.find_all("meta", itemprop="interactionCount")[0]).split("=")[1].split('"')[1].replace(".", "")
            views = int(views)
        except IndexError:
            views = "null"
        try:
            likes = str(soup).split('{"iconType":"LIKE"}')[1].split('Me gusta')[0].split('"label":"')[1].replace(".", "")
        except IndexError:
            likes = "null"
        try:
            dislikes = str(soup).split('No me gusta"}},"simpleText":"')[1].split('"')[0].replace(".", "")
            dislikes = int(dislikes)
        except IndexError:
            dislikes = "null"
        try:
            comments = "null"
        except IndexError:
            comments = "null"
        try:
            video_duration = str(soup.find_all("meta", itemprop="duration")[0]).split("=")[1].split('"')[1]
        except IndexError:
            video_duration = "null"
        try:
            published_at = str(soup.find_all("meta", itemprop="datePublished")[0]).split("=")[1].split('"')[1]
        except IndexError:
            published_at = "null"
        try:
            family = str(soup.find_all("meta", itemprop="isFamilyFriendly")[0]).split("=")[1].split('"')[1]
        except IndexError:
            family = "null"
        try:
            paid = str(soup.find_all("meta", itemprop="paid")[0]).split("=")[1].split('"')[1]
        except IndexError:
            paid = "null"

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
        print("Work ended by worker: "+threading.current_thread().name+" | reason: "+IndexError)

        return data
