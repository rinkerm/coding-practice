#ifndef NDISCOUNT1_H
#define NDISCOUNT1_H
#include "pricing.h"
class ndiscount1 : public pricing {
public:
	ndiscount1();
	double cost(const product &p, int n) override;
};
#endif
