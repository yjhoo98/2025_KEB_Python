import random

drinks_foods=[['위스키','초콜릿'],['와인','치즈'],['소주','삼겹살'],['고량주','양꼬치']]

drinks_foods.append(["사케", "광어회"])
drinks_foods.append([ "위스키", "낙곱새"])

drinks_foods.pop(0)

while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods[0][0]}   2) {drinks_foods[1][0]}   3) {drinks_foods[2][0]}   4) {drinks_foods[3][0]}   5) {drinks_foods[4][0]}   6) 아무거나   7) 종료 : ')
    if menu in{'1','2','3','4','5'}:
        a=int(menu)-1
        print(f'{drinks_foods[a][0]}에 어울리는 안주는 {drinks_foods[a][1]} 입니다')
    elif menu == '6':
        num=random.randint(0,len(drinks_foods)-1)
        print(f'{drinks_foods[num][0]}에 어울리는 안주는 {drinks_foods[num][1]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break