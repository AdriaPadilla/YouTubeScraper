# YouTube Scraper

Hi All! 

This is an example of how we can scrape YouTube Video metrics. This thecnique is especially useful for those who need to collect video data, but have API quota limitations.
I have written this code as an example, in the framework of a doctoral thesis. **Possibly needs a lot of improvement, and is not intended for intensive work**. It is only a methodological approximation.

There are some important considerations:
- **The starting point is the ID of a video**. For the script to work you must have a CSV document with all the IDs. F.e.: https://www.youtube.com/watch?v=***XPXM47rhFwY***
- **Comments cannot be scraped**: The reason, is that I use *BeautifulSoup* library. "Comment counter" in YouTube interface is generated trought Asynchronous JavaScript (AJAX), and the BeautifulSoup library can't handle this type of content.
- **The script has been written using the ".es" version of YouTube**. If you respect this URL structure, the script will provably work as long as the source code is not changed. But if you change to the ".com" version of the YouTube URL, you may need to make some changes in this script.
- The Script has a **progress counter** (TQDM progress bar).
- **You are free to take this code as an example and do whatever you want with it**, under GNU liscense.
- The script is provided "as it is", and no technical support is given.
- This is an hypothetical academic walkarraund to solve a problem. The author is not responsible for malicious use or any other damage it may cause.


