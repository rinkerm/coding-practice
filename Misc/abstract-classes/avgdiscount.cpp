#include "avgdiscount.h"

using namespace std;
// avg of two pricing schemes
avgdiscount::avgdiscount(pricing &p1, pricing &p2) :
	pricing("avg of " + p1.name() + " and " + p2.name()),
	policy1(p1), policy2(p2) {}
double avgdiscount::cost(const product &p, int n) {
	return ((policy1.cost(p, n)+policy2.cost(p, n))/2);
}

