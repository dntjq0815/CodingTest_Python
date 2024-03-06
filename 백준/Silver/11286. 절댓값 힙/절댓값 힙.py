import heapq as hq
import sys

heap = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())

    if x != 0:
        hq.heappush(heap, (abs(x), x))      # 절댓값 x와 원본 x를 같이 저장한다
    else:
        print(hq.heappop(heap)[1] if heap else 0)