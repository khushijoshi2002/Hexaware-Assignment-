import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from dao.TechShopRepository import ITechShopRepository
from util.db_util import DBUtil
from entity.model import Products, Customers, OrderDetails, Orders
from datetime import date, datetime
from exception import custom_exceptions


class TechShopProcessor(ITechShopRepository):
    def CustomerRegistration(self, customer):
        try:
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()
            cursor.execute("SELECT TOP 1 CustomerID FROM Customers ORDER BY CustomerID DESC")
            customer_id = cursor.fetchone()[0]+1
            cursor.execute("""INSERT INTO Customers (FirstName, LastName, Email, Phone, Address)
                           VALUES ( ?, ?, ?, ?, ?)""", ( customer.get_first_name(), 
                                                          customer.get_last_name(), customer.get_email(), 
                                                          customer.get_phone(), customer.get_address()))
            conn.commit()
            print('Customer Created Successfully.\n')
        except custom_exceptions.InvalidDataException as e:
            conn.rollback()
            print(e)
        finally:
            cursor.close()
            conn.close()
    
    def ProductCatalog(self, choice):
        # Your implementation for ProductCatalog
        def check_product_exists(product_id):
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("""SELECT COUNT(*) FROM Products 
                               WHERE ProductID = ? """, (product_id,))
                count = cursor.fetchone()[0]
                cursor.close()
                return count>0

        def update_product_info():
                product_id = int(input('Enter Product ID: '))
                if check_product_exists(product_id):
                    conn = DBUtil.getDBConn()
                    cursor = conn.cursor()
                    print("What do you want to Update?\n1)Price\n2)Description\n3)Product Name\n4)Category")
                    choice = input("Enter Choice (eg; Price): ")
                    if choice == 'Price':
                        price = float(input('Enter Updated Price: '))
                        cursor.execute(""" UPDATE Products SET Price = ?
                                   WHERE ProductID = ?""",
                                   (price,product_id))
                    elif choice == 'Description':
                        desc = input('Enter Updated Description: ')
                        cursor.execute(""" UPDATE Products SET Description = ?
                                   WHERE ProductID = ?""",
                                   (desc,product_id))
                    elif choice == 'Product Name':
                        Pname = input('Enter Updated Product Name: ')
                        cursor.execute(""" UPDATE Products SET ProductName = ?
                                   WHERE ProductID = ?""",
                                   (Pname,product_id))
                    elif choice == 'Category':
                        category = input('Enter Updated Category: ')
                        cursor.execute(""" UPDATE Products SET Category = ?
                                   WHERE ProductID = ?""",
                                   (category,product_id))
                    else:
                        print("Enter Valid Choice, Try Again!!")
                        return
                    conn.commit()
                    cursor.close()
                    print('Product Information Updated Successfully')
                else:
                    print('Product Not found')
                    
        def show_all_products():
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM Products")
                print("Product Details:")
                for row in cursor.fetchall():
                    print(row)
            finally:
                cursor.close()
                conn.close()

        def product_in_stock():
            product_id = int(input('Enter Product ID: '))
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?", (product_id,))
                quantity = cursor.fetchone()[0]
                if quantity>0:
                    print(f'Product in Stock: {quantity}')
                else:
                    print('Product not in Stock')
            except TypeError as e:
                print("Product not Added in Inventory!")
            finally:
                cursor.close()
                conn.close()


        if choice == 1:
            update_product_info()
        elif choice == 2:
            show_all_products()
        elif choice == 3:
            product_in_stock()
        else:
            print('Invalid Choice. Please Try Again!!')

    def Orders(self, choice):

        def CreateOrder():
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()

                customer_id = int(input('Enter Customer ID: '))
                product_id = int(input('Enter Product ID: '))
                quantity = int(input('Enter Quantity: '))
                order_date = date.today()
                if not product_id or not quantity:
                    raise custom_exceptions.IncompleteOrderException("Enter All the Details")

                cursor.execute("SELECT Price FROM Products WHERE ProductID = ?", (product_id,))
                row = cursor.fetchone()
                if row:
                    price = row[0]
                    total_amount = price * quantity
                else:
                    raise custom_exceptions.ProductNotFoundException('Product Not Found')

                #Insert order into Orders Table
                default_status = 'Pending'
                cursor.execute("""INSERT INTO Orders VALUES(?, ?, ?, ?);""", (customer_id, str(order_date), total_amount, default_status))
                
                cursor.execute("SELECT TOP 1 OrderID FROM Orders ORDER BY OrderID DESC")
                order_id = cursor.fetchone()[0]
                # Insert order details into OrderDetails Table
                cursor.execute(""" INSERT INTO OrderDetails
                               VALUES(?, ?, ?);""", (order_id, product_id, quantity))
                # Update quantity in stock in Inventory Table
                cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?",(product_id,))
                current_quantity = cursor.fetchone()[0]
                if current_quantity:
                    new_quantity = current_quantity - quantity
                    cursor.execute(""" UPDATE Inventory SET QuantityInStock = ?
                                WHERE ProductID = ?;""", (new_quantity, product_id))
                    conn.commit()
                    print('Order Created Successfully')
                else:
                    raise custom_exceptions.InsufficientStockException('Insufficient Stock')
            except custom_exceptions.ProductNotFoundException as e:
                print(e)
            except custom_exceptions.InsufficientStockException as e:
                print(e)
            except custom_exceptions.IncompleteOrderException as e:
                print(e)
            except Exception as e:
                conn.rollback()
                print('Error Creating Order', e)
            finally:
                cursor.close()
                conn.close()

        def GetOrderDetails():
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                customer_id = int(input('Enter Customer ID: '))
                cursor.execute("""SELECT OD.OrderDetailID, OD.OrderID, OD.ProductID, OD.Quantity, O.OrderDate, O.Status, O.TotalAmount 
                               FROM OrderDetails OD
                               JOIN Orders O ON O.OrderID = OD.OrderID
                               WHERE O.CustomerID = ?""", (customer_id,))
                orders = cursor.fetchall()
                print(f"\nYou've ordered {len(orders)} times, below are those Order Details:")
                for order in orders:
                    print()
                    print(f"Order Detail ID: {order[0]}")
                    print(f"Order ID: {order[1]}")
                    print(f"Product ID: {order[2]}")
                    print(f"Quantity: {order[3]}")
                    print(f"Order Date: {order[4]}")
                    print(f"Status: {order[5]}")
                    print(f"Total Order Price: {order[6]}")
                    print()
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def CancelOrder():
            print('FOR YOUR ALL ORDERS: \n')
            GetOrderDetails()
            order_id = int(input('Write an OrderID you want to Cancel: '))
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("UPDATE Orders SET Status = 'Cancelled' WHERE OrderID = ?", (order_id,))
                conn.commit()
                print('Order Cancelled...')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
        
        def DeleteCancelOrder():
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Orders WHERE Status = 'Cancelled';")
                value = cursor.fetchall()
                if value:
                    cursor.execute("DELETE FROM OrderDetails WHERE OrderID IN (Select OrderID FROM Orders WHERE Status = 'Cancelled');")
                    cursor.execute("DELETE FROM Orders WHERE Status = 'Cancelled';")
                    conn.commit()
                    print('Cancelled Orders Deleted!')
                else:
                    print("No Cancelled Orders Found!")
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        if choice == 1:
            CreateOrder()
        elif choice == 2:
            GetOrderDetails()
        elif choice == 3:
            CancelOrder()
        elif choice == 4:
            DeleteCancelOrder()
        else:
            print('Invalid Choice. Please Try again.')
            return

    def OrderStatus(self, order_id, choice):
        def DisplayStatus():
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT Status FROM Orders WHERE OrderID = ?", (order_id,))
                status = cursor.fetchone()[0]
                print("Your order status: ", status)
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def UpdateStatus():
            status = input('Enter Status (Shipped/Pending/Delivered/Cancelled): ').capitalize()
            if (status == ("Shipped") or status == ("Pending") or status == ("Delivered") or status == ("Cancelled")):
                try:
                    conn = DBUtil.getDBConn()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE Orders SET Status = ? WHERE OrderID = ?", (status, order_id))
                    print('Status Updated\n')
                    conn.commit()
                except Exception as e:
                    conn.rollback()
                    raise e
                finally:
                    cursor.close()
                    conn.close()
            else:
                print('Enter valid status. Try again')
                return
        if choice == 1:
            DisplayStatus()
        elif choice == 2:
            UpdateStatus()
        else:
            print('Invalid choice. Please Try again')
    

    def InventoryManagement(self, choice):

        def AddProduct():
            conn = DBUtil.getDBConn()
            cursor = conn.cursor()
            try:
                product_name = input('Enter Product Name: ')
                desc = input('Enter Product Description: ')
                price = float(input('Enter Product Price: '))
                category = input('Enter Product Category: ')
                quantity = int(input('Enter Quantity in Stock: '))
                last_stock_date = str(date.today())
                cursor.execute("INSERT INTO Products VALUES (?,?,?,?)",
                               (product_name, desc, price, category))
                cursor.execute('SELECT TOP 1 ProductID FROM Products ORDER BY ProductID DESC')
                product_id = cursor.fetchone()[0]
                cursor.execute("INSERT INTO Inventory VALUES (?,?,?);",
                                (product_id, quantity, last_stock_date))
                conn.commit()
                print('Product Added Succesfully')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def UpdateProductStock():
            product_id = int(input('Enter Product ID: '))
            new_quantity = int(input('Enter Quantity to be Added: '))
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = ?", (product_id,))
                quantity_in_stock = cursor.fetchone()[0]
                print('Quantity in Stock: ', quantity_in_stock)
                quantity = quantity_in_stock + new_quantity
                cursor.execute("UPDATE Inventory SET QuantityInStock = ? WHERE ProductID = ?", (quantity, product_id))
                print(f'Quantity Updated for Product ID {product_id}: {quantity}')
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def RemoveDiscontinuedItems():
            product_id = int(input('Enter Product you want to Discontinue (Product ID): '))
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id))
                count = cursor.fetchall()
                if count:
                    cursor.execute("DELETE FROM Inventory WHERE ProductID = ?",(product_id))
                    cursor.execute("DELETE FROM Products WHERE ProductID = ?",(product_id))
                    conn.commit()
                    print('Removed Items Successfully!!')
                else:
                    print("Product Not Found!!, Try Again.")
                    return
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
        if choice == 1:
            AddProduct()
        elif choice == 2:
            UpdateProductStock()
        elif choice == 3:
            RemoveDiscontinuedItems()
        else:
            print('Invalid choice. Please Try again')

    def SalesReport(self, choice):
        def RetrieveSalesData():
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                query = """WITH ProductSales AS(
                            SELECT OD.ProductID, SUM(OD.Quantity) Quantity FROM OrderDetails OD
                            GROUP BY OD.ProductID
                        )
                        SELECT P.ProductID, P.ProductName, PS.Quantity AS TotalQuantity
                        FROM Products P
                        JOIN ProductSales PS ON PS.ProductID = P.ProductID"""
                cursor.execute(query)
                rows = cursor.fetchall()

                print("Sales Report:")
                print("Product ID | Product Name | Total Quantity Sold")
                for row in rows:
                    print(f"{row.ProductID} | {row.ProductName} | {row.TotalQuantity}")
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def GenerateSalesReport():
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                query = """WITH ProductSales AS(
                            SELECT OD.ProductID, SUM(OD.Quantity) Quantity 
                            FROM OrderDetails OD
                            GROUP BY OD.ProductID
                        )
                        SELECT P.ProductID, P.ProductName, PS.Quantity AS TotalQuantity FROM Products P
                        JOIN ProductSales PS ON PS.ProductID = P.ProductID
                        WHERE PS.Quantity = (SELECT MAX(Quantity) FROM ProductSales) OR 
                        PS.Quantity = (SELECT MIN(Quantity) FROM ProductSales)
                        """
                cursor.execute(query)
                rows = cursor.fetchall()

                print("Sales Report:")
                print("Product ID | Product Name | Total Quantity Sold")
                for row in rows:
                    print(f"{row.ProductID} | {row.ProductName} | {row.TotalQuantity}")
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        if choice == 1:
            RetrieveSalesData()
        elif choice == 2:
            GenerateSalesReport()
        else:
            print('Invalid choice. Try again')
            return

    def CustomerUpdate(self, choice):
        def UpdateCustomerDetails():
            try:
                customer_id = int(input('Enter Customer ID: '))
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
                customer_details = cursor.fetchone()
                if customer_details:
                    print("What do you want to Update?\n1)First Name\n2)Last Name\n3)Email\n4)Phone Number\n5)Address\n6)Want to Update All Details")
                    choice = int(input("Enter Choice: "))
                    if choice == 1:
                        fname = input('Enter Updated First Name: ')
                        cursor.execute("""UPDATE Customers SET FirstName = ?
                                     WHERE CustomerID = ?""",
                                 (fname, customer_id))
                    elif choice == 2:
                        lname = input('Enter Updated Last Name: ')
                        cursor.execute("""UPDATE Customers SET LastName = ?
                                     WHERE CustomerID = ?""",
                                 (lname, customer_id))
                    elif choice == 3:
                        try:
                            email = input('Enter New Email: ')
                            if '@' not in email:
                                raise custom_exceptions.InvalidDataException('Invalid Email "@ is not mentioned!"')
                        except custom_exceptions.InvalidDataException as e:
                            print(e)
                            return
                        cursor.execute("""UPDATE Customers SET Email = ?
                                     WHERE CustomerID = ?""",
                                 (email, customer_id))
                    elif choice == 4:
                        phone = input('Enter New Phone Number: ')
                        cursor.execute("""UPDATE Customers SET Phone = ?
                                     WHERE CustomerID = ?""",
                                 (phone, customer_id))
                    elif choice == 5:
                        address = input('Enter New Address: ')
                        cursor.execute("""UPDATE Customers SET Address = ?
                                     WHERE CustomerID = ?""",
                                 (address, customer_id))
                    elif choice == 6:
                        fname = input('Enter Updated First Name: ')
                        lname = input('Enter Updated Last Name: ')
                        try:
                            email = input('Enter New Email: ')
                            if '@' not in email:
                                raise custom_exceptions.InvalidDataException('Invalid Email "@ is not mentioned!"')
                        except custom_exceptions.InvalidDataException as e:
                            print(e)
                            return
                        phone = input('Enter New Phone Number: ')
                        address = input('Enter New Address: ')
                        cursor.execute("""UPDATE Customers SET FirstName = ?, LastName = ?, Email = ?, Phone = ?, Address = ?
                                    WHERE CustomerID = ?""", (fname, lname, email, phone, address, customer_id))
                    conn.commit()
                    print("Customer Details Updated!")
                else:
                    print("Customer Not Found!! Try Again.")
                    return
            except Exception as e:
                conn.rollback()
                raise e
            finally: 
                cursor.close()
                conn.close()

            
        def GetCustomerDetails():
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                customer_id = int(input('Enter Customer ID: '))
                cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id, ))
                detail = cursor.fetchone()
                print('Customer ID: ', detail[0])
                print('First Name: ', detail[1])
                print('Last Name: ', detail[2])
                print('Email: ', detail[3])
                print('Phone: ', detail[4])
                print('Address: ', detail[5])
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
                
        
        if choice == 1:
            UpdateCustomerDetails()
        elif choice == 2:
            GetCustomerDetails()
        else:
            print("Invalid choice. Try again\n")


    def PaymentProcess(self, choice):

        def ProcessPayment():
            order_id = int(input('Enter Order ID: '))
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                query = """SELECT OD.OrderID, OD.ProductID, OD.Quantity, SUM(P.Price * OD.Quantity) TotalAmount FROM OrderDetails OD
                        JOIN Products P ON P.ProductID = OD.ProductID
                        WHERE OrderID = ?
                        GROUP BY OD.OrderID, OD.ProductID, OD.Quantity"""
                cursor.execute(query, (order_id,))
                rows = cursor.fetchall()
                if not rows:
                    print("No Order Details Found for the Given Order ID!!")
                else:
                    print("OrderID | ProductID | Quantity | TotalAmount")
                    print("-" * 40)
                    for row in rows:
                        order_id, product_id, quantity, total_amount = row
                        print(f"{order_id:^8} | {product_id:^9} | {quantity:^8} | {total_amount:^12}")
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()

        def AddDiscount():
            order_id = int(input('Enter Order ID: '))
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                query = """SELECT OD.OrderID, SUM(P.Price * OD.Quantity) TotalAmount FROM OrderDetails OD
                            JOIN Products P ON P.ProductID = OD.ProductID
                            WHERE OrderID = ?
                            GROUP BY OD.OrderID"""
                cursor.execute(query, (order_id,))
                total_amount = float(cursor.fetchone()[1])
                print("Total Amount: Rs.",total_amount)
                discounted_amount = total_amount - total_amount*0.10
                print("Discount of 10 percent will be added...")
                print("Total Amount: Rs.", discounted_amount)
            except Exception as e:
                conn.commit()
                raise e
            finally:
                cursor.close()
                conn.close()
        if choice == 1:
            ProcessPayment()
        elif choice == 2:
            AddDiscount()
        else:
            print('Invalid choice. Try again')
            return

    def SearchOrRecommendProduct(self, choice):
        
        def SearchProduct():
            product_id = input('Enter a Product ID: ')
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Products WHERE ProductID = ?", (product_id,))
                rows = cursor.fetchone()
                if rows:
                    print('Product Found!\n')
                    print('Product ID: ', rows[0])
                    print('Product Name: ', rows[1])
                    print('Product Description: ', rows[2])
                    print('Product Price: ', rows[3])
                    print('Product Category: ', rows[4])
                else:
                    print('Product Not Found!! Try Again.\n')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()
        
        def RecommendProduct():
            category = input('Enter a Product Category: ')
            try:
                conn = DBUtil.getDBConn()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Products WHERE Category = ?",(category))
                recommended_products = cursor.fetchall()

                if recommended_products:
                    print('Here are the Recommeded Products: \n')
                    for product in recommended_products:
                        print(product[1])
                else:
                    print('Sorry, No Recommendations Found!!')
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                cursor.close()
                conn.close()


        if choice == 1:
            SearchProduct()
        elif choice == 2:
            RecommendProduct()
        else:
            print('Invalid choice. try again')
            return