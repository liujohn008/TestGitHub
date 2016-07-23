# Joseph Problem

def safePosition(total, killPosition):
    s1 = 0
    s2 = 1
    for i in range(2,total+1):
        s1 = (s1 + killPosition) % i
        s2 = (s2 + killPosition) % i
        #print s1
    return s1, s2

print safePosition(5,3)
