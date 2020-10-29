import pandas as pd
import concurrent.futures
import time
import parser_file as p
import scraper as s
import frame as f


data = pd.read_excel("subset_10.xlsx") # This is your Youtube Videos ID list to scrape
video_list = data["hash"].tolist()

works_index = []
for element in video_list:
    index = video_list.index(element)
    index = index+1
    works_index.append(index)

def main():
    print("---------> Total tasks: " + str(len(works_index)))
    page_results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=99) as executor:
        content = executor.map(s.scrape, video_list, works_index)
        page_results.extend(content)
    print("---------> ENDED SCRAPING")
    return page_results

def parser(page_results):
    print("---------> Start parsing data Process")
    parsed_data_list = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        parsed_data = executor.map(p.parse, page_results, video_list, works_index)
        parsed_data_list.extend(parsed_data)
    print("---------> Finished data parsing")
    return parsed_data_list

if __name__ == '__main__':
    start_time = time.time()
    page_results = main()
    data = parser(page_results)
    f.to_frame(data)
    print("--- %s seconds ---" % (time.time() - start_time))
