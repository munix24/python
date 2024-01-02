x_wins=0
y_wins=0

x_roll=100
y_roll=50

x_win_guarantee=(x_roll - y_roll)
x_50_50=(y_roll / 2)
x_win_chance=x_win_guarantee+x_50_50
print(x_win_chance)

for x in range(x_roll):
    for y in range(y_roll):
        if(y>x):
            y_wins+=1
        elif(x>y):
            x_wins+=1
        #print(x, y, x_wins, y_wins)

print(x_wins)
print(y_wins)
print(x_wins/(x_wins+y_wins))
