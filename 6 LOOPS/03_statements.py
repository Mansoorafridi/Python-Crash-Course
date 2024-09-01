for i in range (100):
    if(i == 35):
        break       # Loop exits before printing 35
    print(i)


for i in range (100):
    if(i == 35):
        continue      ## Skip this iteration 
    print(i)


i = 1
while i <= 6:
    print(i)
    if i == 3:
        break          # Loop exits after printing 3
    i += 1