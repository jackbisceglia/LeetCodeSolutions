s = "  hello world!  "


new = ""
chopped = s.split(" ")[::-1]
copy = chopped.copy()

for i in chopped:
    if i == '':
        copy.remove(i)

print(copy)

manip = ''
for i in range(len(copy)):
    if i != len(copy) - 1:
        manip += copy[i] + ' '

    else:
        manip += copy[len(copy) - 1]

print(manip)

