t = int(input())
# print(t)
for i in range(t):
    cars = int(input())
    n = str(input())
    max_speed = list(map(int,n.split()))
    temp = max_speed[0]
    count = 1
    # print(max_speed[0])
    for j in range(1,len(max_speed)):
        if max_speed[j]<temp:
            count+=1
            temp = max_speed[j]

    print(count)
        

# 3
# 1
# 10
# 3
# 8 3 6
# 5
# 4 5 1 2 3