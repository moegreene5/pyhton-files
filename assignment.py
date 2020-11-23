def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    avg = sum_num/len(num)
    return avg
print ('the average is',
cal_average([76,56,35,55,87]))