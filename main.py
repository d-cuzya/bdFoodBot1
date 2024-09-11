#file  -- main.py --
import sqliteEz

def main():
    # Объект класса
    bd = sqliteEz.sqliteEz()

    #bd.getGroductsID()[i][0] - для парсинга
    print(bd.getProductsID())
    print(bd.getFoodMenuID())
    print(bd.getUserListID())
    print(bd.getCartID())
    print(bd.getProguctName(1))
    print(bd.getProguctDescription(1))
    print(bd.getProguctPrice(1))
    print(bd.getProguctImage(1))
if __name__ == "__main__":
    main()