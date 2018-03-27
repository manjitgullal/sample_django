Simple Django Project
---------------------

What does this project contain?
------------------------------
This is chat forum, where users can create a topic and discuss about it

Basic commands for the project
------------------------------
C:\Users\Manjit\Desktop\Random\Star_Trek\Development\my_python\django\new_project
virtualenv venv
venv\Scripts\activate
venv\Scripts\deactivate.bat
django-admin startproject myproject
python manage.py runserver 
http://127.0.0.1:8000/
django-admin startapp boards
python manage.py makemigrations
python manage.py sqlmigrate boards 0001
python manage.py migrate
Board.objects.all() 

Git commands
------------
cd /c/Users/Manjit/Desktop/Random/Star_Trek/Development/my_python/django/new_project
git pull
git push -u origin master
git diff origin/master README.txt


External Sources for Info
-------------------------
https://docs.djangoproject.com/en/2.0/ref/django-admin/
https://simpleisbetterthancomplex.com/series/2017/09/04/a-complete-beginners-guide-to-django-part-1.html
https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html

Errors received
----------------
https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete
