def calculate_time(func):
    def time_diff():
        start = time.perf_counter()
        func()
        finish = time.perf_counter()
        print(f'finished two thread in  {finish-start}')
    return time_diff


from threading import Thread
import time 
def do_something():
    time.sleep(2)
    print("done")
# do_something()
# do_something()

def do_something_2(second):
    time.sleep(second)
    print("args_ done")





#  any program running synchronously are called as CPU bound or IO bound task 
#  in case of IO bound task we prefer threading because they do not bother CPU that much 
#  if progam is reading from the data and processing that we use processing 


# in order to achive threading we'll import threading module 
@calculate_time
def managing_two_thread():


    # secondly we will create threads 
    thread_1 = Thread(target=do_something)
    thread_2 = Thread(target=do_something) 

    # start threads

    thread_1.start()
    thread_2.start()

    # join thre thread with the current execution otherwise other code will execute 
    thread_1.join()
    thread_2.join()

@calculate_time
def manage_multiple_thread():
    # we want to run something function 10 times we'll loop over the thread and to store them we'll user a list
    
    threads = []
    for _ in range(10):
        thread = Thread(target=do_something)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join() 
       

# handeling arg inthread

@calculate_time
def handeling_arg_with_thread():
    threads = []
    for _ in range(10):
        t = Thread(target=do_something_2, args=[1.5])
        t.start()

    for thread in threads:
        thread.join()

handeling_arg_with_thread()

