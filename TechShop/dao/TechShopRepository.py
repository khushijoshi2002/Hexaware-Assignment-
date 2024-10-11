from abc import ABC, abstractmethod

class ITechShopRepository(ABC):
    @abstractmethod
    def CustomerRegistration(self, customer):
        pass
    
    @abstractmethod
    def ProductCatalog(self, choice):
        pass
    
    @abstractmethod
    def Orders(self, customer, choice):
        pass

    @abstractmethod
    def OrderStatus(self, order, choice):
        pass

    @abstractmethod
    def InventoryManagement(self, choice):
        pass

    @abstractmethod
    def SalesReport(self, choice):
        pass

    @abstractmethod
    def CustomerUpdate(self, customer, choice):
        pass

    @abstractmethod
    def PaymentProcess(self, choice):
        pass

    @abstractmethod
    def SearchOrRecommendProduct(self, choice):
        pass 