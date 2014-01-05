// Following number theoretic functions just make use of GMP's number theoretic
// function implementations. Please refer the following manual:
// https://gmplib.org/manual/Number-Theoretic-Functions.html

#ifndef CSYMPY_NTHEORY_H
#define CSYMPY_NTHEORY_H

#include "integer.h"

namespace CSymPy {

RCP<Integer> gcd(const Integer &a, const Integer &b);
RCP<Integer> lcm(const Integer &a, const Integer &b);
int probab_prime_p(const Integer &a, int reps = 25);
RCP<Integer> nextprime(const Integer &a);
void gcd_ext(const Integer &a, const Integer &b, const Ptr<RCP<Integer>> &g,
                        const Ptr<RCP<Integer>> &s, const Ptr<RCP<Integer>> &t);
}
#endif
