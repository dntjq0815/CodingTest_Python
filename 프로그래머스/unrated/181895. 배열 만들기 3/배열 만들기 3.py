def solution(arr, intervals):
    answer = []
    for i in range(len(intervals)):
        start, end = intervals[i][0], intervals[i][1]
        for j in range(start, end+1):
            answer.append(arr[j])
            
    return answer