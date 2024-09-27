import asyncio

"""
- gather tasks and run them asynchronously. 
- Expect both Hello & Goodbye to appear before Finished Task and Finished Goodbye are completed

"""

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate I/O-bound task
    print("Finished Task")

async def say_goodbye():
    print("Goodbye")
    await asyncio.sleep(2)  # Simulate another I/O-bound task
    print("Finished Goodbye")

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(say_hello(), say_goodbye())

# Main Entry point to run the async code - this is blocking (so you'll see the first print statement, followed by the tasks and then the last print statement)
print("**script-started")
asyncio.run(main())
print("**script-completed")