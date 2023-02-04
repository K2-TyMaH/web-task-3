from datetime import datetime

def factorize(*numbers):
    result = []
    for elem in numbers:
        needed_nums = []
        new_num = elem
        while new_num > 0:
            if not elem % new_num:
                needed_nums.append(new_num)
            new_num -= 1
        result.append(needed_nums)

    return result


starter = datetime.now()

a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [128, 64, 32, 16, 8, 4, 2, 1]
assert b == [255, 85, 51, 17, 15, 5, 3, 1]
assert c == [99999, 33333, 11111, 2439, 813, 369, 271, 123, 41, 9, 3, 1]
assert d == [10651060, 5325530, 2662765, 2130212, 1521580, 1065106, 760790, 532553, 380395, 304316, 152158, 76079, 140, 70, 35, 28, 20, 14, 10, 7, 5, 4, 2, 1]

stoper = datetime.now()

f_time = stoper - starter

print(f_time)

