from graphics import *
win = GraphWin("Test", width = 700, height = 700) # create window
win.setBackground(color='black')
win.setCoords(0, 0, 10, 10) # window coords; bottom left is (0, 0) and top right is (10, 10)

pl_pos_x = 5
pl_pos_y = 5

enemies=[]

class Unit():
    movement = 0

player = Rectangle(Point(0, 0), Point(.2760349, .5558807)).draw(win) 
player.setOutline('green')
player.setFill('green')
player.move(pl_pos_x, pl_pos_y)

enemy = Rectangle(Point(0, 0), Point(0.3225, 0.3225)).draw(win)     #set outline to red in graphics.py so you don't have to set it here
enemy.move(5, 5)

while True:
    win.getMouse()
    player.move(1, 1)
win.getMouse()

##5 hp
##2 edps
##
##100 hp
##5 minutes
##
##how fast should enemies increase mvmt speed/hp?
