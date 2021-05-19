def ActivitySelection(Activities):
    selected=[]
    selected.append(Activities[0])
    k=0
    for i in range(1,len(Activities)):
        if Activities[i][0]>Activities[k][1]:
            selected.append(Activities[i])
            k=i

    return selected


s = list(map(int,input("Enter the the start times: ").split()))
f = list(map(int,input("Enter the the end times: ").split()))
Activities = []
for i in range(len(s)):
    data = [s[i],f[i]]
    Activities.append(data)
Activities.sort(key=lambda x: x[1])
print(Activities)
selected = ActivitySelection(Activities)
print("Selected Activities are:",selected)

