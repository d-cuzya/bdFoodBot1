#file  -- sqliteEz.py --
import sqlite3

class sqliteEz:
    #Конструктор
    def __init__(self):
        #print("Конструктор")
        self.con = sqlite3.connect("FoodBot.db")
        self.cur = self.con.cursor()
        #Вкючние ссылок на другие таблицы
        self.cur.execute("PRAGMA foreign_keys = ON;")
        #Создание таблицы "Products"
        self.cur.execute("CREATE TABLE IF NOT EXISTS Products ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "Name TEXT NOT NULL, "
                         "Description TEXT, "
                         "Price INTEGER, "
                         "Img TEXT"
                         ");")
        #Создание таблицы "FoodMenu"
        self.cur.execute("CREATE TABLE IF NOT EXISTS FoodMenu ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "DayOfTheWeek TEXT NOT NULL, "
                         "ProductID INTEGER NOT NULL, "
                         "FOREIGN KEY (ProductID) REFERENCES Products (ID) "
                         ");")
        #Создание таблицы "UserList"
        self.cur.execute("CREATE TABLE IF NOT EXISTS UserList ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "FirstName TEXT NOT NULL, "
                         "SecondName TEXT NOT NULL, "
                         "Username TEXT NOT NULL, "
                         "UserId TEXT NOT NULL, "
                         "Admin INTEGER NOT NULL DEFAULT 0"
                         ");")
        #Создание таблицы "Cart"
        self.cur.execute("CREATE TABLE IF NOT EXISTS Cart ("
                         "ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                         "UserID INTEGER NOT NULL,"
                         "DayOfTheWeek TEXT NOT NULL,"
                         "FOREIGN KEY (UserID) REFERENCES UserList (ID), "
                         "FOREIGN KEY (DayOfTheWeek) REFERENCES FoodMenu (DayOfTheWeek) "
                         ");")
        
        self.con.commit()
    
    #Деструктор
    def __del__(self):
        #print("Деструктор")
        self.con.close()

    #Функция добовления строки в таблицу Products
    def addProduct(self, _Name, _Description = "", _Price = "", _Img = ""):
        self.cur.execute("INSERT INTO Products (Name, Description, Price, Img) VALUES (?, ?, ?, ?);", (_Name, _Description, _Price, _Img))
        self.con.commit()
        
    #==Гетеры для таблицы Products
    #Возвращает массив айдишников из таблицы Products
    def getProductsID(self):
        return self.cur.execute("SELECT ID FROM Products;").fetchall()
    #Возвращает Name из Products
    def getProguctName(self, _idProduct):
        return self.cur.execute("SELECT Name FROM Products WHERE ID = ?;", (_idProduct,)).fetchall()[0][0]
    #Возвращает Description из Products
    def getProguctDescription(self, _idProduct):
        return self.cur.execute("SELECT Description FROM Products WHERE ID = ?;", (_idProduct,)).fetchall()[0][0]
    #Возвращает Price из Products
    def getProguctPrice(self, _idProduct):
        return self.cur.execute("SELECT Price FROM Products WHERE ID = ?;", (_idProduct,)).fetchall()[0][0]
    #Возвращает Image из Products
    def getProguctImage(self, _idProduct):
        return self.cur.execute("SELECT Img FROM Products WHERE ID = ?;", (_idProduct,)).fetchall()[0][0]

    #==Гетеры для FoodMenu
    #Возвращает массив айдишников из таблицы FoodMenu
    def getFoodMenuID(self):
        return self.cur.execute("SELECT ID FROM FoodMenu;").fetchall()
    #Возвращает DayOfTheWeek из Products
    def getFoodMenuDayOfTheWeek(self, _idProduct):
        return self.cur.execute("SELECT DayOfTheWeek FROM FoodMenu WHERE ID = ?;", (_idProduct,)).fetchall()
    #Возвращает DayOfTheWeek из Products
    def getFoodMenuProductID(self, _idProduct):
        return self.cur.execute("SELECT ProductID FROM FoodMenu WHERE ID = ?;", (_idProduct,)).fetchall()
    
    #==Гетеры для UserList
    #Возвращает массив айдишников из таблицы UserList
    def getUserListID(self):
        return self.cur.execute("SELECT ID FROM UserList;").fetchall()
    #Возвращает FirstName из UserList
    def getUserListFirstName(self, _idProduct):
        return self.cur.execute("SELECT FirstName FROM UserList WHERE ID = ?;", (_idProduct,)).fetchall()
    #Возвращает SecondName из UserList
    def getUserListSecondName(self, _idProduct):
        return self.cur.execute("SELECT SecondName FROM UserList WHERE ID = ?;", (_idProduct,)).fetchall()
    #Возвращает Username из UserList
    def getUserListUsername(self, _idProduct):
        return self.cur.execute("SELECT Username FROM UserList WHERE ID = ?;", (_idProduct,)).fetchall()
    #Возвращает UserID из UserList
    def getUserListUserID(self, _idProduct):
        return self.cur.execute("SELECT UserId FROM UserList WHERE ID = ?;", (_idProduct,)).fetchall()
    #Возвращает Admin из UserList
    def getUserListAdmin(self, _idProduct):
        return self.cur.execute("SELECT Admin FROM UserList WHERE ID = ?;", (_idProduct,)).fetchall()

    #==Гетеры для Cart
    #Возвращает массив айдишников из таблицы Cart
    def getCartID(self):
        return self.cur.execute("SELECT ID FROM Cart;").fetchall()
    #Возвращает UserID из Cart
    def getCartUserID(self, _idProduct):
        return self.cur.execute("SELECT UserID FROM Cart WHERE ID = ?;", (_idProduct,)).fetchall()
    #Возвращает DayOfTheWeek из Cart
    def getCartDayOfTheWeek(self, _idProduct):
        return self.cur.execute("SELECT DayOfTheWeek FROM Cart WHERE ID = ?;", (_idProduct,)).fetchall()


    #===Get Методы===
    #Получение значение колонки из таблицы с определённым условием 
    #_Table - название требуемой таблицы, _ColumnForCondition - Колонка к которому будет преминятся условие, _ValueForCondition - какое значение должно быть у колонки, _ReturnColumn - какую колонку вернуть
    #def getColumnValueByCondition(self, _Table, _ColumnForCondition, _ValueForCondition, _ReturnColumn):
    #    try:
    #        return self.cur.execute(f"SELECT \"{_ReturnColumn}\" FROM \"{_Table}\" WHERE \"{_ColumnForCondition}\" = \"{_ValueForCondition}\";", ()).fetchall()[0][0]
    #    except:
    #        return None
    #===Add Методы===
    
    #Функция добовления юзера
    #def addUser(self, _FirstName, _SecondName, _Username):
    #    self.cur.execute("INSERT INTO UserList (FirstName, SecondName, Username) VALUES (?, ?, ?);", (_FirstName, _SecondName))
    #    self.con.commit()
    #Функция добовления заказа
    #def addOrder(self, _FoodID, _UserID):
    #    try:
    #        self.cur.execute("INSERT INTO CurrentOrders (FoodID, UserID) VALUES (?, ?);", (_FoodID, _UserID))
    #        self.con.commit()
    #    except:
    #        return None
    #Функция добавляющая элемент в "FoodMenu"
    #def addItemInFoodMenu(self):
    #    self.cur.execute("INSERT INTO CurrentOrders (FoodID, UserID) VALUES (?, ?);", (_FoodID, _UserID))
    #
    #===Set Методы===
    #Функция перемещения заказа в history
    #def moveOrderToHistory(self, _OrderID):
        #try:
        #    self.cur.execute("INSERT INTO History (OrderID) VALUES (?) UNION UPDATE CurrentOrders SET PaidFor = 1, Completed = 1 WHERE ID = (?);", (_OrderID, _OrderID))
        #    self.con.commit()
        #except:
        #    return None