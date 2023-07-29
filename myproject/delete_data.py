# delete_data.py

from myapp.models import Saved

# 모든 데이터 삭제
Saved.objects.all().delete()


