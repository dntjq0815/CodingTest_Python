import re

def solution(myStr):
    answer = re.sub('(a|b|c)', ' ', myStr).split()
    
    return answer if len(answer) > 0 else ['EMPTY']