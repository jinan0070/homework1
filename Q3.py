infile = open ('j.txt','r')
ques_and_answ = [x.rstrip() for x in infile]
c = 0
for i in ques_and_answ :
    print (i[ :i.index("=")+1])
j = input ('enter message')
if a == i [i.index("=")+1]:
    c+=1
name = input ('enter name')
print (name,c)
outfile = open ('j.txt','w')
outfile = write (name +str(c))
outfile.close()
infile.close()