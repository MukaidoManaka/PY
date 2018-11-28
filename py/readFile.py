
f = open("../yome.txt")
line = f.readline()
while line:
    print(line)
 #   line = f.readline()    wocao,飞起来了
f.close()


"""
f = open("../yome.txt")
for line in open("../yome.txt"):
    print(line)
"""

'''
f = open("../yome.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
'''

