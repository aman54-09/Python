from urllib.request import urlopen
file=urlopen("https://www.w3.org/")
#print(file.read())

from bs4 import BeautifulSoup
#soup=BeautifulSoup(file)
#print(soup.title)
#print(soup.title.string)

soup=BeautifulSoup(file, "html.parser")
for script in soup(["script","style"]):
    script.extract()
    
text=soup.get_text()
lines=(line.strip() for line in text.splitlines())
#print(lines)

#for line1 in lines:
#   print (line1)

list_word1=[]
for word in lines:
    for word in lines:
        word=word.split()
        list_word1.extend(word)

#print(list_word1)        

list_word2=[]
import re
pattern=re.compile(r'(?<!\S)[A-Za-z]+(?!\S)')
for word in list_word1:
    matchObject=pattern.match(word)
    if(matchObject):
        list_word2.append(matchObject.group().lower())
#print(list_word2)


ignore_list=[]
#compare wuth ignore list andf deleting the words
with open('ignore.txt','r') as file2:
    data=file2.readlines()
    for lines in data:
        for x in lines.split():
            ignore_list.append(x.lower())

list_word2.sort()
#print(list_word2)

Dict_word={}

for word in list_word2:
    cnt=list_word2.count(word)
    Dict_word[word]=cnt

#print(Dict_word)    

for word in ignore_list:
    if word in Dict_word:
        del Dict_word[word]

print('_'*50)
print(Dict_word)
# database coding

#database Coding
#starting database connection
import sqlite3
conn = sqlite3.connect('mydb.db')
print("open database success")
#creating a neaw table
conn.execute("drop table if exists word")
conn.execute('''CREATE TABLE WORD(WORD TEXT NOT NULL,COUNT INT NOT NULL);''')
print("table created successfully")
#inserting records in table
for word,count in Dict_word.items():
    count = str(count)
    c ="INSERT INTO WORD VALUES('"+word+"',"+count+");"
    conn.execute(c)
conn.commit()
print("record created successfully")
cur=conn.execute("select* from word")
for row in cur:
    print(row[0],' : ',row[1])
conn.close()

A={}
import operator
A=dict(sorted(Dict_word.items(),key=operator.itemgetter(1),reverse=True)[:10])

print (A)

import xlsxwriter
workbook=xlsxwriter.Workbook('word.xlsx')
worksheet=workbook.add_worksheet()
worksheet.set_column('A:A',30)
bold=workbook.add_format({'bold': True})
worksheet.write('A1', 'WORDS', bold)
worksheet.write('B1', 'WORDS', bold)

row=1
col=0

for word,count in A.items():
    worksheet.write(row, col, word)
    worksheet.write(row, col+1, count)
    row += 1
    chart = workbook.add_chart({'type': 'column'})
    chart.set_x_axis({
        'name': 'Words',
        'name_font':{'size':14, 'bold': True},
        'num_font': {'italic': True},
})

chart.set_y_axis({
    'name': 'frequency',
    'name_font': {'size': 14, 'bold' : True},
    'num_font': {'italic': True},
})

chart.add_series({'values': '=Sheet1!$B$2:$B$11',
                  'categories': '=Sheet1!$A$2:$A$11'})
worksheet.insert_chart('D2', chart)

workbook.close()
#Displaying ignore.txt.
