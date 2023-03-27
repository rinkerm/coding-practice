#ifndef AVGDISCOUNT_H
#define AVGDISCOUNT_H
#include "pricing.h"
// avg of two pricing schemes
class avgdiscount : public pricing {
	pricing &policy1;
	pricing &policy2;
	public:
	avgdiscount(pricing &p1, pricing &p2);
	double cost(const product &p, int n) override;
};
#endif

