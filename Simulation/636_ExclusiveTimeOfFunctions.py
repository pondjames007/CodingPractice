# TIPS:
#
# Remember to +1 when end since it is finished after that time
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        table = [0]*n
        stack = []
        prev = 0
        for log in logs:
            fid, act, time = log.split(':')
            fid, time = int(fid), int(time)
            if act == 'start':
                if stack:
                    table[stack[-1]] += time - prev
                stack.append(fid)
                prev = time
            else:
                table[stack.pop()] += (time + 1) - prev
                prev = time + 1
        
        return table