from sys import exit
class Fraction:

	def __init__(self, nom, den):
		if type(nom) == int and type(den) == int:
			ggd = ggd(nom, den)
			self.nom = nom/ggd
			self.den = den/ggd
		else:
			print 'Dit is geen geldige Fractie'
			exit(0)

	def __repr__(self):
		return 'Fraction({},{})'.format(self.nom, self.den)

	def __str__(self):
		return '{} / {}'.format(self.nom, self.den)
	
	#Return the reciproke of the current Fraction
	def reciproke(self):
		return Fraction(self.den, self.nom)

	#Return the ggd of the two values
	def ggd(nom, den):
		while nom != 0:
			den,nom = nom, den % nom
		return den

	#Multiply self with Fraction f2 and return new Fraction.
	def __mul__(self, f2):
		return Fraction(self.nom * f2.nom, self.den * f2.den)

	#Divide self by Fraction f2 and return new Fraction.
	def __div__(self, f2):
		return self.reciproke()*f2

	#Add self to Fraction f2 and return new Fraction.
	def __add__(self, f2):
		newDen
		newNom
		return Fraction(newNom, newDen)

	#Substract f2 from self and return new Fractions
	def __sub__(self, f2):
		newDen
		newNom
		return Fraction(newNom, newDen)
