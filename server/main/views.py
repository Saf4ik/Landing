from django.shortcuts import render
from django.utils.html import mark_safe

# Create your views here.
def index(request):
    return render(
        request,
        'main/index.html',
        {
            'title': 'Pretty Nails',
            'title_page': mark_safe("Привет! Я <strong>Юлия Ветрова</strong>."),
            'description': '''Я мастер маникюра. Моя специализация шеллак и гель-лак. 
                            Также занимаюсь всякой прочей ерудной и вяжу крестиком. 
                            Могу петь и танцевать на свадьбах, корпоративах''',
                            
            'stuff_description': 'Здесь можно почитать отзывы клиентов и оставить свои.',
            'boxes': [
                        mark_safe('<span class="icon featured fa-comments-o"></span>'),
                        mark_safe('<span class="icon featured fa-camera-retro"></span>'),
                        mark_safe('<span class="icon featured fa-thumbs-o-up"></span>'),
            ],
            'portfolio': [
                            mark_safe('<img src="/static/main/images/pic01.jpg" alt="" />'),
                            mark_safe('<img src="/static/main/images/pic02.jpg" alt="" />'),
                            mark_safe('<img src="/static/main/images/pic03.jpg" alt="" />'),
                            mark_safe('<img src="/static/main/images/pic04.jpg" alt="" />'),
                            mark_safe('<img src="/static/main/images/pic05.jpg" alt="" />'),
                            mark_safe('<img src="/static/main/images/pic06.jpg" alt="" />'),
            ]
            
        }
    )