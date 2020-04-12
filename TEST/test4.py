input = open("input.txt", "r").readline

n = int(input())
classes = {}
for i in range(n):
    s = input()
    if s.find(':') != -1:
        key, value = s.split(':')
        key = key.strip()
        value = value.strip().split()
        if key not in classes:
            classes[key] = []
            for i in value:
                classes[key].append(i)
        else:
            for i in value:
                classes[key].append(i)
    else:
        classes[s.strip()] = []

# print(classes)
# classes = {'d': ['b', 'c'], 'a': [], 'c': ['a'], 'b': ['a'], 'e': ['d']}
# print(classes)


for k, v in classes.items():
    for k2, v2 in classes.items():
        if k in v2:
            v2 += v


print(classes)
for _ in classes:
    print(_, ':', classes[_])


m = int(input())
for k in range(m):
    c = input().split()
    if len(c) == 2:
        class1, class2 = c
        if class1 in classes and class2 in classes:
            if class1 == class2:
                print('Yes')
            elif class1 in classes[class2]:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
