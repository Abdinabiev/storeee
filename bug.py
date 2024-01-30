def sum_numbers(*args):
    summ_nums = 0
    for i in args:
        if i  != 0:
            summ_nums += i
    print(summ_nums)
sum_numbers(5,3,4,5,4,4,3)
    
