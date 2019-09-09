def smallest_num_divisible_brute():
    num_not_found = True
    num = 1
    while num_not_found:
        divisible_by_all = True
        for i in range(min, max+1):
            if num % i != 0:
                divisible_by_all = False
                break
        if divisible_by_all:
            return num
        num += 1