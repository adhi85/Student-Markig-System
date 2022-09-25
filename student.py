print('Enter number of students')
num=input()
num=int(num)

students=[dict() for x in range(num)]

for i in range(num):
    print('Enter name')
    nam=input()
    students[i]['Name']=nam
    print('Enter Roll n.o')
    rno=int(input())
    students[i]['RollNo']=rno
    print('Enter Marks as a list')
    temp = input()
    Mrk=[]
    for k in range(len(temp)):
        if(temp[k]=='[' or temp[k]==']' or temp[k]==','):
            continue
        else:
            Mrk.append(temp[k])
    for j in range(len(Mrk)):
        Mrk[j]=int(Mrk[j])
    students[i]['Marks']=Mrk
    
print("\nmenu\na)Details of all the students\nb)sum of all marks in descending order\nc)student with maximum mark")
print("d)student with minimum mark\ne)student who is having average mark\nf)exit")    

option='z'
while option!='f':
    option=input("\nEnter the option\n")
    if(option=='a'):
       for i in range(num):
           print("Name:",students[i]['Name'])
           print("Roll number:",students[i]['RollNo'])
           print("Marks:",end='')
           print(*students[i]['Marks'],sep=',')
    
    elif(option=='b'):
        summark=[]
        for i in range(num):
            summark.append(sum(students[i]['Marks']))
        summark.sort(reverse=True)
        print(*summark,sep=',')
            
    elif(option=='c'):
        summark=[]
        for i in range(num):
            summark.append(sum(students[i]['Marks']))
            
        for i in range(num):
            if(summark[i]==max(summark)):
                print("student name:",students[i]['Name'])
                print("mark:",summark[i])
                break;
    
    elif(option=='d'):   
        summark=[]
        for i in range(num):
            summark.append(sum(students[i]['Marks']))
        
        for i in range(num):
            if(summark[i]==min(summark)):
                print("student name:",students[i]['Name'])
                print("mark:",summark[i])
                break;    
    
    elif(option=='e'):         
        summark=[]
        for i in range(num):
            summark.append(sum(students[i]['Marks']))
        
        for i in range(num):
            if(summark[i]==sum(summark)/num):
                print("student name:",students[i]['Name'])
                print("mark:",summark[i])
                break;
            else:
                print("student name:no student")
                
    else:
        break;
            
# CREDIT : https://github.com/adhi85/
