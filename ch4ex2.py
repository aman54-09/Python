"""def sum (a,b):
    return a+b
L1=[1,2,3]
L2=[5,6,7]
L=[x for x in map (sum, L1, L2)]
print(L)

nlist=["Anurag","deepti","jack","hina"]
mlist=[56,39,49,84]
for x in zip (nlist, mlist):
    print (x)

def odd (a):
    if a%2!=0:  return True
    else: return False

L1=[4,3,5,6,2,7,11,23,48,98]
L=[x for x in filter (odd,L1)]    # odd is the function name
print (L)          # select odd values from  the list 

square = lambda d:d*d
cube = lambda f:f*f*f
fifth = lambda h:h*h*h*h*h
print (square(6))
print (cube(8))
print (fifth(2))


def even (a):
    if a%2==0:  return True
    else: return False

l2 = [1,3,4,5,8,90,3,6]
l = [x for x in filter(lambda a: a%2==0, l2)]
print (l)"""


"""fo=open("article.txt","w")
fo.write("Certainly! Here are some of the top news headlines from today:Delhi Court Rejects Arvind Kejriwal’s Plea for Regular Video Consultation with Doctor: A Delhi court has rejected the plea by jailed Delhi Chief Minister Arvind Kejriwal seeking regular video consultations with his doctor. An AIIMS panel will now decide on his insulin needs1")
fo.close()

fo=open("ignore.txt","r")
fo.read("of, for, are, the, a, on")
s1=fo.readline()

print(s1)"""

"""l1=[]
with open("article.txt","r") as file:
    data=file.readlines()

    for line in data:
        w=line.split()
        l1.append(w)
        print(line)

print(l1)    # print list with subtitle

dict={}
l1.sort()
for list1 in l1:
    for word in list1:
        del ignore.txt["for, of, are, the, a, on"]
print("-"*10)
print(del)"""

fo = open("article.txt", "w")
fo.write("Certainly! Here are some of the top news headlines from today: Delhi Court Rejects Arvind Kejriwal's Plea for Regular Video Consultation with Doctor: A Delhi court has rejected t")
fo.close()

fo = open("ignore.txt", "r")
fo.read("of, for, are, the, a, on")
sl = fo.readline()
print(sl)

data = []
with open("article.txt", "r") as file:
    for line in file:
        words = line.split()
        data.append(words)

print(line)
print(data)

# print list with subtitle
ignore.txt={}
for line in l1:
    for word in list1:
        del ignore.txt["for, of, are, the, a, on"]
print("-"*10)
print(ignore.txt)     
