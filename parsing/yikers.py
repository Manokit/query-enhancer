import sys 

arg1 = ''

for i in sys.argv:
    arg1.join([i]).join(" ")
print(arg1)