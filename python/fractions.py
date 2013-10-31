##
#   NAAM    : Maico Timmerman
#   CKNUM   : 10542590
#   Studie  : Informatica
#
#   fractions.py
#       This program implements 2 classes, Fraction and Complex Faction.
#       Both classes have overloaded functions for +, -, * and /. and 
#		can be reversed.
##

from sys import exit
class Fraction:
	#Constructor with check for a nominator of zero.
	def __init__(self, nom, den):
		if type(nom) == int and type(den) == int:
			if den != 0:
				a = self.getGgd(nom, den)
				self.nom = nom / a
				self.den = den / a
			else:
				print 'Denominator cannot be zero.'
				exit(0)
		else:
			print 'This isn\'t a valid Fraction.'
			exit(0)

	#Return a string in the form Fraction(x, x)
	def __repr__(self):
		return 'Fraction({},{})'.format(self.nom, self.den)

	#Return a string in the form x / x
	def __str__(self):
		return '{}/{}'.format(self.nom, self.den)
	
	#Return the ggd of the two values
	def getGgd(self, nom, den):
		while nom != 0:
			den,nom = nom, den % nom
		return den

	#Return the reciproke of the current Fraction
	def reciproke(self):
		return Fraction(self.den, self.nom)


	#Multiply self with Fraction f2 and return new Fraction.
	def __mul__(self, f2):
		return Fraction(self.nom * f2.nom, self.den * f2.den)

	#Divide self by Fraction f2 and return new Fraction.
	def __div__(self, f2):
		return Fraction(self.nom * f2.den, self.den * f2.nom)

	#Add self to Fraction f2 and return new Fraction.
	def __add__(self, f2):
		return Fraction((self.nom * f2.den) + (f2.nom * self.den), (self.den * f2.den))

	#Substract f2 from self and return new Fractions
	def __sub__(self, f2):
		return Fraction((self.nom * f2.den) - (f2.nom * self.den), (self.den * f2.den))


class ComplexFraction:
	def __init__(self, re, im):
		if isinstance(re, Fraction) and isinstance(im, Fraction):
			self.re = re
			self.im = im
		else:
			print 'The inputs aren\'t fractions'
			exit()

	#Returns a string in the form of (x/x) + (x/x)j
	def __str__(self):
		return '({}) + ({})j'.format(self.re, self.im)

	#Returns a string in the form ComplexFraction(Fraction(x,x), Fraction(x,x)).
	def __repr__(self):
		return 'ComplexFraction({},{})'.format(self.re.__repr__(), self.im.__repr__())

	#Adds 2 ComplexFractions and returns the result as ComplexFraction.
	def __add__(self, cf2):
		return ComplexFraction(self.re + cf2.re, self.im + cf2.im)

	#Substracts cf2 from self and returns the result as ComplexFraction.
	def __sub__(self, cf2):
		return ComplexFraction(self.re - cf2.re, self.im - cf2.im)

	#Returns the result of self * cf2 as ComplexFraction.
	def __mul__(self, cf2):
		return ComplexFraction((self.re * cf2.re) - (self.im * cf2.im) ,
								(self.re * cf2.im) + (self.im * cf2.re))

	def __div__(self, cf2):
		return self * cf2.reciproke()

	#Returns the result of self / cf2 as ComplexFraction.
	def reciproke(self):
		p = self.re.nom
		q = self.re.den
		r = self.im.nom
		s = self.im.den
		f1 = Fraction((p * q * s * s), (p * p * s * s) + (r * r * q * q))
		f2 = Fraction((-1 *(r * q * q * s)), (p * p * s * s) + (r * r * q * q))
		return ComplexFraction(f1, f2)

#Test Fraction and ComplexFraction classes
if __name__ == '__main__':
	##
	#	Fractions
	##
	print '#Fractions:'
	f1 = Fraction(1,6)
	f2 = Fraction(1,4)
	print 'f1: {}'.format(f1)
	print 'f2: {}'.format(f2)
	print 'omgekeerde f1: {}'.format(f1.reciproke())
	print 'omgekeerde f2: {}'.format(f2.reciproke())
	#Add and substract tests.
	print
	print 'f1 + f2: {}'.format(f1 + f2)
	print 'f1 - f2: {}'.format(f1 - f2)
	print 'f2 - f1: {}'.format(f2 - f1)
	print 'f1 - f2 + f2: {}'.format(f1 - f2 + f2)
	print 'f2 - f1 + f1: {}'.format(f2 - f1 + f1)
	#Multiply and divide tests.
	print
	print 'f1 * f2: {}'.format(f1 * f2)
	print 'f1 / f2: {}'.format(f1 / f2)
	print 'f2 / f1: {}'.format(f2 / f1)
	print 'f1 / f2 * f2: {}'.format(f1 / f2 * f2)
	print 'f2 / f1 * f1: {}'.format(f2 / f1 * f1)
	print
	##
	#	ComplexFractions
	##
	print '#Complex Fractions'
	fr1 = Fraction(1,6)
	fr2 = Fraction(1,4)
	fr3 = Fraction(5,6)
	fr4 = Fraction(2,3)
	cf1 = ComplexFraction(fr1, fr2)
	cf2 = ComplexFraction(fr3, fr4)
	print 'cf1: {}'.format(cf1)
	print 'cf2: {}'.format(cf2)
	print 'omgekeerde cf1: {}'.format(cf1.reciproke())
	print 'omgekeerde cf2: {}'.format(cf2.reciproke())
	#Add and substract tests.
	print
	print 'cf1 + cf2: {}'.format(cf1 + cf2)
	print 'cf1 - cf2: {}'.format(cf1 - cf2)
	print 'cf2 - cf1: {}'.format(cf2 - cf1)
	print 'cf1 - cf2 + cf2: {}'.format(cf1 - cf2 + cf2)
	print 'cf2 - cf1 + cf1: {}'.format(cf2 - cf1 + cf1)
	#Multiply and divide tests.
	print
	print 'cf1 * cf2: {}'.format(cf1 * cf2)
	print 'cf1 / cf2: {}'.format(cf1 / cf2)
	print 'cf2 / cf1: {}'.format(cf2 / cf1)
	print 'cf1 / cf2 * cf2: {}'.format(cf1 / cf2 * cf2)
	print 'cf2 / cf1 * cf1: {}'.format(cf2 / cf1 * cf1)