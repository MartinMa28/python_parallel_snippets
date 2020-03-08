import time
import threading

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done sleeping')

start = time.perf_counter()

pool = []

for _ in range(30):
    t = threading.Thread(target=do_something)
    t.start()
    pool.append(t)

for t in pool:
    t.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} secs')