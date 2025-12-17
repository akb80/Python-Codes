s=input("Enter a string: ")
vow=0
conso=0
dig=0
special=0
for ch in s:
    if ch in "aeiou":
        vow+=1
    elif ch.isdigit():
        dig+=1
    elif ch.isalpha():
        conso+=1
    else:
        special+=1
print("vowels,consonents,digits,special char:",vow,special,dig,special)