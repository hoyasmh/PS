s = "121"
while len(s) <= 80:
    s = s + "3" + s
print(s[:int(input())])