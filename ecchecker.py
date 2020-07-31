import sys

if len(sys.argv) != 2:
    print('Invalid Arguments')
    sys.exit(-1)
   
my_work = []
correct = []
with open(sys.argv[1],'r') as fn:
    for l in fn:
        item = l.strip().split()
        my_work.append((item[2],item[7]))

with open('correct.txt','r') as fnco:
    for l in fnco:
        item  = l.strip().split()
        correct.append((item[2],item[7]))

for my_answer, correct_answer in zip(my_work, correct):
    if(my_answer != correct_answer):
        print('Values are different!')
        sys.exit(-1)
print('Values are the same!')