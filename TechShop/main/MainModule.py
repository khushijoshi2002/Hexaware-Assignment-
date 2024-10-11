import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from entity.model import Customers
from dao.TechShopProcessor import TechShopProcessor
from util.db_util import DBUtil
from exception import custom_exceptions
class TechShop:
    @staticmethod
    def main():
        while True:
            print('\nMENU')
            print('-----------------')
            print('1. Customer Registration')
            print('2. Product Catalog Management')
            print('3. Orders')
            print('4. Order Status')
            print('5. Inventory Management')
            print('6. Sales Report')
            print('7. Customer Account Update')
            print('8. Payment Processing')
            print('9. Search and Recommend a Product')
            print('10. Exit\n')

            choice = int(input('Enter your Choice: '))

            if choice == 1:
                TechShop.customer_registration()
            elif choice == 2:
                TechShop.product_catalog_management()
            elif choice == 3:
                TechShop.orders()
            elif choice == 4:
                TechShop.order_status()
            elif choice == 5:
                TechShop.inventory_management()
            elif choice == 6:
                TechShop.sales_report()
            elif choice == 7:
                TechShop.customer_account_update()
            elif choice == 8:
                TechShop.payment_processing()
            elif choice == 9:
                TechShop.search_or_recommend_product()
            elif choice == 10:
                print('Exiting...')
                break
            else:
                print('Invalid Choice. Please try Again\n')

    def customer_registration():
        # Take customer details
        first_name = input('Enter your First Name: ')
        last_name = input('Enter your Last Name: ')
        try:
            email = input('Enter your Email: ')
            if '@' not in email:
                raise custom_exceptions.InvalidDataException('Invalid Email "@ is not Mentioned!"')
        except custom_exceptions.InvalidDataException as e:
            print(e)
            return
        phone = input('Enter your Phone Number: ')
        address = input('Enter your Address: ')

        customer = Customers("", first_name, last_name, email, phone, address)
        TechShopProcessor().CustomerRegistration(customer)


    def product_catalog_management():
        while True:
            print('\n1. Update Product Details')
            print('2. Show All Products')
            print('3. Search for Product in Stock')
            print('4. Exit')
            choice = int(input('Enter your Choice: '))
            if choice == 4:
                print('Redirecting to Main Menu...\n')
                break
            else:
                TechShopProcessor().ProductCatalog(choice)

    def orders():
        while True:
            print('\n1. Create Order')
            print('2. Get Order Details')
            print('3. Cancel Order')
            print('4. Delete Orders which are Cancelled')
            print('5. Exit')
            choice = int(input('Enter your Choice: '))
            if choice == 5:
                print('Redirecting to Main Menu...\n')
                break
            else:
                TechShopProcessor().Orders(choice)

    def order_status():
        order_id = int(input('Enter Order ID: '))
        while True:
            print('\n1. Display Order Status')
            print('2. Change Order Status')
            print('3. Exit')
            choice = int(input('Enter your Choice: '))
            if choice == 3:
                print('Redirecting to Main Menu...\n')
                break
            else:
                TechShopProcessor().OrderStatus(order_id, choice)

    def inventory_management():
        while True:
            print("\n1. Add New Product")
            print("2. Update Product Stock")
            print("3. Remove Discontinued Product")
            print("4. Exit")
            choice = int(input("Enter your Choice: "))
            if choice == 4:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopProcessor().InventoryManagement(choice)

    def sales_report():
        while True:
            print('\n1. Retrieve Sales Data')
            print('2. Generate Sales Report')
            print('3. Exit')
            choice = int(input('Enter your Choice: '))
            if choice == 3:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopProcessor().SalesReport(choice)

    def customer_account_update():
        while True:
            print("\n1. Update Customer Details")
            print("2. Get Customer Details")
            print("3. Exit")
            choice = int(input("Enter your Choice: "))
            if choice == 3:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopProcessor().CustomerUpdate(choice)
            
    def payment_processing():
        while True:
            print('\n1. Process Payment')
            print('2. Add Discount')
            print('3. Exit')
            choice = int(input('Enter your Choice:'))
            if choice == 3:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopProcessor().PaymentProcess(choice)
            
    def search_or_recommend_product():
        while True:
            print('\n1. Search Product')
            print('2. Recommend Product')
            print('3. Exit')
            choice = int(input('Enter your Choice: '))
            if choice == 3:
                print('Redirecting to Main Menu...')
                break
            else:
                TechShopProcessor().SearchOrRecommendProduct(choice)

if __name__ == '__main__':
    TechShop.main()

    