#include "giftcard.h"

using namespace std;

giftcard::giftcard(double d, int u) :
	pricing("limited uses giftcard") {
	discount = d;
	uses = u;
	}
	
double giftcard::cost(const product &p, int n) {
	if(n == 0)
	{
		return 0;
	}
	else if(get_uses()>0)
	{
		decrement_uses();
		return ((p.price()*discount)*n);
	}
	else{
		return p.price()*n;
	}
	
}
int giftcard::get_uses()
{
	return uses;
}

void giftcard::decrement_uses()
{
	if(get_uses()>0)
	{
		uses -= 1;
	}
}
