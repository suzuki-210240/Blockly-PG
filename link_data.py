#データベースに既存の課題とユーザーをリンクする
from AdminApp.models import Kadai, KadaiProgress
from django.contrib.auth.models import User

def link_existing_data():
    users = User.objects.all()
    kadai_list = Kadai.objects.all()

    existing_progress = set(
        KadaiProgress.objects.values_list('user_id', 'kadai_id')
    )

    new_progress = []
    for user in users:
        for kadai in kadai_list:
            if (user.id, kadai.number) not in existing_progress:
                new_progress.append(
                    KadaiProgress(user=user, kadai=kadai)
                )

    if new_progress:
        KadaiProgress.objects.bulk_create(new_progress)
        print(f"new {len(new_progress)} :edit")
    else:
        print("nondata")
        
        
if __name__ == "__main__":
    link_existing_data()
