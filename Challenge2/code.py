# Working hours of person 1
wt1 = ["9:00", "20:00"]
#Meetings of person 1
cal1 = [["9:00","10:30"],["12:00","13:00"],["16:00","18:00"]]
#Working hours of person 2
wt2=["10:00","18:30"]
#Meetings of person 2
cal2=[["10:00","11:30"],["12:30","14:30"],["14:30","15:00"],["16:00","17:00"],["17:00","18:00"]]
#List of possible hours
strt=["0:00","0:30","1:00","1:30","2:00","2:30","3:00","3:30","4:00","4:30","5:00","5:30","6:00","6:30","7:00","7:30",
      "8:00","8:30","9:00","9:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30","14:00","14:30","15:00","15:30",
      "16:00","16:30","17:00","17:30","18:00","18:30","19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30"]
#Find common working hours
if int(wt1[0].split(":")[0])<int(wt2[0].split(":")[0]) or (int(wt2[0].split(":")[0])==int(wt2[0].split(":")[0]) and int(wt2[0].split(":")[1])>=int(wt2[0].split(":")[1])):
    strt=strt[strt.index(wt2[0]):]
else:
    strt=strt[strt.index(wt1[0]):]
if int(wt1[0].split(":")[1])<int(wt2[0].split(":")[1]) or (int(wt2[0].split(":")[1])==int(wt2[0].split(":")[1]) and int(wt2[1].split(":")[1])>=int(wt2[1].split(":")[1])):
    strt=strt[:strt.index(wt2[1])+1]
else:
    strt=strt[:strt.index(wt1[1])+1]
#Add meetings to common list
cale=cal1+cal2
#Find common "Busy" hours
for j in range(0,len(cale)):
    for i in range(0, len(cale)-1):
        if(cale[i][1]==cale[i+1][0]):
            cale[i][1]=cale[i+1][1]
            cale[i + 1][0]=cale[i + 1][1]="d"
cale=[value for value in cale if value != ["d","d"]]
#Find hours for meetings
for j in range(0,len(cale)):
    inth1=int(cale[j][0].split(":")[0])
    intm1=int(cale[j][0].split(":")[1])
    inth2 = int(cale[j][1].split(":")[0])
    intm2 = int(cale[j][1].split(":")[1])
    try:
        i=0
        while i < len(strt):
            valh=int(strt[i].split(":")[0])
            valm = int(strt[i].split(":")[1])
            if (((valh == inth1 and valm > intm1) or (valh>inth1)) and ((valh == inth2 and valm < intm2) or (valh<inth2))):
                strt.remove(strt[i])
            else: i+=1
    except:
       pass
val=[int(strt[0].split(":")[0]),int(strt[0].split(":")[1])]
#Make it looks more nicely
i=1
strp=[]
while i<=len(strt):
    if(i==len(strt)):
        if(strt[0]!=strt[i - 1]):
            strp.append([strt[0], strt[i - 1]])
        break
    cale = [int(strt[i].split(":")[0]), int(strt[i].split(":")[1])]
    if(val[0]==cale[0]):
        val=cale
        i+=1
    elif(val[0]+1 == cale[0] and val[1]!=cale[1]):
        val = cale
        i += 1
    else:
        strp.append([strt[0],strt[i-1]])
        strt=strt[i:]
        val = cale
        i=1
print(strp)