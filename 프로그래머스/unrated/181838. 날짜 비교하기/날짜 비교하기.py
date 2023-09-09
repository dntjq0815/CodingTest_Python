def solution(date1, date2):
    date1_string = ''
    date2_string = ''
    for i in range(len(date1)):
        date1_string += str(date1[i])
        
    for j in range(len(date2)):
        date2_string += str(date2[j])
    
    if int(date1_string) < int(date2_string):
        return 1
    
    else:
        return 0