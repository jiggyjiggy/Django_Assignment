from products.models import Allergy, Allergy_Drink, Drink

allergies=[
    ['대두', ['트리플 미니 스콘', '밀당 초코 타르트']],
    ['우유', ['나이트로 바닐라 크림','나이트로 쇼콜라 클라우드', '딸기 요거트 블렌디드', '트리플 미니 스콘', '보니밤 몽블랑 데니쉬', '밀당 에그 타르트', '밀당 초코 타르트']],
    ['난류', ['트리플 미니 스콘', '보니밤 몽블랑 데니쉬', '밀당 에그 타르트', '밀당 초코 타르트']],
    ['밀', ['트리플 미니 스콘', '보니밤 몽블랑 데니쉬', '밀당 에그 타르트', '밀당 초코 타르트']],
    ['아황산류', ['보니밤 몽블랑 데니쉬']],
    ['토마토', ['딸기 요거트 블랜디드']]
]

for allergy in allergies:
    for i in range(len(allergy[1])):
        Allergy_Drink.objects.create(allergy=Allergy.objects.get(name=allergy[0]), drink=Drink.objects.get(korean_name=allergy[1][i]))