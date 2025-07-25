#include "product.h"


bool product::equals(const product &p) 
{
	return this->price() == p.price() && this->name() == p.name();
}
bool product::greater_than(const product &p)
{
	return this->price()>p.price();
}
bool product::greater_than_equal(const product &p)
{
	return this->price()>=p.price();
}
bool product::less_than(const product &p)
{
	return this->price()<p.price();
}
bool product::less_than_equal(const product &p)
{
	return this->price()<=p.price();
}