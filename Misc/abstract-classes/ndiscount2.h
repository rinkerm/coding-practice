#ifndef NDISCOUNT2_H
#define NDISCOUNT2_H
#include "pricing.h"
class ndiscount2 : public pricing {
	double discount;
public:
	ndiscount2(double d);
	double cost(const product &p, int n) override;
};
#endif
