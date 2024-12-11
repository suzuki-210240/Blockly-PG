import re
import os,requests,urllib.parse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from .models import Material, Kadai, Answer
from .forms import  AddMaterialForm,KadaiForm,AnswerForm
from django.core.files.storage import default_storage
from django.contrib.auth.models import User, Group
from .forms import UserGroupForm
from django.http import HttpResponse,Http404
from django.db import transaction, IntegrityError


#管理者のみがアクセスできるビューのデコレーター
def is_admin(user):
    return user.groups.filter(name='admin').exists()

#管理者用のアカウント管理ページ
@login_required
@user_passes_test(is_admin)
def account_management(request):
    users = User.objects.exclude(is_superuser=True)  #すべてのユーザーを取得（スーパーユーザーを除く）
    if request.method == 'POST':
        form = UserGroupForm(request.POST)
        if form.is_valid():
            #フォームから取得したユーザーIDとグループ名を使って、ユーザーオブジェクトとグループを取得
            user = form.cleaned_data['user']  #ここでUserオブジェクトを取得
            group_name = form.cleaned_data['group'] #グループ名

            #グループオブジェクトを取得
            group = Group.objects.get(name=group_name)

            #ユーザーのグループを変更
            user.groups.clear() #現在のグループを削除
            user.groups.add(group)  #新しいグループを追加

            #更新後にリダイレクト
            return redirect('AdminApp:account_management')
    else:
        form = UserGroupForm()

    return render(request, 'admin/account_management.html', {'users': users, 'form': form})

#アカウント削除メソッド
@login_required
@user_passes_test(is_admin)
def account_management_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    #ユーザーを削除
    user.delete()
    #削除後にアカウント管理ページにリダイレクト
    return redirect('AdminApp:account_management')



@login_required
def admin_menu(request):
    context = {}    #ユーザー名と権限名の入れ物
    #↓ログインされていればユーザー名と権限名取得
    if request.user.is_authenticated:
        user = request.user
        group_names = [group.name for group in user.groups.all()]

        if 'admin' in group_names:
            group_display = "管理者"
        elif 'user' in group_names:
            group_display = "一般ユーザー"
        else:
            group_display = "未分類"
            
        context['user_info'] = {
            'username' : user.username,
            'group' : group_display
        }
    return render(request, 'home/admin_menu.html', context)

# @staff_member_required
# def task_list(request):
#     tasks = Task.objects.filter(created_by=request.user)
#     return render(request, 'adminapp/task_list.html', {'tasks': tasks})

# @staff_member_required
# def task_create(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST, request.FILES)
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.created_by = request.user
#             task.file_content = request.FILES['file_upload'].read().decode('utf-8')
#             task.file_type = request.FILES['file_upload'].name.split('.')[-1].lower()
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'adminapp/task_create.html', {'form': form})

# @staff_member_required
# def task_edit(request, task_id):
#     task = get_object_or_404(Task, id=task_id, created_by=request.user)
#     if request.method == 'POST':
#         form = TaskForm(request.POST, request.FILES, instance=task)
#         if form.is_valid():
#             task = form.save(commit=False)
#             if 'file_upload' in request.FILES:
#                 task.file_content = request.FILES['file_upload'].read().decode('utf-8')
#                 task.file_type = request.FILES['file_upload'].name.split('.')[-1].lower()
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm(instance=task)
#     return render(request, 'adminapp/edit.html', {'form': form})


def admin_materials_list(request):
    return render(request, 'Materials/admin_materials_list.html')

def add_materials(request):
    return render(request, 'Materials/add_materials.html')

def index(request):
    return render(request, 'Materials/index.html')

def edit_materials(request):
    return render(request, 'Materials/edit_materials.html')

#def material_display(request):
    #return render(request, 'material_display.html')

def send_material(request):
    return render(request, 'Materials/material_display.html')


#----------------------------教材一覧リスト------------------------------------

def list_files(request):

    # uploadsディレクトリのパス
    folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads')

    # フォルダ内のファイルとディレクトリを取得
    try:
        # mediaフォルダ内のファイル取得(リスト)
        files_and_dirs = os.listdir(folder_path)
        print('files_and_dirs', files_and_dirs)
        # dbから二次元リストとして作成[{material_name},{html_file_name}]
        db_files_name = Material.objects.values('material_name', 'html_file_name').filter(html_file_name__in=files_and_dirs)
        # db_files_nameをリストに変換
        db_files_list = list(db_files_name)
        # db_files_nameの内容を確認
        print(f"db_files_name: {db_files_list}")
        # db_files_listをhtml_file_name順に並べ替え、files_and_dirsの順番でmaterial_nameを取得
        material_dict = {material['html_file_name']: material['material_name'] for material in db_files_list}
        # files_and_dirsの順番に従って、対応するmaterial_nameを取得
        db_material_names = [material_dict[file_name] for file_name in files_and_dirs if file_name in material_dict]
        # 並び替えた結果を表示
        print(f"db_material_names: {db_material_names}")

    except FileNotFoundError:
        # フォルダが存在しない場合のエラーハンドリング
        files_and_dirs = []
        error_message = "指定されたフォルダが見つかりませんでした。"
        return render(request, 'Materials/admin_materials_list.html', {'error_message': error_message})
    except Exception as e:
        # その他の例外が発生した場合のエラーハンドリング
        files_and_dirs = []
        error_message = "エラーが発生しました。"
        return render(request, 'Materials/admin_materials_list.html', {'error_message': error_message})

    print('ファイルのurl作成')
    # ファイルのURLを作成 (エンコード処理を追加)
    file_urls = [
        os.path.join(settings.MEDIA_URL, 'uploads', urllib.parse.quote(file)) 
        for file in files_and_dirs
    ]
    # ファイル名とURLを組み合わせたタプルのリストを作成
    files_with_urls = zip(db_material_names, file_urls)
    # フォルダ内のファイルがある場合に表示
    return render(request, 'Materials/admin_materials_list.html', {'files_with_urls': files_with_urls})
#----------------------------教材一覧リスト-----------------------------------

#----------------------------教材表示-----------------------------------
def send_material(request):

    # 教材一覧で選択した教材情報を取得
    if(request.method == 'POST'):
        material_title = request.POST.get('title')
        material_url = request.POST.get('url') #medhia/uploads\ファイル名
        print(material_title, material_url)

        try:
            # MEDIA_ROOT を基準に絶対パスを作成
            material_url = os.path.join(settings.MEDIA_URL, material_url.replace("\\", "/"))
            print(material_url)

        except requests.exceptions.RequestException as e:
            #例外処理
            print(f"Error fetching HTML file: {e}") #例外処理(エラーメッセージ出力)e)

        return render(request, 'Materials/material_display.html', {'title': material_title, 'url': material_url})

    return HttpResponse('Invalid request', status=400)
#----------------------------教材表示-----------------------------------


#--------------------------教材ファイル新規追加--------------------------------

def add_file(request):
    
    if request.method == 'POST' and request.FILES:
        # フォームインスタンスを1回だけ作成
        form = AddMaterialForm(request.POST, request.FILES)
        
        if form.is_valid():
            # 教材タイトルの取得 
            title = form.cleaned_data['title']
            # アップロードされたファイルの取得
            uploaded_file = request.FILES['file']
            # アップロードされたファイル名の取得
            file_name = uploaded_file.name

            # トランザクションを開始
            try:
                with transaction.atomic():
                    # データベースに保存
                    Material.objects.create(
                        material_name=title,
                        html_file_name=file_name
                    )

                    # 保存先のパスを作成
                    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', uploaded_file.name)
                    # ディレクトリが存在しない場合、作成
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)

                    # ファイルを保存
                    with default_storage.open(file_path, 'wb+') as destination:
                        for chunk in uploaded_file.chunks():
                            destination.write(chunk)
                
                # 正常終了時
                return render(request, 'Materials/index.html')

            except IntegrityError:
                # 一意制約違反などのデータベースエラー処理
                error_message = 'このタイトルは既に使用されています。'
                return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': error_message})

            except Exception as e:
                # 他のエラー処理
                return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': str(e)})

        else:
            # フォームが無効な場合、エラーメッセージとともに再レンダリング
            return render(request, 'Materials/add_materials.html', {'form': form, 'error_message': 'フォームにエラーがあります。'})
    else:
        # 初回表示時
        form = AddMaterialForm()
    return render(request, 'Materials/add_materials.html', {'form': form})
#--------------------------教材ファイル新規追加--------------------------------
 

#--------------------------------問題・解答設定----------------------------------------


#プレフィックスの追加（基本問題はb、追加問題はa）
def create_number(kadai):
    if kadai.number:  # numberが空でないとき
        if kadai.category:
            # プレフィックスが既に含まれていない場合にのみプレフィックスを追加
            if not (kadai.number.startswith('b') or kadai.number.startswith('a') or kadai.number.startswith('t')):
                # プレフィックス設定
                category_prefix = 'b' if kadai.category == '基本区分'else ('t' if kadai.category == 'チュートリアル' else 'a')
                # プレフィックスと番号を組み合わせて設定
                kadai.number = f"{category_prefix}{kadai.number}"


def add_kadai_and_answer(request, kadai_id=None):
    if kadai_id:
        kadai = get_object_or_404(Kadai, id=kadai_id)
        answers = Answer.objects.filter(kadai=kadai)
    else:
        kadai = None
        answers = []

    # 問題フォーム
    if request.method == "POST":
        kadai_form = KadaiForm(request.POST, instance=kadai)
        answer_form = AnswerForm(request.POST)  # 解答フォーム

        if kadai_form.is_valid():
            kadai_instance = kadai_form.save(commit=False)  # 問題データを保存
            create_number(kadai_instance)  # プレフィックスを設定
            kadai_instance.save()  # 問題データの保存

            # 解答フォームが有効な場合にのみ解答を保存
            if answer_form.is_valid():
                answer_instance = answer_form.save(commit=False)
                answer_instance.kadai = kadai_instance  # 解答を問題に関連付け
                answer_instance.save()

            return redirect('AdminApp:admin_kadai_list')  # 遷移先に適宜変更

    else:
        kadai_form = KadaiForm(instance=kadai)
        answer_form = AnswerForm()

    return render(request, 'kadai/Kadai_add.html', {
        'kadai_form': kadai_form,
        'answer_form': answer_form,
        'kadai': kadai,
        'answers': answers,
    })

def edit_kadai_and_answer(request, kadai_id):
    # 問題データを取得
    kadai = get_object_or_404(Kadai, number=kadai_id)
    answers = Answer.objects.filter(kadai=kadai)

    # 問題と解答のフォームを編集
    if request.method == "POST":
        # 問題フォームの処理
        kadai_form = KadaiForm(request.POST, instance=kadai)

        # 解答フォームの処理（解答が無い場合でも空フォームを表示）
        answer_forms = [
            AnswerForm(request.POST, prefix=f"answer_{i}", instance=answer)
            for i, answer in enumerate(answers)
        ]

        if kadai_form.is_valid():
            kadai_instance = kadai_form.save(commit=False)
            kadai_instance.save()  # 問題データを保存

            # 解答フォームの保存
            for answer_form in answer_forms:
                if answer_form.is_valid():
                    answer_instance = answer_form.save(commit=False)
                    answer_instance.kadai = kadai_instance  # 解答を問題に関連付け
                    answer_instance.save()

            return redirect('AdminApp:admin_kadai_list')  # 遷移先に適宜変更

    else:
        kadai_form = KadaiForm(instance=kadai)
        # 解答フォームの初期化
        answer_forms = [
            AnswerForm(prefix=f"answer_{i}", instance=answer)
            for i, answer in enumerate(answers)
        ]


    return render(request, 'kadai/Kadai_edit.html', {
        'kadai_form': kadai_form,
        'answer_forms': answer_forms,
        'kadai': kadai,
        'answers': answers,
    })


#--------------------------------問題・解答設定----------------------------------------

#------------------------------------課題管理------------------------------------------

def admin_kadai_list(request):
    kadais_by_category = Kadai.objects.values('category').distinct()  # カテゴリごとにグループ化
    categories = {}
    for category in kadais_by_category:
        category_name = category['category']
        categories[category_name] = Kadai.objects.filter(category=category_name)

    return render(request, 'kadai/Kadai_admin_list.html', {'categories': categories})

def delete_kadai(request, kadai_id):
    # 複数のKadaiオブジェクトが返ってくることに対応
    kadais = Kadai.objects.filter(number=kadai_id)
    
    if kadais.exists():
        # 1つだけ削除する（最初の1件）
        kadai = kadais.first()
        kadai.delete()
        return redirect('AdminApp:admin_kadai_list')  # 遷移先に適宜変更
    else:
        raise Http404("問題が見つかりません")
    
#------------------------------------課題管理------------------------------------------
