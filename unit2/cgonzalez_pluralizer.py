#varibles
number=input("Enter a number:")
word=input("Enter a word: ")
fe_ending="ves"
y_ending="ies"
sh_ending="es"
ch_ending="es"
us_ending="i"
s_ending="s"
#if, elif, and else statements
if number=="1":
    print(number+" "+word)
elif word[-2:]=="fe":
    print(number +" "+ word[0:-2]+fe_ending)
elif word[-2:]=="oy":
    print(number +" "+ word+s_ending)
elif word[-2:]=="sh":
    print(number +" "+ word[0:-2]+sh_ending)
elif word[-2:]=="ch":
    print(number +" "+ word[0:-2]+ch_ending)
elif word[-2:]=="us":
    print(number +" "+ word[0:-2]+ch_ending)
elif word[-2:]=="ay":
    print(number +" "+ word+s_ending)
elif word[-2:]=="ey":
    print(number +" "+ word+s_ending)
elif word[-2:]=="uy":
    print(number +" "+ word+s_ending)
elif word[-1:]=="y":
    print(number +" "+ word[0:-1]+y_ending)
else:
    print(number +" "+ word+"s")
 
 