from django.db import models
# 名前からURLを取得する関数reverseをインポート
from django.urls import reverse

# !!モデルを更新したら、データベースに反映するためにマイグレーションが必要!!
class Category(models.Model):
    # カテゴリー名は文字列（CharField）で定義
    name = models.CharField(max_length=200)
    # 管理画面で自身のカテゴリー名を表示するようにする
    def __str__(self):
        return self.name

#Django内で用意されているModelクラスを継承したサブクラスProductを作成
class Product(models.Model):
    # 商品名は文字列（CharField）で定義
    name = models.CharField(max_length=200)
    # 金額は正の整数（PositiveIntegerField）で定義
    price = models.PositiveIntegerField()
    # カテゴリーを付与することで1対多のリレーションを設定する。
    # カテゴリー削除時は、紐づいているProductもすべて削除（CASCADE）する。
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 商品説明フィールドを追加
    description = models.TextField(blank=True, null=True)
    # 画像フィールドを追加（画像ファイルをアップロードできるようになる）
    # 画像ファイルがメディアフォルダに保存され、そのパスがデータベースに保存される
    img = models.ImageField(blank=True, default='noImage.png')
    # 管理画面で自身の商品名（name、文字列）を表示するようにする
    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')