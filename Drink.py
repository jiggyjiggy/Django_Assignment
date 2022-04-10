from products.models import Category, Drink

drinks = [['나이트로 바닐라 크림', '콜드 브루'],  ['나이트로 쇼콜라 클라우드','콜드 브루'], ['망고 패션 후르프 블렌디드', '블렌디드'], ['딸기 요거트 블렌디드', '블렌디드'], ['트리플 미니 스콘','브레드'], ['보니밤 몽블랑 데니쉬','브레드'], ['밀당 에그 타르트','케이크'], ['밀당 초코 타르트','케이크']]

for i in range(len(drinks)):
    if drinks[i][1] == '콜드 브루':
        Drink.objects.create(korean_name=drinks[i][0], category= Category.objects.get(name='콜드 브루') )
    elif drinks[i][1] == '블렌디드':
        Drink.objects.create(korean_name=drinks[i][0], category= Category.objects.get(name='블렌디드') )
    elif drinks[i][1] == '브레드':
        Drink.objects.create(korean_name=drinks[i][0], category= Category.objects.get(name='브레드') )
    elif drinks[i][1] == '케이크':
        Drink.objects.create(korean_name=drinks[i][0], category= Category.objects.get(name='케이크') )




