def solution(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    
    if len_arr1 > len_arr2:
        return 1
    
    elif len_arr1 < len_arr2:
        return -1
    
    elif len_arr1 == len_arr2:
        sum_arr1 = sum(arr1)
        sum_arr2 = sum(arr2)
        if sum_arr1 > sum_arr2:
            return 1
        elif sum_arr1 < sum_arr2:
            return -1
        else:
            return 0