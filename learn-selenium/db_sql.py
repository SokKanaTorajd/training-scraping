import pymysql

class SQLDatabase():
    def __init__(self):
        self.db = None
        self.cursor = None
        self.host = 'localhost'
        self.user = 'root'
        self.pwd = ''
        self.db_name = 'train_scraping'

    def open_conn(self):
        """
        open database connection
        """
        self.db = pymysql.connect(
            host=self.host,user=self.user,
            password=self.pwd,db=self.db_name
        )
        self.cursor = self.db.cursor()
    
    def close_conn(self):
        """
        close database connection
        """
        self.db.close()
    
    def get_urls(self):
        self.open_conn()
        q = "SELECT * FROM url"
        self.cursor.execute(q)
        urls = self.cursor.fetchall()
        self.close_conn()
        return urls

    def add_url(self, data):
        self.open_conn()
        q = f"INSERT INTO url(result_url) values ({data})"
        self.cursor.execute(q)
        self.db.commit()
        self.close_conn()

    def add_detail_url(self, data):
        self.open_conn()
        q = f"INSERT INTO detail_url(product_title,	product_price, product_code, shop_name) \
            values ({data[0]}, {data[1]}, {data[2]}, {data[3]})"
        self.cursor.execute(q)
        self.db.commit()
        self.close_conn()
