from django.shortcuts import render
import random
from PIL import Image

# Create your views here.


def dinner(request):
    # 지역 추천
    location = ['Seoul', 'Incheon', 'Jeju']
    city = random.choice(location)

    # 지역별 맛집 추천
    Seoul_ = ['단상', '또보겠지떡볶이집', '구스토타코']
    Incheon_ = ['다담닭갈비', '발꾸락', '고복샤브샤브']
    Jeju_ = ['나무식탁', '돈사무소', '심바카레']

    if (city == 'Seoul'):
        matzip = random.choice(Seoul_)
    elif (city == 'Incheon'):
        matzip = random.choice(Incheon_)
    else:
        matzip = random.choice(Jeju_)

    images = {
        '단상':'https://mblogthumb-phinf.pstatic.net/MjAyMDEwMjBfNDcg/MDAxNjAzMjA0MzU2Mjc0.oUznzU50p79ziYACYvRWYQ7R8WFNrki3V0nro0SuUcQg.1euHMsRkfAfxPSYFX8PPImpMXxwlPnVIA1SQjioWWDEg.JPEG.ino111/1603204355113.jpg?type=w800',
        '또보겠지떡볶이집':'https://d12zq4w4guyljn.cloudfront.net/20220501111922_photo1_753fea4c5d8f.jpg',
        '구스토타코':'https://ko.wikipedia.org/wiki/%ED%83%80%EC%BD%94#/media/%ED%8C%8C%EC%9D%BC:001_Tacos_de_carnitas,_carne_asada_y_al_pastor.jpg',
        '다담닭갈비':'https://ko.wikipedia.org/wiki/%EB%8B%AD%EA%B0%88%EB%B9%84#/media/%ED%8C%8C%EC%9D%BC:Dakgalbi.jpg',
        '발꾸락':'https://hub.zum.com/view/photo?url=https%3A%2F%2Fstatic.hubzum.zumst.com%2Fhubzum%2F2019%2F07%2F26%2F11%2F8291a05e16b14e9b91eedc7a4375c934.jpg',
        '고복샤브샤브':'https://d12zq4w4guyljn.cloudfront.net/750_750_20220908065720298_photo_cf9b59e40079.jpg',
        '나무식탁':'https://mp-seoul-image-production-s3.mangoplate.com/389603/1895637_1615974524552_43102',
        '돈사무소':'img:'
    }

    image = images[matzip] # 이미지는 images 딕셔너리의 matzip key에 해당하는 value

    context = {
        'city': city,
        'matzip': matzip,
        'image' : image,
    }

    return render(request, 'dinner.html', context)



def lotto(request):
    return render(request, 'lotto.html')
