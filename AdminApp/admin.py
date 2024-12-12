from django.contrib import admin
from .models import Kadai,Answer,KadaiProgress

class KadaiAdmin(admin.ModelAdmin):
    list_display = ('number', 'category', 'q_text')  # 問題番号、区分、問題内容、作成日時を表示
    list_filter = ('category',)  # 区分でフィルタリングできるようにする
    search_fields = ('a_text',)  # 問題内容を検索できるようにする

@admin.register(KadaiProgress)
class KadaiProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'kadai', 'progress', 'update_at')
    list_filter = ('progress', 'update_at')
    search_fields = ('user__username', 'kadai__name')

admin.site.register(Kadai,KadaiAdmin)
admin.site.register(Answer)