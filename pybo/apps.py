from django.apps import AppConfig
from django.db import OperationalError, ProgrammingError


class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'

    def ready(self):
        from .models import Category
        try:
            if not Category.objects.exists():
                Category.objects.create(name='질의응답')
                Category.objects.create(name='자유게시판')
        except (OperationalError, ProgrammingError):
            # 데이터베이스가 아직 초기화되지 않은 경우 발생하는 에러를 무시합니다.
            pass