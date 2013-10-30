##
#   NAAM    : Maico Timmerman
#   CKNUM   : 10542590
#   Studie  : Informatica
#
#   Ggd.py
#       This program prints ggd of two numbers.
#       e.g. De ggd van 5 en 15: 5
##

def ggd(a, b):
    while b != 0:
        a,b = b, a % b
    return a

print 'De ggd van 5 en 15: {}'.format(ggd(5, 15))
print 'De ggd van 15 en 5: {}'.format(ggd(15, 5))
print 'De ggd van 16 en 2048: {}'.format(ggd(16, 2048))
print 'De ggd van 1234 en 81242: {}'.format(ggd(1234, 81247))