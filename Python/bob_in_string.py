s = 'azcbobobegghakl'
x = 'bob'
count = 0

while True:
    y = s[:3]
    if x in y:
        count += 1
    s = s[1:]
    if len(s) < 3:
        break
print("Number of times bob occurs is: ", count)
