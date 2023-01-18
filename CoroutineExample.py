# The following example shows how to use coroutines to download a list of URLs in parallel.
# Coroutines are a special kind of generator
# that can be paused and resumed multiple times.
# They allow you to write asynchronous code in a synchronous style.
# This is mainly useful when you need to wait for some I/O operation to complete.
# For example, you might need to wait for a network request to complete.
# The download_one function is a coroutine that downloads a URL and returns the number of bytes downloaded.
# The download_all function is a coroutine that calls download_one for each URL in a list of URLs.
# The main function creates an event loop and runs the download_all coroutine.
# The event loop runs until the download_all coroutine completes.
# The main function then prints the total number of bytes downloaded.


import asyncio
import time
import aiohttp
import async_timeout


async def download_one(url):
    async with aiohttp.ClientSession() as session:
        with async_timeout.timeout(10):
            async with session.get(url) as response:
                print('Read {} from {}'.format(response.content_length, url))
                return response.content_length


async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    return await asyncio.gather(*tasks)


async def main():
    sites = [
                'https://www.jython.org',
                'http://olympus.realpython.org/dice',
            ] * 80
    start_time = time.time()
    total_length = await download_all(sites)
    end_time = time.time()
    msg = '{} sites downloaded in {:.2f} seconds'
    print(msg.format(len(total_length), end_time - start_time))
    # print(total_length)

asyncio.run(main())


