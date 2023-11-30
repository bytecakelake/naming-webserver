import httpx
import asyncio
from uuid import uuid4
from time import time


async def unit_tester(url):
    httpx.get(url)


async def main(tasks):
    await asyncio.gather(*tasks)
    

def request_performance_tester(num_try, url):
    tasks = [unit_tester(f"{url}?id={i}") for i in range(num_try)]
    test_id = uuid4()
    print(f"\nperformance testing ... [{test_id}]", end="")
    start = time()
    asyncio.run(main(tasks))
    end = time()
    print(f"\rperformance testing is done [{test_id}]")
    total_runtime = round(end - start, 4)
    avg_runtime = round(total_runtime / num_try, 4)
    average_processing = round(num_try / total_runtime, 4)
    print(f"-- {average_processing} req/s :: {avg_runtime} s/req :: total {total_runtime}s --")

req_num = 100
req_url = f"http://127.0.0.1:7700/"
request_performance_tester(req_num, req_url)



