#include "bogo.h"

using namespace std;

bogo::bogo() :
	pricing("bogo") {}
	
double bogo::cost(const product &p, int n) {
	if(n%2==1)
	{
		return p.price()*((n/2)+1);
	}
	else
	{
		return p.price()*(n/2);
	}
}
