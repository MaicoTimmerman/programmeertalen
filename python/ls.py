# test
#  PUT SOME INFO HERE.... (who you are and what is in this file)
#
#

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
        self.step = step
        self.angle = angle
        self.width = width

    def clone(self):
        """return a clone of the state."""
        return TurtleState(Point(self.pos.getX(), self.pos.getY()), self.step, self.angle, self.width)

    def __repr__(self):
        """really easy when debugging"""
        rString = 'Pos: {},{},\n'.format(self.pos.getX(), self.pos.getY())
        rString += 'Step: {},\nAngle: {},\nWidth: {}'.format(self.step, self.angle, self.width)
        return rString


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return self.stack.__str__()

    def push(self,item):
        self.stack.append(item)

    def pop(self):
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
    c, par, pastIndex
    wordLength = len(word)
    if wordLength <= startIndex:
        c = word[startIndex]
    else:
        c = None
    if wordLength <= (startIndex + 1):
        if (word[startIndex + 1]) == '(':
            i = 1
            while True:
                if word[startIndex + i + 1] != ')':
                    par = par.word[startIndex + 1 + i]
                else:
                    pastIndex = word[startIndex + i + 1]
                    break
        else:
            pastIndex = word[startIndex + 1]
    else:
        par = None
        pastIndex = -1
    return c, par, pastIndex

class Turtle:
    def __init__(self, win, defwidth):
        self.defwidth = defwidth
        self.win = win
        self.stack = Stack()

    def stepPenUp(self):
        self.step(False)

    def stepPenDown(self):
        self.step(True)

    def step(self, isPenDown):
        dx = self.step * int(cos(self.currentAngle))
        dy = self.step * int(sin(self.currentAngle))
        newPos = Point(self.pos.getX() + dx, self.pos.getY() + dy)
        if isPenDown:
            line = Line(self.pos, self.newPos)
            line.setWidth(self.currentWidth)
            line.draw(self.win)
            self.pos = self.newPos
        else:
            self.pos = self.newPos

    def left(self):
        """action associated with +"""
        self.currentAngle -= turnAngle

    def right(self):
        """action associated with -"""
        self.currentAngle += turnAngle

    def scale(self, scale):
        """action associated with \"(scale) """
        self.currentWidth *= scale

    def push(self):
        """action associated with ["""
        stack.push(TurtleState(Point(self.pos.getX(), self.pos.getY),
                 self.step, self.currentAngle, self.currentWidth))

    def pop(self):
        """action associated with ]"""


    def drawLS(self, lsys, n, startx, starty, startangle):
        self.currentAngle = startangle
        self.turnAngle = lsys.defangle
        self.pos = Point(startx, starty)
        self.step = lsys.defstep
        self.drawAxiom = lsys.generate(n)
        """Draw the Lindenmayer system (lsys) after n iterations
        startx, starty are the starting position on the window
        startangle is the starting angle

        This function does the interpretation of the LS string (you are give
        the LS object and the required number of iterations).
        Loop over characters in the generated string using the parseWord function. Every
        call to parseWord will return three values c,par,pastindex.
        Decide what to do for every character c (and use the right argument if 
        an argument was given and found in the string).

        This is also the function where you need the Stack class. When
        you encounter the '[' character you have to push the state and
        when you encounter the ']' character you have to pop a state
        from the stack.

        Please be aware not to push a reference to the state on the
        stack (you will be overwriting it). I advise to have a method
        clone in the State class that really makes a new state object
        that you can safely push on the stack.

        """
        pass



if __name__=='__main__':
    #
    # the following code is what is used to test the default
    # implementation. Running this code shows two Lindemayer systems
    # in one window
    #
    win = GraphWin('Lindenmayer System', 400, 400)
    win.yUp()

    ls = LS(3,pi/2) #step 3, angle:90 degree
    ls.setAxiom('F-F-F-F')
    ls.addRule('F','F-F+F+FF-F-F+F')

    print ls  # in the 'default' implementation this would print something like
              # the three lines above

    t = Turtle(win, 1)
    t.drawLS(ls, 100, 100, pi/2)

    tree = LS(80,pi/2)
    tree.setAxiom('"(1.5)FFA')
    tree.addRule('A', '"(0.687)[+FA][-FA]')

    t.defwidth = 12
    t.drawLS(tree, 10, 200, 30, pi/2)

    win.promptClose(win.getWidth()/2,20)
