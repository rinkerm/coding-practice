#include "product.h"
#include <iostream>
#include <string>

int main() {
    try {
        // Create product instances
        Product item1("Product1", 10.0);
        std::cout << "Name is: " << item1.name() << std::endl;
        std::cout << "Price is: " << item1.price() << std::endl;
        
        Product item2("Product2", 20.0);
        Product item3("Product1", 10.0);  // Same as item1
        
        // Test comparison operators
        std::cout << "\n=== Comparison Tests ===" << std::endl;
        std::cout << "item1 == item2? " << std::boolalpha << (item1 == item2) << std::endl;
        std::cout << "item1 == item3? " << std::boolalpha << (item1 == item3) << std::endl;
        std::cout << "item1 != item2? " << std::boolalpha << (item1 != item2) << std::endl;
        
        std::cout << "\n=== Price Comparisons ===" << std::endl;
        std::cout << "item1 > item2? " << std::boolalpha << (item1 > item2) << std::endl;
        std::cout << "item1 >= item2? " << std::boolalpha << (item1 >= item2) << std::endl;
        std::cout << "item1 < item2? " << std::boolalpha << (item1 < item2) << std::endl;
        std::cout << "item1 <= item2? " << std::boolalpha << (item1 <= item2) << std::endl;
        
        // Test edge cases
        Product item4("Product3", 10.0000001);  // Very close price
        std::cout << "\n=== Edge Case Tests ===" << std::endl;
        std::cout << "item1 == item4 (similar price)? " << std::boolalpha << (item1 == item4) << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
