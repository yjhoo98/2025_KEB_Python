#메뉴 삭제 추가에 대응되는 코드 추가
import random
def print_menu(num):
    print(f'{drinks[num]}에 어울리는 안주는 {drinks_foods[num]} 입니다')
# drinks_foods=[['위스키','초콜릿'],['와인','치즈'],['소주','삼겹살'],['고량주','양꼬치']]
drinks=['위스키','와인','소주','고량주']
drinks_foods=['초콜릿','치즈','삼겹살','양꼬치']
# drinks_foods.append(["사케", "광어회"])
# drinks_foods.append([ "위스키", "낙곱새"])
drinks.append('사케')
drinks_foods.append('광어회')
drinks.append('위스키')
drinks_foods.append('낙곱새')
drinks.pop(0)
drinks_foods.pop(0)
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