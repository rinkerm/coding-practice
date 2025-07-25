#include "bulk_order.h"
#include <sstream>
#include <algorithm>
#include <iomanip>

double BulkOrder::get_total() const 
{
    double total = 0.0;
    
    for (const LineItem& item : _items) {
        total += item.product.price() * item.quantity;
    }
    
    double discount_factor = (100.0 - _discount) / 100.0;
    return total * discount_factor;
}

bool BulkOrder::operator==(const BulkOrder &o) const 
{
    return this->_id == o._id && this->get_total() == o.get_total();
}

bool BulkOrder::operator!=(const BulkOrder &o) const 
{
    return this->_id != o._id && this->get_total() != o.get_total();
}

bool BulkOrder::operator>(const BulkOrder &o) const
{
    return this->get_total() > o.get_total();
}

bool BulkOrder::operator>=(const BulkOrder &o) const
{
    return this->get_total() >= o.get_total();
}

bool BulkOrder::operator<(const BulkOrder &o) const
{
    return this->get_total() < o.get_total();
}

bool BulkOrder::operator<=(const BulkOrder &o) const
{
    return this->get_total() <= o.get_total();
}

bool BulkOrder::contains(const Product &p) const
{
    for (const LineItem& item : _items) {
        if (item.product==p) {
            return true;
        }
    }
    return false;
}

void BulkOrder::add_item(Product &p, int quantity)
{
    // Check if the product already exists in the order
    for (auto& item : _items) {
        if (item.product==p) {
            item.quantity += quantity;
            return;
        }
    }
    
    // If product doesn't exist, add it as a new line item
    _items.emplace_back(p, quantity);
}

void BulkOrder::remove_item(Product &p, int quantity)
{
    for (auto it = _items.begin(); it != _items.end(); ++it) {
        if (it->product==p) {
            it->quantity -= quantity;
            
            // If quantity is reduced to 0 or below, remove the line item
            if (it->quantity <= 0) {
                _items.erase(it);
            }
            
            return;
        }
    }
}

std::string BulkOrder::to_string() const
{
    std::stringstream ss;
    ss << "Order #" << _id << " (Discount: " << _discount << "%)" << std::endl;
    ss << "----------------------------------------" << std::endl;
    
    for (const LineItem& item : _items) {
        ss << std::setw(30) << std::left << item.product.name() 
           << std::setw(10) << std::right << item.quantity 
           << " x $" << std::fixed << std::setprecision(2) << item.product.price() 
           << " = $" << std::fixed << std::setprecision(2) << (item.quantity * item.product.price()) << std::endl;
    }
    
    ss << "----------------------------------------" << std::endl;
    ss << "Subtotal: $" << std::fixed << std::setprecision(2) 
       << (get_total() * 100.0 / (100.0 - _discount)) << std::endl;
    ss << "Discount: $" << std::fixed << std::setprecision(2) 
       << (get_total() * 100.0 / (100.0 - _discount) * _discount / 100.0) << std::endl;
    ss << "Total:    $" << std::fixed << std::setprecision(2) << get_total() << std::endl;
    
    return ss.str();
}
