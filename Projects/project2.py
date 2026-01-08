soccer_points = 0
basketball_points = 0
hockey_points = 0
anwser1 = input ("Do you A prefer to play year round or B play in the winter C play in the fall") 
if anwser1 == "A" or anwser1 == "a":
    soccer_points += 1
elif anwser1 == "B" or "b":
    basketball_points += 1
elif anwser1 == "C" or "c": 
    hockey_points += 1
anwser2 = input ("Do you A like playing sports with your feet or B  like playing sports with your hands C like playing with something else in your hand")
if anwser2 == "A":
    soccer_points += 1
elif anwser2 == "B":
    basketball_points += 1
elif anwser2 == "C":
    hockey_points += 1
anwser4 = input ("do you prefer to play on A field B court C Ice")
if anwser4 == "A":
    soccer_points += 1
elif anwser4 == "B":
    basketball_points += 1
elif anwser4 == "C":
    hockey_points += 1
anwser5= input ("do you perfer to play with A light padding B no padding C heavy padding")
if anwser5 == "A":
    soccer_points += 1
elif anwser5 == "B":
    basketball_points += 1
elif anwser5 == "C":
    hockey_points += 1
if soccer_points > basketball_points and soccer_points > hockey_points:
    print("You should play soccer! You have a lot in common with soccer players!")
elif basketball_points > soccer_points and  basketball_points > hockey_points:
    print("You should play basketball you have a lot in common with basketball players")
elif hockey_points > soccer_points and  hockey_points > basketball_points  :
    print("You should play hockey you have a lot in common with hockey players")