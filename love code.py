print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
t = (lower_name1+lower_name2).count('t')
r = (lower_name1+lower_name2).count('r')
u = (lower_name1+lower_name2).count('u')
e = (lower_name1+lower_name2).count('e')
total_wordtrue = t+r+u+e
l = (lower_name1+lower_name2).count('l')
o = (lower_name1+lower_name2).count('o')
v = (lower_name1+lower_name2).count('v')
e = (lower_name1+lower_name2).count('e')
total_wordlove = l+o+v+e
result_score = str(total_wordtrue)+str(total_wordlove)
score = int(result_score)
if score < 10 or score > 90:
    print(f'"Your score is {score}, you go together like coke and mentos."')
elif score > 40 and score < 50:
    print(f'"Your score is {score}, you are alright together."')
else:
    print(f'"Your score is {score}."')