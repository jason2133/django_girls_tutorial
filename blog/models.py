from django.db import models
from django.utils import timezone


class Post(models.Model): # 모델을 정의한다

    # 작가
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    # models.ForeignKey : 다른 모델에 대한 링크

    # 글 제목
    title = models.CharField(max_length=200)
    # models.CharField : 글자 수가 제한된 텍스트를 정의할 때 사용
    # 글 제목 같이 짧은 문자열!
    # 여기서는 max_length = 200이므로 글 제목 글자수 제한은 200자겠네

    # 글 내용
    text = models.TextField()
    # models.TextField : 글자 수에 제한이 없는 긴 텍스트
    # 블로그 컨텐츠 글 내용을 담기 좋음

    # 글 써진 시간
    created_date = models.DateTimeField(
            default=timezone.now)
    # default = timezone.now를 통해 디폴트 기본설정값은 현재 시간임

    # 글 올라간 시간
    published_date = models.DateTimeField(
            blank=True, null=True)
    # models.DateTimeField : 날짜와 시간을 의미

    def publish(self):
        self.published_date = timezone.now()
        # 글 올라간 시간은 현재 시간이고요

        self.save()
        # 저장시켜요~

    def __str__(self):
        return self.title
        # __str__ 을 호출하면 글의 제목을 리턴시켜줌

# cmd에 python manage.py migrate blog 명령을 통해 실제 데이터베이스에 모델 추가를 반영함
# 글 모델이 데이터베이스에 저장됨!

