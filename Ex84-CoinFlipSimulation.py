
import random as rn

n = int(input("Enter the number of flips: "))
Sum = 0
AverageSum = 0
for i in range(n):
    consecutive = 0
    flips = 0
    outcome = ""
    while consecutive != 3:
        toss = rn.randint(0,1)
        if toss == 1:
            toss = " H "
        else:
            toss = " T "

        if flips == 0:
            outcome = toss
            consecutive += 1
        else:
            if outcome == toss:
                consecutive += 1
            else:
                pass
                consecutive = 1
                outcome = toss
        print(toss, end="")
        flips += 1
    print("({} flips)".format(flips))
    Sum += flips
    AverageSum = Sum / n


print("Average number of flips needed to reach 3 consecutive occurrences:", AverageSum)


























"""for toss in range(10):
    count_h += 1
    toss = random.randint(0,1)
    if toss == 1:
        outc = outc + "H"
    else:
        outc = outc + "T"
while outc[-2] != outc[-1] != outc[0]:
    break

print(outc)"""
