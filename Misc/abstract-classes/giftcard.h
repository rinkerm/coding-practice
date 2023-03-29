#ifndef GIFTCARD_H
#define GIFTCARD_H
#include "pricing.h"
class giftcard : public pricing {
	double discount;
	int uses;
	void decrement_uses();
public:
	giftcard(double d, int u);
	double cost(const product &p, int n) override;
	int get_uses();
};
#endif
