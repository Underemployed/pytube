import logging
import pandas as pd
from pytube import Channel


LOGGER = logging.getLogger(__name__)
HANDLER = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
HANDLER.setFormatter(formatter)

LOGGER.addHandler(HANDLER)
LOGGER.setLevel(logging.INFO)

LOADING_PATH_SYNTAX = "./data/{}.csv"

############################################
# INPUT
url = "https://www.youtube.com/@MrBeast"

############################################
ch = Channel(url)

data = []

LOGGER.info("Download started...")
for v in ch.videos:

    LOGGER.info(v.title)
    try:
        s = v.streams
    except:
        pass

    d = {
        "id": v.video_id,
        "title": v.title,
        "views": v.views,
        "publish_date": v.publish_date,
        "description": v.description,
        "keywords": v.keywords,
        "length": v.length
    }

    data.append(d)

LOGGER.info("Download completed")

table = pd.DataFrame(data)

loading_path = LOADING_PATH_SYNTAX.format(ch.channel_name)
LOGGER.info(f"Saving data at {loading_path}...")
table.to_csv(loading_path, index=False)

LOGGER.info("Done")
