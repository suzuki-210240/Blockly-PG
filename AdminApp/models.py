from django.db import models
from django.contrib.auth.models import User
from pathlib import Path
from django.conf import settings

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('basic', '基本'),
        ('advanced', '応用'),
    ]
    
    title = models.CharField(max_length=200)
    file_content = models.TextField()
    file_type = models.CharField(max_length=10, choices=[('html', 'HTML'), ('py', 'Python')])
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def upload_to_overwrite(instance, filename):
    file_path = Path(settings.MEDIA_ROOT) / 'uploads' /filename

    if file_path.exists():
        file_path.unlink()

    return Path('uploads') / filename

class FileUpload(models.Model):
    file = models.FileField(upload_to=upload_to_overwrite)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file.name)


#--------------------------教材テーブル--------------------------------
class Material(models.Model):
    #教材タイトル
    material_name = models.CharField(max_length=40, unique=True)  # VARCHAR(40) に対応
    #htmlファイル名
    html_file_name = models.CharField(max_length=40) # VARCHAR(40) に対応
    # アップロード日（使用なし）
    #upload_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'materials_table'  # MySQLのテーブル名を指定

    def __str__(self):
        return f"{self.material_name} - {self.html_file_name}"

#--------------------------教材テーブル--------------------------------

#--------------------------課題テーブル--------------------------------

class Kadai(models.Model):
    #課題ID
    kadai_id = models.AutoField(primary_key=True)
    #教材タイトル
    kadai_name = models.CharField(max_length=40, unique=True)  # VARCHAR(40) に対応
    #htmlファイル名
    python_file_name = models.CharField(max_length=40) # VARCHAR(40) に対応
    # アップロード日（使用なし）
    #upload_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'kadai_table'  # MySQLのテーブル名を指定

    def __str__(self):
        return f"{self.kadai_name} - {self.python_file_name}"


#--------------------------課題テーブル--------------------------------


#--------------------------課題実績テーブル--------------------------------

class KadaiResult(models.Model):
    #ユーザーID
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #課題ID
    kadai_id = models.ForeignKey(Kadai, on_delete=models.CASCADE)
    #実績
    achieve = models.CharField(max_length=1) #0=未着手,1=実行中,2=完了

    class Meta:
        db_table = 'kadai_achieve_table'
#--------------------------課題実績テーブル--------------------------------