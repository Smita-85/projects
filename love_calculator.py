#CALCULATING THE PERCENTAGE OF LOVE(....MINI LOVE CALCULATOR....)
name_1=input("enter first name:")
name_2=input("enter second name:")
combined_string=name_1+name_2
lower_case_string=combined_string.lower()
t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t +r +u +e
l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=l +o +v +e
love_score=int(str(true)+str(love))
if love_score>10 and love_score<=90:
     print("your score is:",love_score)
     print("you both are like romie and juliet")
elif love_score>=40 and love_score<=50:
    print("your score is:",love_score)
    print("you are alright together")
else:
    print("your score is:",love_score)
