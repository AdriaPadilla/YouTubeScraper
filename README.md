# YouTube Scraper

Hi All! 

This is an example of how we can scrape YouTube Video metrics. This thecnique is especially useful for those who need to collect video data, but have API quota limitations.
I have written this code as an example, in the framework of a PhD thesis. **This is only a hypothetical exercise, and is not intended for intensive work. It's only a methodological approximation.**

There are some important considerations:
- **The starting point is the ID of a video**. For the script to work you must have a CSV document with all the IDs. 
F.e.: https://www.youtube.com/watch?v=XPXM47rhFwY -> XPXM47rhFwY = Video ID
- **Comments cannot be scraped**: The reason, is that I use *BeautifulSoup* library. "Comment counter" in YouTube interface is generated trought Asynchronous JavaScript (AJAX), and the BeautifulSoup library can't handle this type of content.
- **The script has been written using the ".es" version of YouTube**. If you respect this URL structure, the script will provably work as long as the source code is not changed. But if you change to the ".com" version of the YouTube URL, you may need to make some changes in this script.
- **You are free to take this code as an example and do whatever you want with it**, under GNU liscense.
- The script is provided "as it is", and no technical support is given.
- This is an hypothetical academic walkarraond to solve a problem. It is not necessarily intended to be put into operation, or to work intensively.
- The author is not responsible for malicious use or any other damage it may cause.

**Performance tests**
- With ThreadPoolexEcutor and ProcessPoolExecutor: Tested with 1000 URL = 0.39s/url. This includes: request url content + html parsing (bs4) and dataset export to xlsx file.
- Possible improvements: Parse html responses with xlmx bs4. 

**Special thanks**
- Prof. Bernhard Rieder (Amsterdam University) https://github.com/bernorieder/
- Raquel Horta https://github.com/raquelhortab
