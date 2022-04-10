from products.models import Menu

menus = ['음료', '푸드', '상품', '카드']
for menu in menus:
    Menu.objects.create(name=menu)