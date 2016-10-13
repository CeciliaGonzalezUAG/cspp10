number=input("Enter a number:")
word=input("Enter a word: ")
fe="ves"
y="ies"
sh="es"
ch="es"
us="i"
s="s"

if number=="1":
    print(number+" "+word)
elif word[-2:]=="fe":
    print(number +" "+ word[0:-2]+fe)
elif word[-2:]=="oy":
    print(number +" "+ word+s)
elif word[-2:]=="sh":
    print(number +" "+ word[0:-2]+sh)
elif word[-2:]=="ch":
    print(number +" "+ word[0:-2]+ch)
elif word[-2:]=="us":
    print(number +" "+ word[0:-2]+ch)
elif word[-2:]=="ay":
    print(number +" "+ word+s)
elif word[-1:]=="y":
    print(number +" "+ word[0:-1]+y)
elif word[-2:]=="ey":
    print(number +" "+ word+s)
elif word[-2:]=="uy":
    print(number +" "+ word+s)
else:
    print(number +" "+ word+"s")