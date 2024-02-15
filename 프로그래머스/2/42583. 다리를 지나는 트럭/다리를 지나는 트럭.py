from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     time = 0    # 경과시간
#     tmp = 0     # 다리를 건너는 트럭
#     depart = deque([0] * bridge_length)     # 다리를 지난 트럭
#     trucks = deque(truck_weights)   # 대기 트럭
    
#     while len(depart):
#         time += 1
#         tmp -= depart[0]
#         depart.popleft()
#         if trucks:
#             if tmp + trucks[0] <= weight:
#                 tmp += trucks[0]
#                 depart.append(trucks.popleft())
#             else:
#                 depart.append(0)

#     return time

def solution(bridge_length, weight, truck_weights):
    time = 0
    temp = 0
    on_bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    while len(on_bridge):
        time += 1
        temp -= on_bridge[0]
        on_bridge.popleft()
        
        if trucks:
            if (temp + trucks[0] <= weight):
                temp += trucks[0]
                on_bridge.append(trucks.popleft())
            else:
                on_bridge.append(0)
            
    return time