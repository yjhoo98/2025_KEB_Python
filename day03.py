#메뉴 삭제 추가에 대응되는 코드 추가
import random

drinks_foods=[['위스키','초콜릿'],['와인','치즈'],['소주','삼겹살'],['고량주','양꼬치']]

drinks_foods.append(["사케", "광어회"])
drinks_foods.append([ "위스키", "낙곱새"])

drinks_foods.pop(0)
menu_list='다음 술중에 고르세요.\n'
for i in range(len(drinks_foods)):
    menu_list=menu_list+f'{i+1}){drinks_foods[i][0]} '
menu_list=menu_list+f'{len(drinks_foods)+1}) 아무거나 {len(drinks_foods)+2}) 종료:'

while True:
    menu=input(menu_list)
    if int(menu)<=len(drinks_foods):
        a=int(menu)-1
        print(f'{drinks_foods[a][0]}에 어울리는 안주는 {drinks_foods[a][1]} 입니다')
    elif int(menu)==len(drinks_foods)+1:
        num=random.randint(0,len(drinks_foods)-1)
        print(f'{drinks_foods[num][0]}에 어울리는 안주는 {drinks_foods[num][1]} 입니다')
    elif int(menu)==len(drinks_foods)+2:
        print(f'다음에 또 오세요')
        break