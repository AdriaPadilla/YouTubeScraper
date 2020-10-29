import pandas as pd

list_of_frames = []

def to_frame(data):
    print("---------> Creating Dataframe")
    for element in data:
        try:
            df = pd.DataFrame({
                "video_id": element["video_id"],
                "channel_title": element["channel_title"],
                "channel_id": element["channel_id"],
                "video_title": element["video_title"],
                "views_count": element["video_views"],
                "likes_count": element["video_likes"],
                "dislikes_count": element["video_dislikes"],
                "comment_count": element["video_comment"],
                "genre": element["video_genre"],
                "video_duration": element["video_duration"],
                "published_at": element["published_at"],
                "family_friendly": element["family"],
                "paid": element["paid"],
                "live_broadcast": element["live"],
                "start_live": element["live_start"],
                "end_live": element["live_end"],
                "keywords": [element["keywords"]],
            })
            list_of_frames.append(df)
        except TypeError:
            print("error on element: "+str(data.index(element)))
            pass

    final_df = pd.concat(list_of_frames, ignore_index=True)
    print(final_df)
    print("---------> DF To Excel")
    final_df.to_excel("output.xlsx")
    print("---------> job Done!")