--Task1
--1.
create database TechShop;
use Techshop;

--4.
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1000,1),
    ProductName VARCHAR(100) NOT NULL,
    Description VARCHAR(MAX),
    Price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(100,1),
    CustomerID INT FOREIGN KEY REFERENCES Customers(CustomerID),
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL
);

CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY IDENTITY(10000,1),
    OrderID INT FOREIGN KEY REFERENCES Orders(OrderID),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    Quantity INT   
);

CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY IDENTITY(100000,1),
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    QuantityInStock INT NOT NULL,
    LastStockUpdate DATE NOT NULL
);

--5.
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES
('Khushi', 'Joshi', 'khushijoshi@gmail.com', '9876543210', '123, Sector 17, Indore, Madhya Pradesh'),
('Allu', 'Arjun', 'alluarjun@example.com', '8765432109', '456, Vijay Nagar, Bhopal, Madhya Pradesh'),
('Suryakumar', 'Yadav', 'suryakumaryadav@example.com', '7654321098', '789, Old City, Jaipur, Rajasthan'),
('Yash', 'Agrawal', 'yashagrawal@example.com', '6543210987', '1011, New Colony, Delhi, Delhi'),
('Prabhas', 'Raju', 'prabhasraju@example.com', '5432109876', '1234, Model Town, Mumbai, Maharashtra'),
('Piyush', 'Menaria', 'piyushmenaria@example.com', '4321098765', '5678, Banjara Hills, Hyderabad, Telangana'),
('Nishtha', 'Kaigaonkar', 'nishthakaigaonkar@example.com', '3210987654', '9012, Indiranagar, Bengaluru, Karnataka'),
('Vibhuti', 'Jain', 'vibhutijain@example.com', '2109876543', '1314, Salt Lake City, Kolkata, West Bengal'),
('Akshay', 'Kumar', 'akshaykumar@example.com', '1098765432', '1516, Beach Road, Chennai, Tamil Nadu'),
('Dharmesh', 'Yelande', 'dharmeshyelande@example.com', '9876543210', '1718, MG Road, Kochi, Kerala');

INSERT INTO Products (ProductName, Description, Price) VALUES
('iPhone 16 Pro', '6.1-inch Super Retina XDR display, A16 Bionic chip, 12MP dual camera system', 129999.00),
('Samsung Galaxy S24 Ultra', '6.8-inch Dynamic AMOLED 2X display, Snapdragon 8 Gen 2, 200MP camera', 119999.00),
('OnePlus 11', '6.7-inch Fluid AMOLED display, Snapdragon 8 Gen 2, 50MP camera', 59999.00),
('Xiaomi 13 Pro', '6.7-inch AMOLED display, Snapdragon 8 Gen 2, 50MP camera', 69999.00),
('Google Pixel 7 Pro', '6.7-inch LTPO OLED display, Google Tensor G2, 50MP camera', 84999.00),
('MacBook Pro M2', '13.3-inch Liquid Retina XDR display, M2 chip, 8GB RAM, 256GB SSD', 149999.00),
('Dell XPS 13', '13.4-inch InfinityEdge display, Intel Core i7-13700H, 16GB RAM, 512GB SSD', 129999.00),
('Lenovo ThinkPad X1 Carbon', '14-inch OLED display, Intel Core i7-13600H, 16GB RAM, 512GB SSD', 139999.00),
('HP Spectre x360', '13.3-inch AMOLED display, Intel Core i7-13600H, 16GB RAM, 512GB SSD', 129999.00),
('Acer Predator Helios 16', '16-inch IPS display, Intel Core i9-13900HX, 32GB RAM, 2TB SSD', 179999.00);

INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES
(1, '2023-11-25', 129999.00),
(2, '2023-12-01', 59999.00),
(3, '2023-12-10', 69999.00),
(4, '2023-12-15', 149999.00),
(5, '2023-12-20', 119999.00),
(6, '2023-12-25', 84999.00),
(7, '2024-01-01', 129999.00),
(8, '2024-01-05', 139999.00),
(9, '2024-01-10', 179999.00),
(10, '2024-01-15', 129999.00);


INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES
(100, 1000, 1),
(101, 1001, 1),
(102, 1002, 1),
(103, 1003, 1),
(104, 1004, 1),
(105, 1005, 1),
(106, 1006, 1),
(107, 1007, 1),
(108, 1008, 1),
(109, 1009, 1);

INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES
(1000, 10, '2023-12-31'),
(1001, 15, '2023-12-31'),
(1002, 20, '2023-12-31'),
(1003, 5, '2023-12-31'),
(1004, 8, '2023-12-31'),
(1005, 12, '2023-12-31'),
(1006, 7, '2023-12-31'),
(1007, 11, '2023-12-31'),
(1008, 6, '2023-12-31'),
(1009, 9, '2023-12-31');

--Task2
--1
SELECT FirstName, LastName, Email 
FROM Customers;

--2
Select OrderDate, FirstName, LastName from Orders, Customers 
Where Orders.CustomerID = Customers.CustomerID;

--3.
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
VALUES ('Pihu', 'Mehta', 'mehtapihu@example.com', '1234567890', '456,Besatan,Surat, Gujrat');
select * from Customers;

--4.
UPDATE Products
SET Price = Price * 1.10;
select * from Products;

--5
declare @orderid int=102
DELETE FROM OrderDetails
WHERE OrderID = @orderid;
DELETE FROM Orders
WHERE OrderID = @orderid;
select * from OrderDetails;

--6.
INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
VALUES (1, '2024-09-20', 79999.00);
select * from Orders;

INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES
(110, 1009, 1);

--7.
UPDATE Customers
SET Email = 'newemail@example.com',
    Address = '789, New Address, City, State'
WHERE CustomerID = 3;
select * from Customers;

--8.
UPDATE Orders
SET TotalAmount = (
    SELECT (od.Quantity * p.Price)
    FROM OrderDetails od
    JOIN Products p ON od.ProductID = p.ProductID
    WHERE od.OrderID = Orders.OrderID
);
select * from Orders;

--9.
DECLARE @CustomerID INT = 6
DELETE FROM OrderDetails
WHERE OrderID IN (
    SELECT OrderID
    FROM Orders
    WHERE CustomerID = @CustomerID
);
DELETE FROM Orders
WHERE CustomerID = @CustomerID;
select * from OrderDetails;

--10.
INSERT INTO Products (ProductName, Description, Price)
VALUES ('Smartwatch X200', 'A high-end smartwatch with various health tracking features and a sleek design.', 19999.00);
select * from Products;

--11.
ALTER TABLE Orders
ADD Status VARCHAR(50);
UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 100;
UPDATE Orders SET Status = 'Pending' WHERE OrderID = 101;
UPDATE Orders SET Status = 'Pending' WHERE OrderID = 103;
UPDATE Orders SET Status = 'Delivered' WHERE OrderID = 106;
UPDATE Orders SET Status = 'Processing' WHERE OrderID = 107;
UPDATE Orders SET Status = 'Cancelled' WHERE OrderID = 108;
UPDATE Orders SET Status = 'Cancelled' WHERE OrderID = 109;
UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 110;
UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 104;
select * from Orders;

DECLARE @OrderID INT = 101
DECLARE @NewStatus VARCHAR(50) = 'shipped'
UPDATE Orders
SET Status = @NewStatus
WHERE OrderID = @OrderID;
select * from Orders;

--12.
ALTER TABLE Customers
ADD OrderCount INT DEFAULT 0;
UPDATE Customers
SET OrderCount = (
    SELECT COUNT(*)
    FROM Orders
    WHERE Orders.CustomerID = Customers.CustomerID
);
select * from Customers;


select * from OrderDetails;
select * from Orders;
select * from Products;
select * from Inventory;

--Task3
--1.
SELECT O.OrderID, O.OrderDate, O.TotalAmount, C.FirstName, C.LastName, C.Email, C.Phone
FROM Orders AS O
JOIN Customers AS C ON O.CustomerID = C.CustomerID;

--2.
SELECT P.ProductName, SUM(OD.Quantity * P.Price) AS TotalRevenue
FROM OrderDetails AS OD
JOIN Products AS P ON OD.ProductID = P.ProductID
GROUP BY P.ProductName;


SELECT C.CustomerID, C.FirstName, C.LastName, C.Email, C.Phone, C.Address
FROM Customers AS C
JOIN Orders AS O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName, C.Email, C.Phone, C.Address;

--3.
SELECT C.FirstName, C.LastName, C.Email, C.Phone
FROM Customers AS C
JOIN Orders AS O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName, C.Email, C.Phone;

--4.
SELECT top 1 p.ProductName, 
       SUM(od.Quantity) AS TotalQuantityOrdered
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
JOIN Inventory i ON p.ProductID = i.ProductID
WHERE i.QuantityInStock > 0
GROUP BY p.ProductName
ORDER BY TotalQuantityOrdered DESC;

--5.
ALTER TABLE Products
ADD Categories VARCHAR(255);
UPDATE Products
SET Categories = 'Smartphones'
WHERE ProductID IN (1000, 1001, 1002, 1003, 1004);  
UPDATE Products
SET Categories = 'Laptops'
WHERE ProductID IN (1005, 1006, 1007, 1008, 1009);  
UPDATE Products
SET Categories = 'Smartwatches'
WHERE ProductID = 1010;

SELECT ProductName,
       Categories AS CategoryName
FROM Products;

--6.
SELECT c.FirstName,
       c.LastName,
       AVG(o.TotalAmount) AS AverageOrderValue
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName;

--7.
SELECT o.OrderID,
       c.FirstName,
       c.LastName,
       c.Email,
       c.Phone,
       o.TotalAmount AS TotalRevenue
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.TotalAmount = (
    SELECT MAX(TotalAmount)
    FROM Orders
);

--8.
SELECT p.ProductName,
       COUNT(od.OrderID) AS NumberOfOrders
FROM Products p
LEFT JOIN OrderDetails od ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.ProductName;

--9.
DECLARE @ProductName NVARCHAR(255) = 'iPhone 16 Pro';
SELECT DISTINCT c.CustomerID,
                c.FirstName,
                c.LastName,
                c.Email,
                c.Phone
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = @ProductName;

--10.
DECLARE @StartDate DATE = '2023-11-01';  
DECLARE @EndDate DATE = '2023-12-31';    
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders
WHERE OrderDate BETWEEN @StartDate AND @EndDate;

--task4
--1.
SELECT c.CustomerID, c.FirstName, c.LastName, c.Email, c.Phone, c.Address
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;

--2.
SELECT SUM(QuantityInStock) AS TotalProductsAvailable
FROM Inventory;

select * from orders;

--3.
SELECT SUM(TotalAmount) AS TotalRevenue
FROM Orders
WHERE Status IN ('Delivered', 'Shipped');

select * from Products;

--4.
SELECT p.Categories, AVG(od.Quantity) AS AvgQuantityOrdered
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
WHERE p.Categories = 'Laptops'  
GROUP BY p.Categories;

--5.
DECLARE @customerID INT;
SET @customerID = 9;  
SELECT c.CustomerID, CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, SUM(o.TotalAmount) AS TotalRevenue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE c.CustomerID = @customerID
GROUP BY c.CustomerID, c.FirstName, c.LastName;

--6.
SELECT c.CustomerID, CONCAT(c.FirstName, ' ', c.LastName) AS CustomerName, COUNT(o.OrderID) AS OrderCount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY OrderCount DESC;

--7.
SELECT TOP 1 p.Categories, SUM(od.Quantity) AS TotalQuantityOrdered
FROM Products p
JOIN OrderDetails od ON p.ProductID = od.ProductID
GROUP BY p.Categories
ORDER BY TotalQuantityOrdered DESC;

--8.
SELECT TOP 1 C.FirstName, C.LastName, SUM(OD.Quantity * P.Price) AS TotalSpent
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
JOIN OrderDetails OD ON O.OrderID = OD.OrderID
JOIN Products P ON OD.ProductID = P.ProductID
GROUP BY C.FirstName, C.LastName
ORDER BY TotalSpent DESC;

--9.
SELECT C.CustomerID, C.FirstName, C.LastName, AVG(O.TotalAmount) AS AverageOrderValue
FROM Customers C
JOIN Orders O ON C.CustomerID = O.CustomerID
GROUP BY C.CustomerID, C.FirstName, C.LastName;

--10.
SELECT 
    c.FirstName, 
    c.LastName, 
    c.OrderCount as TotalOrders
FROM 
    Customers c
ORDER BY 
    TotalOrders DESC;


select FirstName, LastName, OrderCount from Customers
order by ordercount desc;

select * from Orders;
