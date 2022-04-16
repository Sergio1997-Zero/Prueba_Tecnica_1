import json
import asyncio
import websockets

import threading
import time

from Tools.operations import prime_numbers
from Tools.operations import pair_numbers
from Tools.operations import odd_numbers

async def Tec_1():

    async with websockets.connect('ws://209.126.82.146:8080') as websocket:
        count = 0
        list_dates = []
        struct = { }
        while (count < 100):
            response = await websocket.recv()
            dict_response = json.loads(response)
            list_dates.append(dict_response['b'])
            count += 1

        struct['_max_number'] = max(list_dates)
        struct['min_number'] = min(list_dates)
        struct['first_number'] = list_dates[0]
        struct['last_number'] = list_dates[-1]
        struct['number_of_prime_numbers'] = prime_numbers.prime_numbers(list_dates)
        struct['number_of_even_numbers'] = pair_numbers.pair_numbers(list_dates)
        struct['number_of_odd_numbers'] = odd_numbers.odd_numbers(list_dates)
        
        print(struct)

def main(funtion, repeat):
    
    for x in range(repeat):

        print(f"Cicle {x} of {repeat}")

        asyncio.get_event_loop().run_until_complete(funtion())

        time.sleep(60)


main(Tec_1,3)