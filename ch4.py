l1=[]
with open("abc.txt","r") as file:
    data=file.readlines()

    for line in data:
        w=line.split()
        l1.append(w)
        print(line)

print(l1)

l2=[]
for list1 in l1:
    for word in list1:
        l2.append(word)
print("-"*30)
print(l2)
