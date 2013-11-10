##
#   NAAM    : Maico Timmerman
#   CKNUM   : 10542590
#   Studie  : Informatica
#
#   ls.py
#       This program implements 2 classes, Fraction and Complex Faction.
#       Both classes have overloaded functions for +, -, *, /, ** and 
#       can be reversed.
##

from graphics import *
from math import sin, cos, pi

class LS:
    """The Lindenmayer System"""
    def __init__(self, defstep, defangle):
        """Initialize all LS attributes"""
        self.defstep = defstep
        self.defangle = defangle
        self.axiom = ''
        self.rules = {}

    def setAxiom(self, ax):
        """Set the axiom"""
        self.axiom = ax

    def addRule(self, letter, word):
        """Add a rule to the set of rules"""
        self.rules[letter] = word

    def generate(self, n):
        """Generate the word by applying the rules n times"""
        startWord = self.axiom
        for i in range(0,n):
            newWord = ''
            for c in startWord:
                if c in self.rules:
                    newWord += self.rules[c]
                else:
                    newWord += c
                startWord = newWord
        return startWord


    def __repr__(self):
        """Generate a string representing the LS"""
        #
        # for this class just printing the constructor is not enough:
        # the axiom and rules are added later. These have to be printed as
        # well. You could return as a string the Python code that would reconstruct
        # the LS class instantiation WITH the axiom and the rules.
        #
        # This method is not obligatory for this course but you are strongly
        # encouraged to give it a try. It also helps when you need to debug your
        # code.
        #
        rString = 'LS({},{})\n'.format(self.defstep, self.defangle) 
        rString += 'ls.setAxiom(\'{}\') \n'.format(self.axiom)
        rString += 'ls.addRule(\'{}\')\n'.format(self.rules)
        return rString


class TurtleState:
    """The state of the turtle. This is needed so we can push one object on the stack
    that contains: the position of the turtle, its orientation, the actual stepsize and
    the actual width of the lines to be drawn"""
    def __init__(self, pos, step, angle, width):
        self.pos = pos
        self.stepSize = step
        self.angle = angle
        self.width = width

    def clone(self):
        """return a clone of the state."""
        return TurtleState(Point(self.pos.getX(), self.pos.getY()), self.stepSize, self.angle, self.width)

    def __repr__(self):
        """really easy when debugging"""
        rString = 'Pos: {},{},\n'.format(self.pos.getX(), self.pos.getY())
        rString += 'Step: {},\nAngle: {},\nWidth: {}'.format(self.stepSize, self.angle, self.width)
        return rString


class Stack:
    def __init__(self):
        """create Stack with list"""
        self.stack = []

    def __str__(self):
        """print stack"""
        return self.stack.__str__()

    def push(self,item):
        """add an item at the end of the list"""
        self.stack.append(item)

    def pop(self):
        """remove and return the last item in the list"""
        return self.stack.pop()

    def emtpy(self):
        """Not really used!"""
        del self.stack[:]

    def isEmpty(self):
        """Not really used!"""
        if self.stack == []:
            return True
        else:
            return False

def parseWord(word, startIndex):
    wordLength = len(word)
    par = ''
    """test if the index exists for the letter"""
    if wordLength > startIndex:
        c = word[startIndex]
    else:
        c = None
    """test is the index for the next letter and ( exists"""
    if wordLength > (startIndex + 1):
        if (word[startIndex + 1]) == '(':
            i = 1
            while True:
                if word[startIndex + i + 1] != ')':
                    """keep adding letters till the ) is found"""
                    par = par + word[startIndex + 1 + i]
                    i+=1
                else:
                    pastIndex = startIndex + i + 2
                    break
            par = float(par)
        else:
            par = None
            pastIndex = startIndex + 1
    else:
        par = None
        pastIndex = -1
    return c, par, pastIndex

class Turtle:
    def __init__(self, win, defwidth):
        """initialize a turtle with a default with and a window to draw on"""
        self.defwidth = defwidth
        self.win = win
        self.stack = Stack()

    def stepPenUp(self, none):
        """make a step without making a line"""
        self.step(False)

    def stepPenDown(self, none):
        """make a step while making a line"""
        self.step(True)

    def step(self, isPenDown):
        """make a step with/without a line on the path travelled"""
        dx = self.stepSize * int(cos(self.currentAngle))
        dy = self.stepSize * int(sin(self.currentAngle))
        self.newPos = Point(self.pos.x + dx, self.pos.y + dy)
        if isPenDown:
            line = Line(self.pos, self.newPos)
            line.setWidth(self.defwidth)
            line.draw(self.win)
            self.pos = self.newPos
        else:
            self.pos = self.newPos

    def left(self, none):
        """action associated with +"""
        self.currentAngle = self.currentAngle - self.turnAngle

    def right(self, none):
        """action associated with -"""
        self.currentAngle = self.currentAngle + self.turnAngle

    def scale(self, scale):
        """action associated with \"(scale) """
        self.defwidth = self.defwidth * scale
        self.stepSize = self.stepSize * scale

    def push(self, none):
        """action associated with ["""
        self.stack.push(TurtleState(Point(self.pos.x, self.pos.y),
                 self.stepSize, self.currentAngle, self.defwidth))

    def pop(self, none):
        """action associated with ]"""
        self.state = self.stack.pop().clone()
        """set all var back to before the branch"""
        self.currentAngle = self.state.angle
        self.pos = self.state.pos
        self.defwidth = self.state.width
        self.stepSize = self.state.stepSize
        self.pos = self.state.pos

    def drawLS(self, lsys, n, startx, starty, startangle):
        """Draw the Lindenmayer system (lsys) after n iterations
        startx, starty are the starting position on the window
        startangle is the starting angle"""
        self.currentAngle = startangle
        self.turnAngle = lsys.defangle
        self.pos = Point(startx, starty)
        self.stepSize = lsys.defstep
        self.drawAxiom = lsys.generate(n)
        self.nextIndex = 0
        self.functions = {'F': self.stepPenDown,
                          'f': self.stepPenUp,
                          '\"':self.scale,
                          '+': self.left,
                          '-': self.right,
                          '[': self.push,
                          ']': self.pop}
        while self.nextIndex <= len(self.drawAxiom) and self.nextIndex != -1:
            self.c,self.par,self.nextIndex = parseWord(self.drawAxiom, self.nextIndex)
            if self.c in self.functions:
                self.functions[self.c](self.par)

            



if __name__=='__main__':
    win = GraphWin('Lindenmayer System', 400, 400)
    win.yUp()

    ls = LS(3,pi/2) 
    ls.setAxiom('F-F-F-F')
    ls.addRule('F','F-F+F+FF-F-F+F')

    print 'ls:'
    print ls

    t = Turtle(win, 1)
    t.drawLS(ls, 3, 100, 100, 0)

    tree = LS(80,pi/2)
    tree.setAxiom('"(1.5)FFA')
    tree.addRule('A', '"(0.687)[+FA][-FA]')

    print 'tree:'
    print tree

    t.defwidth = 12
    t.drawLS(tree, 10, 200, 30, pi/2)

    win.promptClose(win.getWidth()/2,20)
