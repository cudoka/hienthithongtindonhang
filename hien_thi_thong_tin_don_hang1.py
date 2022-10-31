sotien = int(input("Nhập vào tổng giá trị đơn hàng: "))
if(sotien >= 150):
    print("Số tiền thanh toán: ", sotien -50)
elif(sotien >= 100):
    print("Số tiền thanh toán: ", sotien - 25)
elif(sotien >= 75):
    print("Số tiền thanh toán: ", sotien - 15)
else:
    print("Số tiền thanh toán: ", sotien)