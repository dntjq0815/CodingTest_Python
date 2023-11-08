def solution(numbers):
    num_dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    for num in num_dic:
        if num in numbers:
            numbers = numbers.replace(num, num_dic[num])
            
    return int(numbers)