#ifndef PRODUCT_H
#define PRODUCT_H
#include <string>
class product {

	const std::string _name;
	const double _price;

	public:

		product(const std::string &n, double p) :
			_name(n), _price(p) {}
	
		const std::string & name() const { return _name; }
		double price() const { return _price; }

};
#endif

