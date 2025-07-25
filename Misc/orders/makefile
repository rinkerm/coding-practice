CXX       := g++
CXX_FLAGS := -Wall -Wextra -std=c++17 -ggdb

BIN     := bin
SRC     := src
INCLUDE := include
LIB     := lib
LIBRARIES   := 

PRODUCT_EXECUTABLE := test_product
BULKORDER_EXECUTABLE := test_bulk_order

all: $(BIN)/$(PRODUCT_EXECUTABLE) $(BIN)/$(BULKORDER_EXECUTABLE)

run_product: $(BIN)/$(PRODUCT_EXECUTABLE)
	@echo "Executing product test..."
	./$(BIN)/$(PRODUCT_EXECUTABLE)

run_bulkorder: $(BIN)/$(BULKORDER_EXECUTABLE)
	@echo "Executing bulk order test..."
	./$(BIN)/$(BULKORDER_EXECUTABLE)

$(BIN)/$(PRODUCT_EXECUTABLE): $(SRC)/product.cpp $(SRC)/test_product.cpp
	@mkdir -p $(BIN)
	@echo "Building product test..."
	$(CXX) $(CXX_FLAGS) -I$(INCLUDE) -L$(LIB) $^ -o $@ $(LIBRARIES)

$(BIN)/$(BULKORDER_EXECUTABLE): $(SRC)/product.cpp $(SRC)/bulk_order.cpp $(SRC)/test_bulk_order.cpp
	@mkdir -p $(BIN)
	@echo "Building bulk order test..."
	$(CXX) $(CXX_FLAGS) -I$(INCLUDE) -L$(LIB) $^ -o $@ $(LIBRARIES)
clean:
	@echo "Clearing..."
	$(RM) $(BIN)/*