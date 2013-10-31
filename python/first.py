##
#   NAAM    : Maico Timmerman
#   CKNUM   : 10542590
#   Studie  : Informatica
#
#   first.py
#       This program prints ggd of two numbers.
#       e.g. De ggd van 5 en 15: 5
##


#Vraagt op een getal en print de Jucidium waarde achter het getal.
def judicium():
	getal = ''
	try:
		getal = float(raw_input('Geef een waarde voor de Judicium functie:'))
	except ValueError:
		print 'Dit is geen getal!'
		print
		return

	if getal<5.5:
		suffix="(Failed)"
	elif getal>=8.5:
		suffix="(Cum Laude)"
	elif getal>= 7.5 and getal<8.5:
		suffix="(With Honors)"
	else:
		suffix=""
	print "Uitslag: {} {}".format(getal,suffix)
	print

#Vraagt een paar getallen op en bepaald van beide de ggd.
def ggd():
	try:
		a = int(raw_input('Geef een geheel getal a:'))
		b = int(raw_input('Geef een geheel getal b:'))
	except ValueError:
		print 'Dit is geen getal!'
		return

	while b != 0:
		a,b = b, a % b
	print a

#
def main():
	judicium()
	ggd()

if __name__ == '__main__':
	main()