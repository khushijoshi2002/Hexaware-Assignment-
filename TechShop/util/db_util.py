import pyodbc
class DBUtil:
    @staticmethod
    def getDBConn():
        # Specify the server name and the database name
        server = r'DESKTOP-4CBODPM\SQLEXPRESS01'
        database = 'TechShop'
        
        # Construct the connection string
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        
        try:
            # Establish the database connection
            conn = pyodbc.connect(conn_str)
            return conn
        except Exception as e:
            # Handle connection errors
            print(f"Error connecting to the database: {str(e)}")
            raise e
