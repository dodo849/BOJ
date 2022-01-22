#2020010849 이도연
mouse = 12000
mouse_num = 5
keyboard = 18000
keyboard_num = 4
hdd = 85000
hdd_num = 2
total = mouse * mouse_num + keyboard * keyboard_num + hdd * hdd_num

#출력결과
print("     [상품구입 내역서]     ")
print("========================")
print("품명  단가  수량  금액    ")
print("마우스", mouse, mouse_num, mouse * mouse_num)
print("키보드", keyboard, keyboard_num, keyboard * keyboard_num)
print("HDD ", hdd, hdd_num, hdd * hdd_num)
print("========================")
print("총 지불액", total)

