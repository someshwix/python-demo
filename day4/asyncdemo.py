import asyncio 
#userfull for performing async operations on IO bound tasks(file operations, network operations)
async def upload():
    print(f"upload coroutine started")
    #performing some  bog task of IO
    await asyncio.sleep(4) # request .post (URL+bigdata) - simulate this
    print(f"upload coroutine ended")

async def download():
    print(f"upload coroutine started")
    #performing some  bog task of IO
    await asyncio.sleep(6) # request .post (URL+bigdata) - simulate this
    print(f"upload coroutine ended")

if __name__ == "__main__":
    print(f"main started")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(upload(), download()))
    loop.close()
    print(f"main ended")        
