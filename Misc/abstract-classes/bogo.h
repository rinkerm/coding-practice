#ifndef BOGO_H
#define BOGO_H
#include "pricing.h"
class bogo : public pricing {
public:
	bogo();
	double cost(const product &p, int n) override;
};
#endif

