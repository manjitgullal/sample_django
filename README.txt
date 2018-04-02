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
python manage.py shell
python manage.py test
python manage.py test --verbosity=2
python manage.py createsuperuser
user:manjit
email:manjit862@gmail.com
pass:*********
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/boards/1/ 
http://127.0.0.1:8000/boards/1/new/

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
https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html
https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html

Errors received
----------------
https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete
https://stackoverflow.com/questions/572549/difference-between-git-add-a-and-git-add
https://stackoverflow.com/questions/43139081/importerror-no-module-named-django-core-urlresolvers
https://www.regextester.com/20

Questions?
----------
how does the virtual env work?
try with docker as well?
put your work in python anywhere?

Read the related articles
--------------------------
https://www.infoworld.com/article/3069558/application-development/7-deadly-career-mistakes-developers-make.html?page=2
https://codeburst.io/how-to-find-your-first-developer-job-f1f33455cf8e
https://www.techinasia.com/talk/5-month-guide-learn-code-get-hired

