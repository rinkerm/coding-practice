#ifndef BULK_ORDER_H
#define BULK_ORDER_H

#include <vector>
#include <string>
#include "product.h"

/**
 * @struct LineItem
 * @brief Represents an order line item of a product with quantity
 */
struct LineItem {
    Product product;
    int quantity;
    
    LineItem(Product& p, int qty) : product(p), quantity(qty) {}
};

/**
 * @class BulkOrder
 * @brief Represents a bulk order with multiple line items and a discount
 */
class BulkOrder {
private:
    const int _id;
    const double _discount;
    std::vector<LineItem> _items;

public:
    /**
     * @brief Constructor for BulkOrder
     * @param id Order ID
     * @param discount Discount percentage (e.g., 10 for 10%)
     */
    BulkOrder(const int id, double discount) :
        _id(id), _discount(discount) {}
    BulkOrder(const BulkOrder& other) = default;
    BulkOrder& operator=(const BulkOrder& other) = default;
    BulkOrder(BulkOrder&& other) = default;
    BulkOrder& operator=(BulkOrder&& other) = default;
    ~BulkOrder() = default;
	
    /**
     * @brief Calculate total order value after discount
     * @return Total value after discount
     */
    double get_total() const;
    int get_id() const { return _id; }
	
    bool operator==(const BulkOrder &o) const;
	bool operator!=(const BulkOrder &o) const;
	bool operator<(const BulkOrder &o) const;
	bool operator<=(const BulkOrder &o) const;
	bool operator>(const BulkOrder &o) const;
	bool operator>=(const BulkOrder &o) const;

    bool contains(const Product &p) const;
    
    /**
     * @brief Add product with quantity to order
     * @param p Product to add
     * @param quantity Quantity to add
     */
    void add_item(Product &p, int quantity);
    
    /**
     * @brief Remove product quantity from order
     * @param p Product to remove
     * @param quantity Quantity to remove
     */
    void remove_item(Product &p, int quantity);
    std::string to_string() const;
};

#endif // BULK_ORDER_H