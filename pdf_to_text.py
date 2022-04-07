from sys import is_finalizing
import PyPDF2
 
#create file object variable
#opening method will be rb
pdffileobj=open('data.pdf','rb')
print(pdffileobj)
#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)
print(pdfreader)
#This will store the number of pages of this pdf file
x=pdfreader.numPages
print(x)
#create a variable that will select the selected number of pages
pageobj=pdfreader.getPage(x-1)
 
#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
# text=pageobj.extractText()
# print(text)
#save the extracted data from pdf to a txt file
#we will use file handling here
#dont forget to put r before you put the file path
#go to the file location copy the path by right clicking on the file
#click properties and copy the location path and paste it here.
#put "\\your_txtfilename"

file1=open(r"1.txt","a")
total = []
text2 = ""
for i in range(0,x):
    pageobj = pdfreader.getPage(i)
    text = pageobj.extractText()
    a = pageobj.getContents()
    print(a)
    # print(text,i)
    text2+=text
    total.append(text)
# print(total)

#preprocessing to make the data accessible
for i in range(x):
    total[i] = total[i].replace("ID: ","ID:")


temp = total
transactions = []
gross = []
# print(temp)
for each in text2.split("Page"):
    print(each,"\n\n\n\n")
    each = each.replace("ID :","ID:")
    gross.append("Page "+each)
    
    for pg in each.split("ID:"):
        print(pg)
        transactions.append("ID:"+pg)
        print("*"*10+"\n\n\n")
print(len(total))
file1.writelines(total)
file1.close()

with open("gross.txt","w") as f:
    f.writelines('\n'.join(gross) + '\n')
print(transactions)
with open("transactions.txt","w") as f:
    f.writelines('\n'.join(transactions) + '\n')

