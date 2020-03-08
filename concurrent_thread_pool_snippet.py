import time
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

def do_something(secs):
    print(f'Sleeping {secs}...')
    time.sleep(secs)
    return f'Done sleeping {secs} sec'

start = time.perf_counter()

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(do_something, sec) for sec in range(5, 0, -1)]

    for f in concurrent.futures.as_completed(futures):
        print(f.result())


with ThreadPoolExecutor() as executor:
    results = executor.map(do_something, range(5, 0, -1))

    for result in results:
        print(result)

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} secs')