def canCompleteCircuit(gas, cost):
    i, j = 0 , 0
    tank = 0

    while i < len(cost):

        if tank + gas[i-len(gas)] >= cost[i-len(cost)] and j - len(gas) < len(gas) -1:
            j = i
            while tank + gas[j-len(gas)] >= cost[j-len(cost)]:
                tank += gas[j-len(gas)] - cost[j-len(cost)]
                j += 1
                if j - len(gas) == i :
                    return i


        i  += 1
    return -1
