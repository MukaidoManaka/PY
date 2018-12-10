import collections

filename = input('Input filename :')
with open(filename) as info:
    str = info.read()
    biaodian = str.lower().replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ')
    print(biaodian)
    str2 = biaodian.split(' ')

    counter = collections.Counter(str2)
    print(counter)

    max = 0
    max_name = []
    for val in counter:
        if counter[val] > max:
            max = counter[val]
            max_name = []
            max_name.append(val)
        elif counter[val] == max:
            max_name.append(val)
print('出现次数最多的单词是：')
for val in max_name:
    print(val)