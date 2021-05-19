def JobSequencing(jobData):
    jobData.sort(reverse=True,key=lambda x: x[2])
    # print(jobData)
    n = len(jobData)
    slots = [False]*n
    sequence = [1]*n
    for x in range(n):
        for y in range(min(n-1,jobData[x][1]-1),-1,-1):
            if slots[y]==False:
                sequence[y] = jobData[x][0]
                slots[y] = True
                break

    return sequence


n = int(input("Enter the number of jobs to perform: "))
jobData = []
for i in range(n):
    data = list(input().split())
    jobData.append(data)
    jobData[i][1] = int(jobData[i][1])
    jobData[i][2] = int(jobData[i][2])
sequence = JobSequencing(jobData)
print("Sequence of Jobs to obtain maximum profit : ")
for i in sequence:
    if not type(i)== int:
        print(i,end=', ')
