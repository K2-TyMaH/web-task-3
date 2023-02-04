from multiprocessing import Process
from datetime import datetime
import logging


def factorize(number):
    needed_nums = []
    new_num = number
    while new_num > 0:
        if not number % new_num:
            needed_nums.append(new_num)
        new_num -= 1
    logging.debug(f"{needed_nums}")   

    


a, b, c, d = (128, 255, 99999, 10651060)
process_list = (a, b, c, d)


if __name__ == '__main__':
    starter = datetime.now()
    logging.basicConfig(level=logging.DEBUG, format='%(processName)s %(message)s')
    
    
    processes = []
    for item in process_list:
        pr = Process(target=factorize, args=(item, ))
        pr.start()
        processes.append(pr)
        

    [pr.join() for pr in processes]
    
    #assert a == [128, 64, 32, 16, 8, 4, 2, 1]
    #assert b == [255, 85, 51, 17, 15, 5, 3, 1]
    #assert c == [99999, 33333, 11111, 2439, 813, 369, 271, 123, 41, 9, 3, 1]
    #assert d == [10651060, 5325530, 2662765, 2130212, 1521580, 1065106, 760790, 532553, 380395, 304316, 152158, 76079, 140, 70, 35, 28, 20, 14, 10, 7, 5, 4, 2, 1]

    stoper = datetime.now()

    f_time = stoper - starter

    print(f_time)
