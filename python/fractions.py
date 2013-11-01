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
				a = abs(self.getGgd(nom, den))
				self.nom = nom / a
				self.den = den / a
				if self.nom < 0 and self.den < 0:
					self.nom = abs(self.nom)
					self.den = abs(self.den)
				elif self.nom > 0 and den < 0:
					self.nom = self.nom * -1
					self.den = abs(self.den)
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

	#Returns the int as a Fraction
	def intToFraction(self, other):
		return Fraction(other, 1)

	#Multiply self with Fraction other and return new Fraction.
	def __mul__(self, other):
		if isinstance(other, Fraction):
			return Fraction(self.nom * other.nom, self.den * other.den)
		elif isinstance(other, int):
			f1 = self.intToFraction(other)
			return self * f1
		
	#Divide self by Fraction other and return new Fraction.
	def __div__(self, other):
		if isinstance(other, Fraction):
			return Fraction(self.nom * other.den, self.den * other.nom)
		elif isinstance(other, int):
			f1 = self.intToFraction(other)
			return self / f1
		
	#Add self to Fraction other and return new Fraction.
	def __add__(self, other):
		if isinstance(other, Fraction):
			return Fraction((self.nom * other.den) + (other.nom * self.den), (self.den * other.den))
		elif isinstance(other, int):
			f1 = self.intToFraction(other)
			return self + f1
		
	#Substract other from self and return new Fractions
	def __sub__(self, other):
		if isinstance(other, Fraction):
			return Fraction((self.nom * other.den) - (other.nom * self.den), (self.den * other.den))
		elif isinstance(other, int):
			f1 = self.intToFraction(other)
			return self - f1

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
	def __add__(self, other):
		if isinstance(other, ComplexFraction):
			return ComplexFraction(self.re + other.re, self.im + other.im)
		elif isinstance(other, Fraction):
			return ComplexFraction(self.re + other, self.im)
		elif isinstance(other, int):
			return ComplexFraction(self.re + other, self.im)

	#Substracts other from self and returns the result as ComplexFraction.
	def __sub__(self, other):
		if isinstance(other, ComplexFraction):
			return ComplexFraction(self.re - other.re, self.im - other.im)
		elif isinstance(other, Fraction):
			return ComplexFraction(self.re - other, self.im)
		elif isinstance(other, int):
			return ComplexFraction(self.re - other, self.im)

	#Returns the result of self * other as ComplexFraction.
	def __mul__(self, other):
		if isinstance(other, ComplexFraction):
			return ComplexFraction((self.re * other.re) - (self.im * other.im) ,
								(self.re * other.im) + (self.im * other.re))
		elif isinstance(other, Fraction):
			return ComplexFraction(self.re * other, self.im * other)
		elif isinstance(other, int):
			return ComplexFraction(self.re * other, self.im * other)


	#Returns the result of self / other as ComplexFraction.
	def __div__(self, other):
		if isinstance(other, ComplexFraction):
			return self * other.reciproke()
		elif isinstance(other, Fraction):
			return ComplexFraction(self.im * other.reciproke(),
										self.re * other.reciproke())
		elif isinstance(other, int):
			return self * Fraction(1, other)

		returm

	#Returns the reciproke ComplexFraction of self.
	def reciproke(self):
		p = self.re.nom
		q = self.re.den
		r = self.im.nom
		s = self.im.den
		f1 = Fraction((p * q * s * s), (p * p * s * s) + (r * r * q * q))
		f2 = Fraction((-1 *(r * q * q * s)), (p * p * s * s) + (r * r * q * q))
		return ComplexFraction(f1, f2)

	#Return a pythonic complex value
	def toComplex(self):
		p = float(self.re.nom)
		q = float(self.re.den)
		r = float(self.im.nom)
		s = float(self.im.den)
		return complex(p/q, r/s)
		

#Test Fraction and ComplexFraction classes
if __name__ == '__main__':
	print '##'
	print '#\tFractions:'
	print '##'
	print
	f1 = Fraction(1,6)
	f2 = Fraction(1,4)
	print 'f1: {}'.format(f1)
	print 'f2: {}'.format(f2)
	print 'omgekeerde f1: {}'.format(f1.reciproke())
	print 'omgekeerde f2: {}'.format(f2.reciproke())
	print
	print 'f1 + f2: {}'.format(f1 + f2)
	print 'f1 - f2: {}'.format(f1 - f2)
	print 'f2 - f1: {}'.format(f2 - f1)
	print 'f1 - f2 + f2: {}'.format(f1 - f2 + f2)
	print 'f2 - f1 + f1: {}'.format(f2 - f1 + f1)
	print
	print 'f1 * f2: {}'.format(f1 * f2)
	print 'f1 / f2: {}'.format(f1 / f2)
	print 'f2 / f1: {}'.format(f2 / f1)
	print 'f1 / f2 * f2: {}'.format(f1 / f2 * f2)
	print 'f2 / f1 * f1: {}'.format(f2 / f1 * f1)
	print
	print '##'
	print '#\t Fractions with integers'
	print '##'
	print
	print 'f1 + 2: {}'.format(f1 + 2)
	print 'f1 - 2: {}'.format(f1 - 2)
	print 'f2 - 2: {}'.format(f2 - 2)
	print 'f1 - 2 + 2: {}'.format(f1 - 2 + 2)
	print 'f2 - 2 + 2: {}'.format(f2 - 2 + 2)
	print
	print 'f1 * 2: {}'.format(f1 * 2)
	print 'f1 / 2: {}'.format(f1 / 2)
	print 'f2 / 2: {}'.format(f2 / 2)
	print 'f1 / 2 * 2: {}'.format(f1 / 2 * 2)
	print 'f2 / 2 * 2: {}'.format(f2 / 2 * 2)
	print
	print '##'
	print '#\tComplex Fractions'
	print '##'
	print
	fr1 = Fraction(1,6)
	fr2 = Fraction(1,4)
	fr3 = Fraction(2,1)
	fr4 = Fraction(0,1)
	cf1 = ComplexFraction(fr1, fr2)
	cf2 = ComplexFraction(fr3, fr4)
	print 'cf1: {}'.format(cf1)
	print 'cf2: {}'.format(cf2)
	print 'omgekeerde cf1: {}'.format(cf1.reciproke())
	print 'omgekeerde cf2: {}'.format(cf2.reciproke())
	print 'pythonic complex cf1 {}'.format(cf1.toComplex())
	print 'pythonic complex cf2 {}'.format(cf2.toComplex())
	print 'cf1 + cf2: {}'.format(cf1 + cf2)
	print 'cf1 - cf2: {}'.format(cf1 - cf2)
	print 'cf2 - cf1: {}'.format(cf2 - cf1)
	print 'cf1 - cf2 + cf2: {}'.format(cf1 - cf2 + cf2)
	print 'cf2 - cf1 + cf1: {}'.format(cf2 - cf1 + cf1)
	print
	print 'cf1 * cf2: {}'.format(cf1 * cf2)
	print 'cf1 / cf2: {}'.format(cf1 / cf2)
	print 'cf2 / cf1: {}'.format(cf2 / cf1)
	print 'cf1 / cf2 * cf2: {}'.format(cf1 / cf2 * cf2)
	print 'cf2 / cf1 * cf1: {}'.format(cf2 / cf1 * cf1)
	print
	print '##'
	print '#\t ComplexFractions with integers'
	print '##'
	print
	print 'cf1 + 2: {}'.format(cf1 + 2)
	print 'cf1 - 2: {}'.format(cf1 - 2)
	print 'cf2 - cf1: {}'.format(cf2 - 2)
	print 'cf1 - 2 + 2: {}'.format(cf1 - 2 + 2)
	print 'cf2 - cf1 + cf1: {}'.format(cf2 - 2 + 2)
	print
	print 'cf1 * 2: {}'.format(cf1 * 2)
	print 'cf1 / 2: {}'.format(cf1 / 2)
	print 'cf2 / 2: {}'.format(cf2 / 2)
	print 'cf1 / 2 * 2: {}'.format(cf1 / 2 * 2)
	print 'cf2 / 2 * 2: {}'.format(cf2 / 2 * 2)