#include "product.h"
#include <stdexcept>

Product::Product(const std::string& name, double price) 
    : name_(name), price_(price) {
    if (price < 0) {
        throw std::invalid_argument("Price cannot be negative");
    }
}

bool Product::operator==(const Product& other) const {
    return (name_ == other.name_) && isEqual(price_, other.price_);
}

bool Product::operator!=(const Product& other) const {
    return !(*this == other);
}

bool Product::operator<(const Product& other) const {
    return price_ < other.price_;
}

bool Product::operator<=(const Product& other) const {
    return (*this < other) || (*this == other);
}

bool Product::operator>(const Product& other) const {
    return other < *this;
}

bool Product::operator>=(const Product& other) const {
    return (*this > other) || (*this == other);
}

bool Product::isEqual(double a, double b, double epsilon) {
    return std::abs(a - b) < epsilon;
}
