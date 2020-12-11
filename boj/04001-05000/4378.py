t=str.maketrans("1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./","`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.")
s=input()
while s:
    s+=s
    s=input()
print(s.translate(t))
