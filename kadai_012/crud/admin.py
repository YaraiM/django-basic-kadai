from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

#Django内で用意されているModelAdminクラスを継承したサブクラスProductAdminを作成
class ProductAdmin(admin.ModelAdmin):
    # 管理画面で表示される内容を配列（タプル）で定義
    list_display = ('id', 'name', 'price', 'category', 'image')
    # 管理画面でnameからProductを検索できるようにする
    search_fields = ('name',)
    # 管理画面でcategoryからフィルタリングできるようにする
    list_filter = ('category',)

    def image(self, obj):
        # 指定した文字列<img src =・・・>が安全であるという印をつけてHTMLを出力する
        return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

# Django内に用意されているModelAdminクラスを継承したサブクラスCategoryAdminを作成
class CategoryAdmin(admin.ModelAdmin):
    # 管理画面で表示される内容を配列（タプル）で定義
    list_display = ('id', 'name')
    search_fields = ('name',)

# 定義したModelを管理画面に登録する。
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)