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
def judicium(getal):
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
def ggd(a,b):
	while b != 0:
		a,b = b, a % b
	print 'ggd:', a
	return a

#Main
if __name__ == '__main__':
	judicium(10.0)
	judicium(9.0)
	judicium(8.0)
	judicium(7.0)
	judicium(6.0)
	judicium(5.0)

	ggd(11,5)
	ggd(15,5)
	ggd(30,2)
	ggd(24404, 18050)
