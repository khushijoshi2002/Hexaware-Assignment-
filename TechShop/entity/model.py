import datetime

class Customers:
    def __init__(self, customer_id: int, first_name: str, last_name: str, email: str, phone: str, address: str):
        self.__CustomerID = customer_id
        self.__FirstName = first_name
        self.__LastName = last_name
        self.__Email = email
        self.__Phone = phone
        self.__Address = address
    
    # Accessor methods
    def get_customer_id(self) -> int:
        return self.__CustomerID
    
    def get_first_name(self) -> str:
        return self.__FirstName
    
    def get_last_name(self) -> str:
        return self.__LastName
    
    def get_email(self) -> str:
        return self.__Email
    
    def get_phone(self) -> str:
        return self.__Phone
    
    def get_address(self) -> str:
        return self.__Address

    # Mutator methods
    def set_customer_id(self, customer_id: int) -> None:
        self.__CustomerID = customer_id
    
    def set_first_name(self, first_name: str) -> None:
        self.__FirstName = first_name
    
    def set_last_name(self, last_name: str) -> None:
        self.__LastName = last_name
    
    def set_email(self, email: str) -> None:
        self.__Email = email
    
    def set_phone(self, phone: str) -> None:
        self.__Phone = phone
    
    def set_address(self, address: str) -> None:
        self.__Address = address

    def CalculateTotalOrders():
        pass

    def GetCustomerDetails():
        pass

    def UpdateCustomerInfo():
        pass 




class Products:
    def __init__(self, product_id: int, product_name: str, desc:str, price:float):
        self.__ProductID = product_id
        self.__ProductName = product_name
        self.__Description = desc
        self.__Price = price
    #Accessors and Mutators.
    def get_product_id(self) -> int:
        return self.__product_id
    def set_product_id(self, value: int):
        self.__product_id = value
    
    def get_product_name(self) -> str:
        return self.__product_name
    def set_product_name(self, value: str):
        self.__product_name = value
    
    def get_description(self) -> str:
        return self.__description
    def set_description(self, value: str):
        self.__description = value
    
    def get_price(self) -> float:
        return self.__price
    def set_price(self, value: float):
        if value>0:
            self.__price = value

    def GetProductDetails():
        pass
    def UpdateProductInfo():
        pass
    def IsProductInStock():
        pass

class Orders:
    def __init__(self, order_id: int, customer: Customers, order_date: datetime, tot_amount: float):
        self.__OrderID = order_id
        self.__customer = customer
        self.__OrderDate = order_date
        self.__TotalAmount = tot_amount

    def get_order_id(self) -> int:
        return self.__OrderID
    def set_order_id(self, value: int):
        self.__OrderID = value
    
    def get_customer(self) -> Customers:
        return self.__customer
    def set_customer(self, value: Customers):
        self.__customer = value
    
    def get_order_date(self) -> datetime:
        return self.__OrderDate
    def set_order_date(self, value: datetime):
        self.__OrderDate = value
    
    def get_total_amount(self) -> float:
        return self.__TotalAmount
    def set_total_amount(self, value: float):
        if value>0:
            self.__TotalAmount = value
    
    def CalculateTotalAmount():
        pass
    def GetOrderDetails():
        pass
    def UpdateOrderStatus():
        pass

class OrderDetails:
    def __init__(self, order_detail_id: int, order: Orders, product: Products, quantity: int):
        self.__OrderDetailID = order_detail_id
        self.__Order = order
        self.__Product = product
        self.__Quantity = quantity
    
    def get_order_detail_id(self) -> int:
        return self.__OrderDetailID
    def set_order_detail_id(self, value: int):
        self.__OrderDetailID = value
    
    def get_order(self) -> Orders:
        return self.__Order
    def set_order(self, value: Orders):
        self.__Order = value
    
    def get_product(self) -> Products:
        return self.__Product
    def set_product(self, value: Products):
        self.__Product = value
    
    def get_quantity(self) -> int:
        return self.__Quantity
    def set_quantity(self, value: int):
        if value>0:
            self.__Quantity = value

    def CalculateSubtotal():
        pass
    def GetOrderDetailInfo():
        pass
    def UpdateQuantity():
        pass
    def AddDiscount():
        pass

class Inventory:
    def __init__(self, inventory_id: int, product: Products, quantity_in_stock, last_stock_update):
        self.__InventoryID = inventory_id
        self.__Product = product
        self.__QuantityInStock = quantity_in_stock
        self.__LastStockUpdate = last_stock_update

    def get_inventory_id(self) -> int:
        return self.__InventoryID
    def set_inventory_id(self, value: int):
        self.__InventoryID = value
    
    def get_product(self) -> Products:
        return self.__Product
    def set_product(self, value: Products):
        self.__Product = value
    
    def get_quantity_in_stock(self) -> int:
        return self.__QuantityInStock
    def set_quantity_in_stock(self, value: int):
        if value>0:
            self.__QuantityInStock = value
    
    def get_last_stock_update(self) -> datetime:
        return self.__LastStockUpdate
    def set_last_stock_update(self, value: datetime):
        self.__LastStockUpdate = value

    def GetProduct():
        pass
    def GetQuantityInStock():
        pass
    def AddToInventory(quantity: int):
        pass
    def RemoveFromInventory(quantity: int):
        pass
    def UpdateStockQuantity(newQuantity: int):
        pass
    def IsProductAvailable(quantityToCheck: int):
        pass
    def GetInventoryValue():
        pass
    def ListLowStockProducts(threshold: int):
        pass
    def ListOutOfStockProducts():
        pass
    def ListAllProducts():
        pass


