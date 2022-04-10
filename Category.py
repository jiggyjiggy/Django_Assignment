from products.models import Menu, Category, Drink, Allergy, Allergy_Drink, Nutrition, Size, Image

categories = [['콜드 브루', '음료'], ['블렌디드', '음료'], ['브레드', '푸드'], ['케이크', '푸드']]
for i in range(len(categories)):
    if categories[i][1] == '음료':
        Category.objects.create(name=categories[i][0], menu= Menu.objects.get(name='음료') )
    elif categories[i][1] == '푸드':
        Category.objects.create(name=categories[i][0], menu= Menu.objects.get(name='푸드') )
