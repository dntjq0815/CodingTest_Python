def solution(arr, queries):
    for query in queries:
        start = query[0]
        end = query[1]
        k = query[2]
        
        for i in range(start, end + 1):
            if i % k == 0:
                arr[i] += 1
    return arr