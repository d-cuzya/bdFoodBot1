#file  -- main.py --
import sqliteEz

def main():
    # Объект класса
    bd = sqliteEz.sqliteEz()
    #addMetods
    

    #Гетеры
    #bd.getGroductsID()[i][0] - для парсинга
    print(bd.getProductsID())
    print(bd.getProguctName(1))
    print(bd.getProguctDescription(1))
    print(bd.getProguctPrice(1))
    print(bd.getProguctImage(1))

    print(bd.getFoodMenuID())
    print(bd.getFoodMenuDayOfTheWeek(1))
    print(bd.getFoodMenuProductID(1))

    print(bd.getUserListID())
    print(bd.getUserListFirstName(1))
    print(bd.getUserListSecondName(1))
    print(bd.getUserListUsername(1))
    print(bd.getUserListUserID(1))
    print(bd.getUserListAdmin(1))

    print(bd.getCartID())
    print(bd.getCartUserID(1))
    print(bd.getCartDayOfTheWeek(1))

if __name__ == "__main__":
    main()