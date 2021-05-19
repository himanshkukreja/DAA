def permutations(li):
     if len(li) == 0:
         return []
     if len(li) == 1:
         return [li]
     per = []
     
     for i in range(len(li)):
         m = li[i]
         remList = li[:i] + li[i+1:]
         
         for p in permutations(remList):
             per.append([m]+ p )
     return per
  

per = permutations([1,2,3,4])
print(per)