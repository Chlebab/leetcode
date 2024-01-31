def dailyTemperatures(temperatures):
    answer = []        
    i = 1

    while i < len(temperatures) + 1:
        day_temp = temperatures[i-1]
        # print("day_temp: ",day_temp)
        # print("temperatures[i:]: ",temperatures[i:])     
        j = 1

        for temp in temperatures[i:]:
            if temp > day_temp:
                answer.append(j)
                # print("j after append: ",j)
                break
            else:
                j += 1
                # print("j after + 1: ",j)
        else:
            # print("there arent higher nums")
            answer.append(0)

        i += 1
        
    print("answer: ",answer)
    return answer

dailyTemperatures([65,31,53,688])