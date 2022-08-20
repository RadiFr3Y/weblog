# weblog_django_prj

## description
in this project i maked weblog(just with django) whitch have good features like:<br>
-comment: your user can send comment for posts and you(super Admin) can management comments "delete edit publish and another"<br>
-admin pannel: if you have admin for post on your weblog, you have personalized admin pannel for they.<br>
-edit profile: your users and your admins can edit their personality information with restrictions<br>
-send message: your users can send message in "contact page" for you<br>
-and another features...

## Install and Run
```bash
cd directory
mkdir weblog
cd weblog 
git clone https://github.com/theFr3Y/weblog_django_prj.git
pip install -r require.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

