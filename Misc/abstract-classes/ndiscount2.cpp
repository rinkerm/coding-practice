#include "ndiscount2.h"

using namespace std;

ndiscount2::ndiscount2(double d) :
	pricing("n discount 2") {discount = d;}
	
double ndiscount2::cost(const product &p, int n) {
	double total = p.price();
	double current_price = p.price();
	if(n==0) {return 0;}
	for(int i =1;i<n;i++)
	{
		current_price -= (current_price * discount);
		total += (current_price);
	}
	return total;
	
}
