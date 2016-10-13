number=input("Enter a number:")
word=input("Enter a word: ")
fe="ves"
y="ies"
sh="es"
ch="es"
us="i"
twoy="s"
if word[-2:]=="fe":
    print(number +" "+ word[0:-2]+fe)
elif word[-1:]=="ies":
    print(number +" "+ word[0:-2]+ies)
elif word[-2:]=="sh":
    print(number +" "+ word[0:-2]+sh)
elif word[-2:]=="ch":
    print(number +" "+ word[0:-2]+ch)
if word[-2:]=="us":
    print(number +" "+ word[0:-2]+ch)
if word[-2:]=="ay":
    print(number +" "+ word[0:-2]+twoy)
if word[-2:]=="oy":
    print(number +" "+ word[0:-2]+twoy)
if word[-2:]=="ey":
    print(number +" "+ word[0:-2]+twoy)
if word[-2:]=="uy":
    print(number +" "+ word[0:-2]+twoy)
else:
    print(number +" "+ word+"s")