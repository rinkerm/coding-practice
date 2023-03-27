#include "ndiscount1.h"

using namespace std;

ndiscount1::ndiscount1() :
	pricing("n discount 1") {}
	
double ndiscount1::cost(const product &p, int n) {
	double total = p.price();
	double current_price = p.price();
	if(n==0) {return 0;}
	for(int i =1;i<n;i++)
	{
		current_price -= (current_price * 0.1);
		total += (current_price);
	}
	return total;
	
}
