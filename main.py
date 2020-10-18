import requests
from bs4 import BeautifulSoup
import timeit
import pandas as pd
from tqdm import tqdm

data = pd.read_csv("dataset.csv") # Path to the file where you store the vide ID's
video_list = data["hash"].tolist() # Use your own column name to find video ID's

video_id_list = []
channel_title_list = []
video_title_list = []
channel_id_list = []
video_genre_list = []
video_views_list = []
video_likes_list = []
video_dislikes_list = []
video_comment_list = []
video_duration_list = []
published_at_list = []
family_list = []
paid_list = []
live_list = []
live_start_list = []
live_end_list = []
keywords_list = []

error_list = []

def scrape(id):

    # Let's TRY to scrape basic info
    try:
        url = f"https://youtu.be/{id}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        basic_info = soup.find_all("div", class_="watch-main-col")

        video_id = id
        channel_title = str(soup.find_all("link", itemprop="name")[0]).split("=")[1].split('"')[1]
        channel_id = str(soup).split("browseId")[2].split('"')[2]
        video_title = str(soup.find_all("meta", itemprop="name")[0]).split("=")[1].split('"')[1]
        video_genre = str(soup.find_all("meta", itemprop="genre")[0]).split("=")[1].split('"')[1]
        views = str(soup.find_all("meta", itemprop="interactionCount")[0]).split("=")[1].split('"')[1].replace(".", "")
        views = int(views)
        likes = str(soup).split("Me gusta:")[2].split('"')[4].replace(".", "")
        likes = int(likes)
        dislikes = str(soup).split('No me gusta"}},"simpleText":"')[1].split('"')[0].replace(".", "")
        dislikes = int(dislikes)
        comments = "null" # Comments can't be scraped due AJAX BeatutifulSoup Limitations!!!
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

        ## All Data To lists

        video_id_list.append(video_id)
        channel_title_list.append(channel_title)
        channel_id_list.append(channel_id)
        video_title_list.append(video_title)
        video_genre_list.append(video_genre)
        video_views_list.append(views)
        video_likes_list.append(likes)
        video_dislikes_list.append(dislikes)
        video_comment_list.append(comments)
        video_duration_list.append(video_duration)
        published_at_list.append(published_at)
        family_list.append(family)
        paid_list.append(paid)
        live_list.append(live)
        live_start_list.append(live_start)
        live_end_list.append(live_end)
        keywords_list.append(clean_keywords_list)
    except IndexError:
        error_list.append(id)

start = timeit.timeit()
items = len(video_list)

ammount = len(video_list) # Count nº of files for progress bar
message = "Videos scraped: "
pbar = tqdm(total=ammount, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', desc=message) # Parameters for tqdm progress bar

for id in video_list:
    scrape(id)
    pbar.update()  # In each loop, progress bar updates

tqdm._instances.pop().close() # This close all tqdm instances and prevent from re-print

print("creating Dataframe")
df = pd.DataFrame({
    "video_id": video_id_list,
    "channel_title": channel_title_list,
    "channel_id": channel_id_list,
    "video_title": video_title_list,
    "views_count": video_views_list,
    "likes_count": video_likes_list,
    "dislikes_count": video_dislikes_list,
    "comment_count": video_comment_list,
    "genre": video_genre_list,
    "video_duration": video_duration_list,
    "published_at": published_at_list,
    "family_friendly": family_list,
    "paid": paid_list,
    "live_broadcast": live_list,
    "start_live": live_start_list,
    "end_live": live_end_list,
    "keywords": keywords_list,
    })

print("DF To Excel")
df.to_excel("output.xlsx")

error_df = pd.DataFrame({
    "id_error": error_list,
})
error_df.to_excel("error_list.xlsx")
print("job Done!")
end = timeit.timeit()
print("time to complete the task: "+str(end - start)+" seconds")
