#메뉴 삭제 추가에 대응되는 코드 추가
import random
def print_menu(num):
    print(f'{drinks[num]}에 어울리는 안주는 {drinks_foods[num]} 입니다')

drinks=['위스키','와인','소주','고량주']
drinks_foods=['초콜릿','치즈','삼겹살','양꼬치']

while True:
    ask = input(f'1)메뉴 추가 2)메뉴 삭제 3)변경없음:')
    if int(ask)==1:
        new_menu = input("주류와 안주 입력:").split(' ')
        if new_menu[0] not in drinks:
            print('이미 있는 메뉴')
            continue
        else:
            drinks.append(new_menu[0])
            drinks_foods.append(new_menu[1])
    elif int(ask)==2:
        del_menu = input("주류와 안주 입력:").split(' ')
        if del_menu[0] not in drinks:
            print('존재하지 않는 메뉴')
            continue
        else:
            drinks.remove(del_menu[0])
            drinks_foods.remove(del_menu[1])

    elif int(ask)==3:
        print(f'변경없음.')
        break
print(drinks)


menu_list='다음 술중에 고르세요.\n'
for i in range(len(drinks_foods)):
    menu_list=menu_list+f'{i+1}){drinks[i]} '
menu_list=menu_list+f'{len(drinks)+1}) 아무거나 {len(drinks)+2}) 종료:'

while True:
    menu=input(menu_list)
    if int(menu)<=len(drinks):
        a=int(menu)-1
        print_menu(a)
    elif int(menu)==len(drinks)+1:
        num=random.randint(0,len(drinks)-1)
        print_menu(num)
    elif int(menu)==len(drinks)+2:
        print(f'다음에 또 오세요')
        break