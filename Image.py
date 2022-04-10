from products.models import Menu, Category, Drink, Allergy, Allergy_Drink, Nutrition, Size, Image

image_urls = [['https://image.istarbucks.co.kr/upload/store/skuimg/2021/04/[9200000002487]_20210426091745609.jpg','나이트로 바닐라 크림'],
    
    
]
for image_url in image_urls:    
    Image.objects.create(image_url=image_url, drink= Drink.objects.get(name=))