import asyncio
import requests as r
import aiohttp

from python_template.json import write_json, read_json
from dataclasses import dataclass, asdict
from requests.models import Response
from typing import List

@dataclass
class Response:
    url: str
    status:str
    text: Response
    is_redirect: str


## synchronous functions
def get_responses(urls):
    """traditional requests"""

    _responses = []
 
    for _u in urls:
        _r = r.get(_u)
        _responses.append(Response(url=_u, status=_r.status_code, text=_r.text, is_redirect=''))
    
    return _responses

def save_data(data:List[Response], file_loc:str):
    
    _d = [asdict(_d) for _d in data]
    write_json(data=_d, file_loc=file_loc)

def main(urls:list):

    # constants
    SAVE_LOC = 'data/output/responses.json'

    # make requests and save data
    responses = get_responses(urls=urls)
    save_data(responses, file_loc=SAVE_LOC)

## async functions
async def fetch(url):
    # https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientResponse
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            status = response.status
            return Response(url=url, status=status, text=text, is_redirect='')
        
async def async_main(urls:list):

    # constants
    SAVE_LOC = 'data/output/responses_async.json'

    # Schedule all API calls to run concurrently
    tasks = [fetch(url) for url in urls]

    # Wait for all tasks to complete
    responses = await asyncio.gather(*tasks)
    save_data(responses, file_loc=SAVE_LOC)

## run script
if __name__ == "__main__":

    """demonstrate traditional vs asychronous requests"""
    import time

    # urls to make requests
    urls = [
        'https://docs.aiohttp.org/en/stable/whats_new_3_0.html#aiohttp-whats-new-3-0',
        'https://www.cnn.com/2024/09/25/us/helene-tropical-storm-florida-evacuations/index.html',
        'https://weather.com/storms/hurricane/news/2024-09-25-hurricane-tropical-storm-helene-forecast-florida-southeast',
        'https://techcrunch.com/2024/09/25/meta-discontinues-quest-2-and-quest-pro/',
        'https://www.independent.co.uk/life-style/us-news-best-college-ranking-2025-worst-b2618559.html',
        # 'https://www.usnews.com/best-colleges/brown-university-3401',
        # 'https://www.usnews.com/best-colleges/brown-university-3401/overall-rankings',
        # 'https://money.usnews.com/loans/mortgages/mortgage-rate-forecast?rec-type=blueshift'
    ]

    # # synchronous requests
    # start = time.perf_counter()
    # main(urls=urls)
    # end = time.perf_counter()
    # print(f"it took: {end - start:.2f}s")

    # asynchronous requests
    start = time.perf_counter()
    asyncio.run(async_main(urls=urls))
    end = time.perf_counter()
    print(f"it took: {end - start:.2f}s")

    # sha256sum to see that the files are the same - they are not, I wonder why
