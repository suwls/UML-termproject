# -*- coding: utf -8 -*-

class Join :
    def __init__(self):
        self.id = input(" 사용자 아이디를 입력하시오: ")
        self.pw = int(input(" 사용자 비밀번호를 입력하시오. 단, 숫자로만 입력하시오: "))
        self.name = input(" 사용자 이름을 입력하시오: ")
        self.ph = input(" 사용자 전화번호를 입력하시오: ")
        self.address = input(" 사용자 주소를 입력하시오: ")
        self.email = input(" 사용자 이메일을 입력하시오: ")
        self.registration_number = input(" 사용자 주민등록 번호를 입력하시오: ")
        self.accountNumber = input(" 사용자 계좌번호를 입력하시오. ")
        self.myCart = {}
        print("")
        print(" 회원가입 완료 !")
        print("")

class Customer(Join):
    def __init__(self):
        super().__init__()

    def getUserID(self):
        return self.id

    def getShoppingCart(self):
        return self.myCart
    
    def resetShoppingCart(self):
        self.myCart.clear()

    def showShoppingCart(self):
        print(" ", self.name, "'s cart : " , list(self.myCart.keys()))
        print("")

class Product :
    def __init__(self):
        self.product_list = {"무스탕" : 5000, "패딩" : 5000, "라이더자켓" : 5000, "코트" : 5000, "후드" : 5000}
    
    def show_productlist(self) :
        print(" 상품 목록과 가격을 보여줍니다. ")
        for i in self.product_list.keys():
            print(" ",i, " : " ,self.product_list[i], "원" )
        print("")

    def search_product(self):
        good = input(" 원하는 상품을 입력하시오: ")
        print("")
        for name in self.product_list.keys() :
            if good == name :
                print(" 원하는 상품이 존재합니다! ")
                print(" 가격은 ", self.product_list[good], "원 입니다!")
                print("")
                return good, self.product_list[good]
        else :
            print(" 원하는 상품이 존재하지 않습니다! ")
            print("")
            return 0,0

class Shopping_Cart:
    def __init__(self, userID):
        self.userID = userID

    def enrollProduct(self, myCart, product_name, product_price):
        myCart[product_name] = product_price
        print(" ", product_name, " 이 쇼핑카트에 담겼습니다! ")

class Payment:
    def __init__(self, user_id) :
        self.user_id = user_id

    def pay(self, uesr_id, pay_means) :
        print("")
        print(" ", self.user_id, "님! 결제를 진행합니다." )

        if pay_means == "현금" :
            print(" 수단은 ", pay_means, " 입니다. ")
            print("")
            print( " 계좌번호 : 농협 000 - 0000 - 0000 - 00로 3일 안에 입금해주세요! ^ㅇ^ " )
            print("")
        else :
            print(" 수단은 ", pay_means, " 카드 입니다. ")
            print("")
            print( " 결제 완료 ! 3일 후 배송됩니다! ^ㅇ^ " )
            print("")

class Card_Payment(Payment) : # Payment를 상속
    def __init(self, user_id):
        super().__init__(user_id)

    def choose_bank(self):
        bank_list = [ '국민', '우리', '신한', 'IBK', '하나', '농협' ]
        print(" 결제를 희망하는 은행을 선택하시오: ", bank_list)
        bank = input(" 은행 선택 : ")
        return bank

    def pay(self, user_id, pay_means):
        super().pay(user_id, pay_means)

class Cash_Payment(Payment) : # Payment를 상속
    def __init(self, user_id):
        super().__init__(user_id)

    def pay(self, user_id, pay_means):
        super().pay(user_id, pay_means)

class Ui:
    def __init__(self):
        print("")
        print(" **************************************************** ")
        print("                                                      ")
        print(" *** Welcome to Byunghoon & Sujin's Shopping Mall *** ")
        print(" ***       First, Join our Shopping Mall          *** ")
        print("                                                      ")
        print(" **************************************************** ")
        print("")

    def cart_check(self):
        print(" 1. 장바구니 담기 / 2. 다른 상품 보기")
        num = int(input(" "))
        print("")
        return num

    def continue_check(self):
        print(" 1. 쇼핑 계속하기 / 2. 결제하기")
        num = int(input(" "))
        print("")
        return num

    def payment_check(self, object):
        print(" 결제를 진행합니다. ")
        print("")
        sum = 0
        for i in object.keys():
            sum += object[i]
        print("총 결제 금액은 ", sum ,"원 입니다.")
        print("")
        print( " 1. 카드 결제 / 2. 현금 결제 / 3. 결제 취소 ")
        num = int(input(" "))
        print("")
        return num

    def recheck_payment(self):
        print( " 정말 결제하시겠습니까? YES or NO ")
        check = input(" ")
        print("")
        return check

    def stop_check(self):
        print(" 계속 쇼핑을 하시겠습니까? YES / NO")
        check = input(" ")
        print("")
        return check

if __name__ == "__main__":
    Ui = Ui()
    C = Customer() # 고객 객체 생성

    while True :
        while True: # 장바구니
            product = Product()
            product.show_productlist()
            product_name, product_price = product.search_product()
            if not product_name == 0:
                shoppingCart_check = Ui.cart_check()
                if shoppingCart_check == 1:
                    Cart = Shopping_Cart( C.getUserID())
                    Cart.enrollProduct( C.getShoppingCart(), product_name, product_price)
                    C.showShoppingCart()
                    continue_check = Ui.continue_check()
                    if continue_check == 2:
                        break
    
        pay_check = Ui.payment_check(C.getShoppingCart())

        if pay_check == 1 : # 카드 결제
            cp = Card_Payment(C.getUserID())
            bank = cp.choose_bank()
            paycheck = Ui.recheck_payment()
            if paycheck == "YES" :
                cp.pay( C.getUserID(), bank)
                C.resetShoppingCart()
            else :
                print(" 결제를 진행하지 않습니다. ")
                print("")

        elif pay_check == 2 : # 현금 결제
            cp = Cash_Payment( C.getUserID() )
            paycheck = Ui.recheck_payment()
            if paycheck == "YES" :
                cp.pay( C.getUserID(), "현금" )
                C.resetShoppingCart()
            else :
                print(" 결제를 진행하지 않습니다. ")
                print("")

        else : # 결제 종료
            print(" 결제를 취소합니다.")
            print("")
    
        
        check = Ui.stop_check()
        if check == "YES" :
            print( " 쇼핑을 계속합니다! " )
            print( "" )
            continue
        else :
            print( " 이용해주셔서 감사합니다! " )
            print("")
            break
