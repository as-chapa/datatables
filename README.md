# 概要
Django環境でDatatablesを利用するためのサンプルコードです。
データ量が増えた際に、Javascript側で性能影響を出さないように、
ajaxを利用してテーブル部分を表示しています。

# インストール
`$ pip install django==2.2`  
`$ pip install django-datatables-view==1.19.1`

# 使い方
### マイグレート＆テストデータ投入
`$ python manage.py makemigrations`  
`$ python manage.py migrate`  
`$ python manage.py shell < sample/create_testdata.py`

### サーバの起動
`$ python manage.py runserver`

### ブラウザで表示
ブラウザで以下のURLを入力する
http://127.0.0.1:8000/sample/booklist/
