from django.db import models
# 名前からURLを取得する関数reverseをインポート
from django.urls import reverse

#Django内で用意されているModelクラスを継承したサブクラスProductを作成
class Product(models.Model):
    # 商品名は文字列（CharField）で定義
    name = models.CharField(max_length=200)
    # 金額は正の整数（PositiveIntegerField）で定義
    price = models.PositiveIntegerField()
    # 管理画面で自身の商品名（name、文字列）を表示するようにする
    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')