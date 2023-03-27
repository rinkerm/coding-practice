#include "product.h"
#include "pricing.h"
#include "bogo.h"
#include "ndiscount1.h"
#include "ndiscount2.h"
#include "avgdiscount.h"
#include "giftcard.h"

#include <iostream>
#include <string>
#include<assert.h>

using namespace std;

void test_bogo()
{
	bogo policy;
	product item("stick",10);
	//Testing case where n = 0
	assert(policy.cost(item,0)==0);
	cout<<"BOGO Passed n == 0"<<endl;
	//Testing case where n is odd
	assert(policy.cost(item,9)==50);
	cout<<"BOGO Passed n % 2 == 1"<<endl;
	//Testing case where n is even
	assert(policy.cost(item,10)==50);
	cout<<"BOGO Passed n % 2 == 0"<<endl;
}

void test_ndiscount1()
{
	ndiscount1 policy;
	product item("stick",10);
	//Testing case where n = 0
	assert(policy.cost(item,0)==0);
	cout<<"NDISCOUNT1 Passed n == 0"<<endl;
	//Testing case where n = 1
	assert(policy.cost(item,1)==10);
	cout<<"NDISCOUNT1 Passed n == 1"<<endl;
	//Testing case where n = 3
	assert(policy.cost(item,3)==27.1);
	cout<<"NDISCOUNT1 Passed n == 3"<<endl;
}

void test_ndiscount2()
{
	ndiscount2 policy(0.1);
	product item("stick",10);
	//Testing cases where discount is 10%
	//Testing case where n = 0
	assert(policy.cost(item,0)==0);
	cout<<"10% NDISCOUNT2 Passed n == 0"<<endl;
	//Testing case where n = 1
	assert(policy.cost(item,1)==10);
	cout<<"10% NDISCOUNT2 Passed n == 1"<<endl;
	//Testing case where n = 3
	assert(policy.cost(item,3)==27.1);
	cout<<"10% NDISCOUNT2 Passed n == 3"<<endl;
	//Testing cases where discount is 50%
	ndiscount2 policy2(0.5);
	//Testing case where n = 0
	assert(policy2.cost(item,0)==0);
	cout<<"50% NDISCOUNT2 Passed n == 0"<<endl;
	//Testing case where n = 1
	assert(policy2.cost(item,1)==10);
	cout<<"50% NDISCOUNT2 Passed n == 1"<<endl;
	//Testing case where n = 3
	assert(policy2.cost(item,3)==17.5);
	cout<<"50% NDISCOUNT2 Passed n == 3"<<endl;
}

void test_avgdiscount()
{
	bogo policy;
	ndiscount2 policy1(0.1);
	ndiscount2 policy2(0.5);
	product item("stick",10);
	//Testing cases where discounts are same type
	avgdiscount policy3(policy1,policy2);
	//Testing case where n=0
	assert(policy3.cost(item,0)==0);
	cout<<"Same Discount AVGDISCOUNT Passed n == 0"<<endl;
	//Testing case where n>0
	assert(policy3.cost(item,3)==22.3);
	cout<<"Same Discount AVGDISCOUNT Passed n > 0"<<endl;
	//Testing cases where discounts are not same type
	avgdiscount policy4(policy,policy2);
	//Testing case where n is odd
	assert(policy4.cost(item,3)==18.75);
	cout<<"Different Discount AVGDISCOUNT Passed n % 2 == 1"<<endl;
	//Testing case where n is even
	assert(policy4.cost(item,4)==19.375);
	cout<<"Different Discount AVGDISCOUNT Passed n % 2 == 0"<<endl;
	
}

void test_giftcard()
{
	giftcard policy(0.5,1);
	product item("stick",10);
	//Testing case where n=0
	assert(policy.cost(item,0)==0);
	assert(policy.get_uses()==1);
	cout<<"GIFTCARD Passed n == 0"<<endl;
	//Testing case where n > 0
	assert(policy.cost(item,5)==25);
	assert(policy.get_uses()==0);
	cout<<"GIFTCARD Passed n > 0"<<endl;
	//Testing case where uses == 0
	assert(policy.cost(item,5)==50);
	assert(policy.get_uses()==0);
	cout<<"GIFTCARD Passed uses == 0"<<endl;
}

int main() {
	test_bogo();
	test_ndiscount1();
	test_ndiscount2();
	test_avgdiscount();
	test_giftcard();
	return 0;
}

