from roots import *
import functools

if __name__ == "__main__":
   p = Polynomial(1, 2, -1, -2)

   print('Potential roots for {} are :- {}'.format(p, p.proots()))
   print('Rational roots for {} are :- {}'.format(p, p.roots()))
   print('The factors for {} are:'.format(p))
   for q in p.pfactors():
     print("   · {}".format(q))
   print('Counterprove: {} = '.format(p), end='')
   print(functools.reduce(Polynomial.__mul__, p.pfactors()))

   p = Polynomial(2,-3,1,-2,-8)

   print('Potential roots for {} are :- {}'.format(p, p.proots()))
   print('Rational roots for {} are :- {}'.format(p, p.roots()))
   print('The factors for {} are:'.format(p))
   for q in p.pfactors():
     print("   · {}".format(q))
   print('Counterprove: {} = '.format(p), end='')
   print(functools.reduce(Polynomial.__mul__, p.pfactors()))
