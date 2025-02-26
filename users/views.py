from django.shortcuts import render

# Create your views here.

# 暫定機能
# ユーザー登録画面
# ユーザーログイン画面
# ユーザーログアウト

# ログアウトしたらログイン画面にリダイレクト
# ログインしたらchat画面にリダイレクト
# ユーザー登録したらログイン画面にリダイレクト

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')
