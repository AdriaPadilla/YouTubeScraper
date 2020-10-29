import requests
import threading
import random
import time

def scrape(id, index):
    sleeptime = random.randint(0, 5)
    print("Sleeping for: " + str(sleeptime) + " Seconds | Worker: " + threading.current_thread().name)
    time.sleep(sleeptime)
    url = f"https://youtu.be/{id}"
    print("Job Nº: "+str(index)+" | Scraping url: " + url + " | Job with Worker: " + threading.current_thread().name)
    requests_session = requests.Session()
    page = requests_session.get(url)
    content = page.content
    return content