#!/usr/bin/env python3
'''Wait function's module'''


import random
import asyncio


async def wait_random(max_delay: int = 10):
    '''Wait for a random number of seconds'''

    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
