def to_time(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def solution(plans):
    result = []
    plans.sort(key=lambda x:x[1])
    stack = []
    for i in range(len(plans)):
        if i == len(plans) - 1:
            result.append(plans[i][0])
            while stack:
                keep = stack.pop()
                result.append(keep[0])
            break
        
        prev_time = to_time(plans[i][1])
        working = int(plans[i][2])
        next_time = to_time(plans[i+1][1])
        
        # 다음꺼 시작과 지금꺼 시작 사이의 시간이 지금꺼 실행시간보다 작으면, 스택 ㄱ.
        if next_time - prev_time < working:
            stack.append((plans[i][0], working - (next_time - prev_time)))
        
        # 다음꺼와 지금꺼의 텀에 지금꺼 실행할시간이 충분하면
        # elif next_time - prev_time >= working:
        else:
            # 끝날 수 있으니 결과에 지금꺼 추가
            result.append(plans[i][0])
            # 이전꺼의 끝난 시간
            end_time = prev_time + working
            
            # 다음꺼와의 텀 시간 구하기 (다음꺼 시작 - 지금꺼 종료시간)
            term = next_time - end_time
            # 텀 시간 동안 팝해서 끝낼 수 있는건 다 추가
            while stack:
                s = stack.pop()
                pop_name, pop_time = s
                # pop한거의 남은 시간이 텀보다 작거나 같으면 종료 가능. result에 append
                if term >= pop_time:
                    result.append(pop_name)
                    term -= pop_time
                # pop한거의 남은 시간이 텀보다 크면, (pop한 시간-텀)=남은시간 을 다시 stack에.    
                else:
                    pop_time -= term
                    stack.append((pop_name, pop_time))
                    break
        
    return result