#code
n = int(input())
dic1 = {}


def process(s):
    
    def check(l):
        if l[0]==-1:
            l=l[1:]
        if l[len(l)-1]==-1:
            l=l[:len(l)-1]
        for i in l:
            if i!=0:
                return False
        return True
                
    s=s.strip().lower().split()
    screen=s[1].strip()
    if s[0].strip()=='add-screen':
        if dic1.get(screen, None) is not None:
            print("failure")
            return
        
        if len(s)>4:
            aisle=set(map(lambda x: int(x)-1, s[4:]))
        else:
            aisle=set()
        
        dic1[screen]=[[-1 if i in aisle else 0 for i in range(int(s[3]))] for j in range(int(s[2]))]
        print("success")
        # when does it fails

    elif s[0].strip()=='reserve-seat':
        row=int(s[2])-1
        seats=list(map(lambda x: int(x)-1, s[3:]))
        suc=True
        # print(dic1[screen][row])
        for i in seats:
            if dic1[screen][row][i]==1:
                suc=False
                break
        if suc:
            print("success")
            for i in seats:
                dic1[screen][row][i]=1
        else:
            print("failure")
    elif s[0].strip()=='get-unreserved-seats':
        row=int(s[2])-1
        st=""
        for i in range(len(dic1[screen][row])):
            if dic1[screen][row][i]<1:
                st+="{} ".format(i+1)
        print(st.strip())
    else:
        num=int(s[2])
        row=int(s[3])-1
        ch=int(s[4])-1
        if num==1:
            if dic1[screen][row][ch]<1:
                print(ch+1)
            else:
                print("none")
            return
        
        if ch+num<len(dic1[screen][row]) and check(dic1[screen][row][ch:ch+num]):
            print(" ".join(map(str, range(ch+1, ch+num+1))))
        elif ch-num>=0 and check(dic1[screen][row][ch-num+1:ch+1]):
            print(" ".join(map(str,range(ch-num+1+1, ch+1+1))))
        else:
            print("none")
            
# comm=[]
for i in range(n):
    # comm.append(input())
# raise Exception(comm)
    x = input()
    process(x)