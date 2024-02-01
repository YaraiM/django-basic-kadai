from django.contrib import admin
from .models import Product

#Django内で用意されているModelAdminクラスを継承したサブクラスProductAdminを作成
class ProductAdmin(admin.ModelAdmin):
    # 管理画面で表示される内容を配列（リスト）で定義
    list_display = ('id', 'name', 'price')
    # 管理画面でnameからProductを検索できるようにする
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)