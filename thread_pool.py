import concurrent.futures
import time 
start = time.perf_counter()
# its used best with the context manager 
def do_something(seconds):
    print(f"sleeping for {seconds} seconds(s)")
    time.sleep(seconds)
    return f"done sleeping for {seconds} "

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 6, 4, 3, 7, 1]
    result = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(result):
        print(f.result())

    # to arrange threads in the same order of secs we require to use map

    results = executor.map(do_something, secs)
    for result in results:
        print(result)

print(f"done in {time.perf_counter() - start}")