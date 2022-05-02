#Mean is avaergae of total number

list1 = [10,12,19,25,26,78,94,19,76,89,84,90,32,19,67,30,35,23]
mean = sum(list1)/len(list1)
print("Mean",mean)


#Median
#for odd (n+1)/2
#for even (((n/2)+((n+1)/2))/2)



list1.sort() #Ascending order
print(list1)
if len(list1)%2==0:
    med1 = list1[len(list1)//2]
    med2 = list1[len(list1)//2-1]
    print(med1)
    print(med2)
    median = (med1+med2)/2
    print("Median",median)
else:
    med = list1[len(list1)//2]
    print(med)


#Mode is max frequency
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("Mode",mode)    
