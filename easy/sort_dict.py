details = {}

n = int(input("Number of entries : "))

for i in range(n):
    name = input("Enter name: ")
    print("Enter marks : ")
    marks = list(map(int, input().split(' ')))
    details[name] = marks

for i in sorted(details, key=lambda x: sum(details[x])):
    print(i, details[i], sum(details[i]))
