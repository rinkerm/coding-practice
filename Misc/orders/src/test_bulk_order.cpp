#include "bulk_order.h"
#include <iostream>
#include <string>

int main()
{
    // Create a bulk order with ID 1001 and 10% discount
    BulkOrder order(1001, 10);
    
    // Create some products
    Product laptop("Laptop", 1200.00);
    Product mouse("Wireless Mouse", 29.99);
    Product keyboard("Mechanical Keyboard", 89.99);
    Product monitor("27-inch Monitor", 349.99);
    
    // Add products to the order
    order.add_item(laptop, 2);
    order.add_item(mouse, 5);
    order.add_item(keyboard, 2);
    order.add_item(monitor, 3);
    
    // Display order as string
    std::cout << order.to_string() << std::endl;
    
    // Test contains method
    Product nonExistentProduct("Headphones", 49.99);
    std::cout << "Order contains mouse? " << (order.contains(mouse) ? "Yes" : "No") << std::endl;
    std::cout << "Order contains headphones? " << (order.contains(nonExistentProduct) ? "Yes" : "No") << std::endl;
    
    // Test remove_item method
    std::cout << "\nRemoving 1 keyboard..." << std::endl;
    order.remove_item(keyboard, 1);
    std::cout << order.to_string() << std::endl;
    
    // Test remove_item that removes an item completely
    std::cout << "Removing remaining keyboards..." << std::endl;
    order.remove_item(keyboard, 1);
    std::cout << order.to_string() << std::endl;
    
    // Create another order for comparison
    BulkOrder order2(1002, 5);
    order2.add_item(laptop, 1);
    order2.add_item(mouse, 2);
    
    std::cout << "\nComparing orders:" << std::endl;
    std::cout << "Order #" << order.get_id() << " total: $" << order.get_total() << std::endl;
    std::cout << "Order #" << order2.get_id() << " total: $" << order2.get_total() << std::endl;
    std::cout << "order1 > order2? " << (order>order2 ? "Yes" : "No") << std::endl;
    std::cout << "order1 = order2? " << (order==order2 ? "Yes" : "No") << std::endl;
    
    return 0;
}
