# def solution(progresses, speeds):
#     answer = []
#     while progresses:
#         for i in range(len(progresses)):
#             progresses[i] += speeds[i]

#         count = 0
#         while progresses and progresses[0] >= 100:
#             count += 1
#             progresses.pop(0)
#             speeds.pop(0)

#         if count > 0:
#             answer.append(count)

#     return answer

from collections import deque

def solution(progresses, speeds):
    day = 0     # 일자
    deployDay = 0   # 배포일자
    answer = []
    
    queue = deque()
    for progress, speed in zip(progresses, speeds):
        queue.append((progress, speed))
    
    while queue:
        day += 1
        
        while queue and (queue[0][0] + (day * queue[0][1])) >= 100:
            deployDay += 1
            queue.popleft()
            
        if deployDay != 0:
            answer.append(deployDay)
            deployDay = 0
    
    return answer