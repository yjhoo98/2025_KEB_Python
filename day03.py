import random
# drinks_foods = {"위스키": "초콜릿", "와인": "치즈", "소주": "삽겹살", "고량주": "양꼬치"}
drinks_foods=[['위스키','초콜릿'],['와인','치즈'],['소주','삼겹살'],['고량주','양꼬치']]
# print(drinks_foods)
# print(drinks_foods.pop("고량주"))
# print(drinks_foods)

#del drinks_foods["위스키"]
#drinks_foods["사케"] = "광어회"
japan_drinks_foods = ["사케", "광어회"]
drinks_foods.append(japan_drinks_foods)
drinks_foods.append([ "위스키", "낙곱새"])
# print(drinks_foods)
#drink = input(drinks_foods.keys())
# drinks_foods_keys = list(drinks_foods)
# print(drinks_foods_keys)
# #print(drinks_foods_keys.pop(0))
# print(drinks_foods_keys.remove("위스키"))
# print(drinks_foods_keys)
#print(random.choice(drinks_foods_keys))
drinks_foods.pop(0)
print(drinks_foods[4][0])
while True:
    menu = input(f'다음 술중에 고르세요.\n1) {drinks_foods[0][0]}   2) {drinks_foods[1][0]}   3) {drinks_foods[2][0]}   4) {drinks_foods[3][0]}   5) {drinks_foods[4][0]}   6) 아무거나   7) 종료 : ')
    if menu == '1':
        print(f'{drinks_foods[0][0]}에 어울리는 안주는 {drinks_foods[0][1]} 입니다')
    elif menu == '2':
        print(f'{drinks_foods[1][0]}에 어울리는 안주는 {drinks_foods[1][1]} 입니다')
    elif menu == '3':
        print(f'{drinks_foods[2][0]}에 어울리는 안주는 {drinks_foods[2][1]} 입니다')
    elif menu == '4':
        print(f'{drinks_foods[3][0]}에 어울리는 안주는 {drinks_foods[3][1]} 입니다')
    elif menu == '5':
        print(f'{drinks_foods[4][0]}에 어울리는 안주는 {drinks_foods[4][1]} 입니다')
    elif menu == '6':
        num=random.randint(0,4)
        random_drink = drinks_foods[num][0]
        print(f'{random_drink}에 어울리는 안주는 {drinks_foods[num][1]} 입니다')
    elif menu == '7':
        print(f'다음에 또 오세요')
        break