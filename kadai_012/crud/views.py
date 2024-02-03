from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"

# ユーザー側ページに商品一覧画面を表示するためのViewクラスを定義
class ProductListView(ListView):
    model = Product
    # ページネーション（１ページに表示する商品名は最大３とする）
    paginate_by = 3

# ユーザー側ページに新規登録フォームを追加（CreateViewを継承したクラスを作成）
class ProductCreateView(CreateView):
    # modelに対象のModelクラスを代入
    model = Product
    # ユーザーが入力できるフィールド（Productの属性）は全フィールド（name, price）
    fields = '__all__'

 # ユーザー側ページに編集フォームを追加（UpdateViewを継承したクラスを作成）
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    # デフォルトのTemplateファイル名が新規作成フォームと同じproduct_form.htmlになるため、
    # product_update_form.htmlに変更
    template_name_suffix = '_update_form'

# ユーザー側ページに削除フォームを追加（DeleteViewを継承したクラスを作成）
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

# 詳細画面を追加（10章課題）
class ProductDetailView(DetailView):
    model = Product