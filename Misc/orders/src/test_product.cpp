#include "product.h"
#include <iostream>
#include <string>

int main()
{
	product item1("product1", 10);
	std::cout<<"name is "<<item1.name()<<std::endl;
	std::cout<<"price is "<<item1.price()<<std::endl;
	
	product item2("product2", 20);
	std::cout<<"item1 = item2? "<<item1.equals(item2)<<std::endl;
	std::cout<<"item1 > item2? "<<item1.greater_than(item2)<<std::endl;
	std::cout<<"item1 >= item2? "<<item1.greater_than_equal(item2)<<std::endl;
	std::cout<<"item1 < item2? "<<item1.less_than(item2)<<std::endl;
	std::cout<<"item1 <= item2? "<<item1.less_than_equal(item2)<<std::endl;
	return 0;
}