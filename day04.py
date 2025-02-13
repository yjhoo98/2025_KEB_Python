import random
def print_menu(num):
    print(f'{drinks[num]}에 어울리는 안주는 {drinks_foods[num]} 이고 가격은 {prices[num]}입니다.')
# d_s_p={"위스키":['초콜릿',50_000]}
# print(d_s_p["위스키"][1])
drinks=['위스키','와인','소주','고량주']
drinks_foods=['초콜릿','치즈','삼겹살','양꼬치']
prices=[50000,30000,5000,7500]
while True:
    ask = input(f'1)메뉴 추가 2)메뉴 삭제 3)변경없음:')
    if int(ask)==1:
        new_menu = input("주류와 안주 가격 입력:").split(' ')
        if new_menu[0]  in drinks:
            print('이미 있는 메뉴')
            continue
        else:
            drinks.append(new_menu[0])
            drinks_foods.append(new_menu[1])
            prices.append(int(new_menu[2]))
    elif int(ask)==2:
        del_menu = input("주류와 안주 가격 입력:").split(' ')
        if del_menu[0] not in drinks:
            print('존재하지 않는 메뉴')
            continue
        else:
            drinks.remove(del_menu[0])
            drinks_foods.remove(del_menu[1])
            prices.remove(int(del_menu[2]))

    elif int(ask)==3:
        print(f'변경없음.')
        break
print(drinks)


menu_list='다음 술중에 고르세요.\n'
for i in range(len(drinks_foods)):
    menu_list=menu_list+f'{i+1}){drinks[i]} '
menu_list=menu_list+f'{len(drinks)+1}) 아무거나 {len(drinks)+2}) 종료:'
total_price=0
while True:
    menu=input(menu_list)
    if int(menu)<=len(drinks):
        a=int(menu)-1
        print_menu(a)
        total_price=total_price+prices[a]
    elif int(menu)==len(drinks)+1:
        rnum=random.randint(0,len(drinks)-1)
        print_menu(rnum)
        total_price = total_price + prices[rnum]
    elif int(menu)==len(drinks)+2:
        print(f'가격은 {total_price}원 입니다.')
        print(f'다음에 또 오세요')
        break