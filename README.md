# Blog-API

API for a blog written in django

You can check here (testing period) — http://blog-tutorial-7657.herokuapp.com/docs/

# Setup

Create virtual environment and clone this repository:

<code>>>> python -m venv .</code>

<code>>>> cd Scripts\activate</code>

<code>>>> git clone https://github.com/jamshidyerzakov/django-blog-api.git</code>

Install all packages from <strong> requirements.txt. </strong> :

<code>>>> pip install -r requirements.py</code>

Make migrations and migrate:

<code>>>> cd django-blog-api</code>

<code>>>> python manage.py makemigrations</code>

<code>>>> python manage.py migrate</code>

Run the server and check the documentation for further actions:

<code>>>> python manage.py runserver</code>

Go to http://127.0.0.1:8000/swagger/ in order to check the docs

# Contributions

Pull requests are welcome!
