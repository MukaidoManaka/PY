import csv
# 成绩最高的人的学号以及哪个班级的人最多

with open('scores.csv') as r:
    reader = csv.reader(r)
    rows = [row for row in reader]
    # column_scores = [column[2] for column in reader]  不起作用
    

with open('scores.csv') as c:
    reader2 = csv.reader(c)
    column_scores = [column[2] for column in reader2]

with open('scores.csv') as clas:
    reader3 = csv.reader(clas)
    column_class = [column[1] for column in reader3]

print(rows)
print(column_scores)
print(column_class)

scores = [int(score) for score in column_scores]
classes = [int(i) for i in column_class]

print(scores)
print(classes)

maxScoresName = []
maxScores = max(scores)
for j in rows:
    for k in j:
        if int(k) == maxScores:
            maxScoresName.append(j[0])

print("分最高的人的学号是：")
for a in maxScoresName:     #  1
    print(a)

aki = {}
for b in classes:
    if not (b in aki.keys()):
        aki[b] = 1
    else:
        aki[b] += 1

print(aki)

haofan = []
_max = 0
for ak in aki:          #2
    if aki[ak] > _max:
        _max = ak
        haofan = []
        haofan.append(ak)
    if aki[ak] == _max:
        haofan.append(ak)

print(haofan)

print('人数最多的班级是:')
for h in haofan:
    print(h,'班')