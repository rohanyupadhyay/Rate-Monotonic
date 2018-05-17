



et=[]
p=[]
t=[]
r=[]
timeLeft=[]
timeline=[]
print("Enter the number of tasks: ")
n=int(input())
for i in range(n):
    t.append(int(i))
    print("Enter time of task",i+1,":")
    et.append(int(input()))
    timeLeft.append(et[i])
    print("Enter the periodicity of task",i+1,":")
    p.append(int(input()))
    print("Enter the release time of task",i+1,":")
    r.append(int(input()))



for i in range(n):
    if p[i] >= p[i-1]:
        continue
    tempp = p[i]
    tempt = t[i]
    tempe = et[i]
    tempr = r[i]
    while i != 0 and tempp < p[i-1]:
        p[i] = p[i-1]
        t[i] = t[i-1]
        et[i] = et[i-1]
        r[i] = r[i-1]
        i -= 1
    p[i] = tempp
    t[i] = tempt
    et[i] = tempe
    r[i] = tempr

for i in range(n):
    timeLeft[i]=0

print(p)
print(t)


lcm=1
temp_p=p.copy()
i=2

while i <= max(temp_p):
    counter=0
    for j in range(len(temp_p)):
        
        if temp_p[j]%i==0:
            counter=1
            temp_p[j]/=i

    if counter==1:
        lcm=lcm*i
    else:
        i+=1




for i in range(lcm):
    for j in range(n):
        if (i!=0 and i%p[j]==0) or r[j]==i:
            timeLeft[j]=et[j]
    for j in range(n):
        if(timeLeft[j]>0):
            timeline.append(t[j]+1)
            timeLeft[j]-=1
            break
        elif j==n-1:
            timeline.append(0)
            
print("\n\n")

mn=0
mx=0




for i in range(1,lcm,1):
    if timeline[i]!= timeline[i-1]:
        mx=i
        print(mn," ",mx," ",timeline[i-1],"             (",mx-mn," seconds)",sep="")
        mn=i
    if i ==lcm-1 and mn != timeline[i]:
        mx =i+1
        print(mn," ",mx," ",timeline[i-1],"             (",mx-mn," seconds)",sep="")
  
    #print("[",i,"]",timeline[i]," ",sep="",end="")
