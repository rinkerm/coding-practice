#ifndef PRODUCT_H
#define PRODUCT_H

#include <string>
#include <cmath>

/**
 * @class Product
 * @brief Represents a product with name and price
 */
class Product {
private:
    std::string name_;   // Removed 'const'
    double price_;       // Removed 'const'

public:
    /**
     * @brief Constructor for Product
     * @param name Product Name
     * @param price Product Price
     */
    Product(const std::string& name, double price);
    
    Product(const Product& other) = default;
    Product(Product&& other) = default;
    Product& operator=(const Product& other) = default;  // Now allowed
    Product& operator=(Product&& other) = default;       // Now allowed
    ~Product() = default;
    
    const std::string& name() const { return name_; }
    double price() const { return price_; }
    
    bool operator==(const Product& other) const;
    bool operator!=(const Product& other) const;
    bool operator<(const Product& other) const;
    bool operator<=(const Product& other) const;
    bool operator>(const Product& other) const;
    bool operator>=(const Product& other) const;

private:
    static bool isEqual(double a, double b, double epsilon = 1e-9);
};

#endif // PRODUCT_H
