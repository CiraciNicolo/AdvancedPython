from primality import *

def test_primes( vl ):
    if len ( vl ) >0:
        print ( " {:14d} :- {} " . format ( vl [ 0], is_prime ( vl [ 0])))
        test_primes ( vl [ 1:])

if __name__ == '__main__' :
    test_primes ([ 25, 127, 8191, 131071, 524286, 524287, 524288, 2147483647])
