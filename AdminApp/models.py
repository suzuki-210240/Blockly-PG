import uuid
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from pathlib import Path
from django.conf import settings
from django.dispatch import receiver

# class Task(models.Model):
#     CATEGORY_CHOICES = [
#         ('basic', '基本'),
#         ('advanced', '応用'),
#     ]
    
#     title = models.CharField(max_length=200)
#     file_content = models.TextField()
#     file_type = models.CharField(max_length=10, choices=[('html', 'HTML'), ('py', 'Python')])
#     category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


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
    # UUIDを生成する関数
    def generate_uuid():
        return uuid.uuid4().hex
    # 教材ID
    material_id = models.CharField(
        max_length=32,  # UUIDの16進数形式は32文字
        primary_key=True,  # 主キー
        #null=True,
        default=generate_uuid,  # 関数を指定
        editable=False  # 編集不可
    )
    #教材タイトル
    material_name = models.CharField(max_length=40, unique=True)  # VARCHAR(40) に対応
    #htmlファイル名
    html_file_name = models.CharField(max_length=40) # VARCHAR(40) に対応
    class Meta:
        db_table = 'materials_table'  # MySQLのテーブル名を指定

    def __str__(self):
        return f"{self.material_name} - {self.html_file_name}"

#--------------------------教材テーブル--------------------------------

#--------------------------課題テーブル--------------------------------

class Kadai(models.Model):
    #課題区分
    CATEGORY_CHOICES = [
        ('基本区分', '基本'),
        ('応用区分', '応用'),
        ('チュートリアル','チュートリアル')
    ]
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='基本区分', verbose_name="問題区分")
    #課題番号
    number = models.CharField(max_length=100, verbose_name="問題番号", primary_key=True, unique=True,default="1")
    #課題名
    name = models.CharField(max_length=100, default="問題名")
    #問題文
    q_text = models.TextField(verbose_name="問題文", default="問題文")

    class Meta:
        db_table = 'kadai_table'

    def __str__(self):
        return f"問題番号：{self.number}-{self.category}:{self.name}"


#--------------------------課題テーブル--------------------------------

#--------------------------課題解答テーブル--------------------------------

class Answer(models.Model):
    #課題テーブルと紐づけ
    kadai = models.ForeignKey(Kadai, related_name="answers", on_delete=models.CASCADE, verbose_name="問題",to_field="number")
    a_text = models.TextField(verbose_name="解答内容")

    class Meta:
        db_table = 'answer_table'

    def __str__(self):        
        return f"解答{self.id} for {self.question.name}"
    
#--------------------------課題解答テーブル--------------------------------

#--------------------------課題実績テーブル--------------------------------
class KadaiProgress(models.Model):
    #進捗状況のフラグ
    PROGURESS_FLAGS = [
        ('未着手',0),
        ('実行中',1),
        ('完了',2)
    ]
    #ユーザーID
    user = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'groups_name':'user'}, verbose_name="user")
    #課題ID
    kadai = models.ForeignKey(Kadai, on_delete=models.CASCADE, verbose_name="課題")
    #進捗状況
    progress = models.CharField(max_length=10, choices=PROGURESS_FLAGS, default='未着手', verbose_name="進捗状況")
    update_at = models.DateTimeField(auto_now_add=True, verbose_name="更新日時")

    class Meta:
        db_table = 'progress_table'
        unique_together = ('user', 'kadai')
        verbose_name = "課題進捗"
        verbose_name_plural = "課題進捗"
    
    def __str__(self):
        return f"{self.user.username} - {self.kadai.number} - {self.progress}"
    
@receiver(post_save, sender=User)
def create_proguress_for_new_user(sender, instance, created, **kwargs):
    #ユーザーの新規登録時に既存課題の進捗を作成
    if created:
        all_kadai = Kadai.objects.all()
        KadaiProgress.objects.bulk_create([
            KadaiProgress(user=instance, kadai=kadai) 
            for kadai in all_kadai
        ])

@receiver(post_save, sender=Kadai)
def create_proguress_for_new_kadai(sender, instance, created, **kwargs):
    #課題の新規登録時に既存ユーザーの進捗を作成
    if created:
        all_user = User.objects.all()
        KadaiProgress.objects.bulk_create([
            KadaiProgress(user=user, kadai=instance) 
            for user in all_user
        ])

# class KadaiResult(models.Model):
#     #ユーザーID
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     #課題ID
#     kadai_id = models.ForeignKey(Kadai, on_delete=models.CASCADE)
#     #実績
#     achieve = models.CharField(max_length=1) #0=未着手,1=実行中,2=完了

#     class Meta:
#         db_table = 'kadai_achieve_table'
#--------------------------課題実績テーブル--------------------------------

#--------------------------画像テーブル--------------------------------
class Image(models.Model):
    img_name = models.CharField(max_length=40, primary_key=True)
    base64_image = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.img_name
#--------------------------画像テーブル--------------------------------