from sys import exit
class Fraction:
	#Constructor with check for a nominator of zero.
	def __init__(self, nom, den):
		if type(nom) == int and type(den) == int:
			if den != 0:
				a = Fraction.getGgd(nom, den)
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
		return '{} / {}'.format(self.nom, self.den)
	
	#Return the ggd of the two values
	@staticmethod
	def getGgd(nom, den):
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

#Test Fraction and ComplexFraction classes
if __name__ == '__main__':
	print '#Fractions:'
	f1 = Fraction(1,6)
	f2 = Fraction(1,4)
	print 'f1: {}'.format(f1)
	print 'f2: {}'.format(f2)
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
	print '#Complex Fractions'