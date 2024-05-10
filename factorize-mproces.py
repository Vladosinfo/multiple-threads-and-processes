import time
from multiprocessing import Process, cpu_count, Pool, Queue

import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


# multiprocessing version using queue
q = Queue()

def factorize_processing_queue(*number):
    for num in number:
        pr = Process(target=calculation, args=(q, ))
        pr.start()
        q.put(num)

def calculation(queue: Queue):
    items_without_remainder = []
    num = queue.get()
    for i in range(1, num+1):
        if num % i == 0:
            items_without_remainder.append(i)
    print(items_without_remainder)


# synchronuous version
def factorize(*number):
    number_list = list() 
    counter = 0
    for num in number:
        items_without_remainder = []
        for i in range(1, num+1):
            if num % i == 0:
                items_without_remainder.append(i)
        number_list.append(items_without_remainder)
        print(number_list[counter])

        counter = counter + 1

    return number_list


# multiprocessing version using pool process
def factorize_process_pool(*number):
    with Pool(cpu_count()) as pool:
        pool.map_async(factorize, number)
        pool.close()
        pool.join()


def main():
    start = time.time()
    factorize(128, 255, 99999, 10651060)
    finish = time.time()
    print(f"\nTime result factorize: {finish - start}")

    print("="*35)

    fq_start = time.time()
    factorize_processing_queue(128, 255, 99999, 10651060)
    fq_finish = time.time()
    print(f"\nTime result factorize_processing: {fq_finish - fq_start}")

    # print("*"*35)

    # f_start = time.time()
    # factorize_process_pool(128, 255, 99999, 10651060)
    # f_finish = time.time()
    # print(f"\nTime result factorize_process: {f_finish - f_start}")
    

if __name__ == "__main__":
    main()