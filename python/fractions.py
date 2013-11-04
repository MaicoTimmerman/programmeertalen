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
			raise ValueError('Use: Fraction(int, int)')

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
		else:
			raise TypeError('cannot multiply Fraction with non-int/non-Fraction')
		
	#Divide self by Fraction other and return new Fraction.
	def __div__(self, other):
		if isinstance(other, Fraction):
			return Fraction(self.nom * other.den, self.den * other.nom)
		elif isinstance(other, int):
			f1 = self.intToFraction(other)
			return self / f1
		else:
			raise TypeError('cannot divide Fraction with non-int/non-Fraction')
		
	#Add self to Fraction other and return new Fraction.
	def __add__(self, other):
		if isinstance(other, Fraction):
			return Fraction((self.nom * other.den) + (other.nom * self.den), (self.den * other.den))
		elif isinstance(other, int):
			f1 = self.intToFraction(other)
			return self + f1
		else:
			raise TypeError('cannot add Fraction with non-int/non-Fraction')
		
	#Substract other from self and return new Fraction.
	def __sub__(self, other):
		if isinstance(other, Fraction):
			return Fraction((self.nom * other.den) - (other.nom * self.den), (self.den * other.den))
		elif isinstance(other, int):
			f1 = self.intToFraction(other)
			return self - f1
		else:
			raise TypeError('cannot substract Fraction with non-int/non-Fraction')
	#Take power of self to other and return new Fraction.
	def __pow__(self, other):
		if isinstance(other, int):
			return Fraction(self.nom**other,self.den**other)
		else:
			raise TypeError('can only take power of a fraction with an integer.')

class ComplexFraction:
	def __init__(self, args1, args2, args3=None, args4=None):
		if isinstance(args1, Fraction) and isinstance(args2, Fraction):
			self.re = args1
			self.im = args2
		elif type(args1) == int and type(args2) == int and type(args3) == int and type(args4) == int:
			self.re = Fraction(args1, args2)
			self.im = Fraction(args3, args4)
		else:
			raise ValueError('Use: ComplexFraction(Fraction, Fraction) or ComplexFraction(int, int, int, int)')

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
		else:
			raise TypeError('cannot add Fraction with non-(int/Fraction/ComplexFraction')

	#Substracts other from self and returns the result as ComplexFraction.
	def __sub__(self, other):
		if isinstance(other, ComplexFraction):
			return ComplexFraction(self.re - other.re, self.im - other.im)
		elif isinstance(other, Fraction):
			return ComplexFraction(self.re - other, self.im)
		elif isinstance(other, int):
			return ComplexFraction(self.re - other, self.im)
		else:
			raise TypeError('cannot substract Fraction with non-(int/Fraction/ComplexFraction')

	#Returns the result of self * other as ComplexFraction.
	def __mul__(self, other):
		if isinstance(other, ComplexFraction):
			return ComplexFraction((self.re * other.re) - (self.im * other.im) ,
								(self.re * other.im) + (self.im * other.re))
		elif isinstance(other, Fraction):
			return ComplexFraction(self.re * other, self.im * other)
		elif isinstance(other, int):
			return ComplexFraction(self.re * other, self.im * other)
		else:
			raise TypeError('cannot multiply Fraction with non-(int/Fraction/ComplexFraction')

	#Returns the result of self / other as ComplexFraction.
	def __div__(self, other):
		if isinstance(other, ComplexFraction):
			return self * other.reciproke()
		elif isinstance(other, Fraction):
			return ComplexFraction(self.im * other.reciproke(),
										self.re * other.reciproke())
		elif isinstance(other, int):
			return self * Fraction(1, other)
		else:
			raise TypeError('cannot divide Fraction with non-(int/Fraction/ComplexFraction')

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
	f1 = Fraction(2,6)
	f2 = Fraction(6,4)
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
	print 'f1 ** 2: {}'.format(f1**2)
	print 'f2 ** 2: {}'.format(f2 ** 2)
	print
	print '##'
	print '#\t Fractions with integers'
	print '##'
	print
	print 'f1 + 2: {}'.format(f1 + 2)
	print 'f1 - 2: {}'.format(f1 - 2)
	print 'f2 - 2: {}'.format(f2 - 2)
	print 'f1 - 21541 + 21541: {}'.format(f1 - 21541 + 21541)
	print 'f2 - 21541 + 21541: {}'.format(f2 - 21541 + 21541)
	print
	print 'f1 * 2: {}'.format(f1 * 2)
	print 'f1 / 2: {}'.format(f1 / 2)
	print 'f2 / 2: {}'.format(f2 / 2)
	print 'f1 / 21541 * 21541: {}'.format(f1 / 21541 * 21541)
	print 'f2 / 21541 * 21541: {}'.format(f2 / 21541 * 21541)
	print
	print '##'
	print '#\tComplex Fractions'
	print '##'
	print
	fr1 = Fraction(1,6)
	fr2 = Fraction(1,4)
	cf1 = ComplexFraction(fr1, fr2)
	cf2 = ComplexFraction(2, 1, 0, 1)
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
	print 'cf1 - 21541 + 21541: {}'.format(cf1 - 21541 + 21541)
	print 'cf2 - 21541 + 21541: {}'.format(cf2 - 21541 + 21541)
	print
	print 'cf1 * 2: {}'.format(cf1 * 2)
	print 'cf1 / 2: {}'.format(cf1 / 2)
	print 'cf2 / 2: {}'.format(cf2 / 2)
	print 'cf1 / 21541 * 21541: {}'.format(cf1 / 21541 * 21541)
	print 'cf2 / 21541 * 21541: {}'.format(cf2 / 21541 * 21541)