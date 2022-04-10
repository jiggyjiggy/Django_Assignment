from products.models import Allergy

allergies = ['대두', '우유', '난류', '밀', '아황산류', '토마토']
for allergy in allergies:
    Allergy.objects.create(name=allergy)