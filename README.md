# Description
This is the final assignment for the Bakend Developer Capstone Course of the Meta Backend Developer Professional Certificate on Coursera.

# Installation

install the dependencies
```jsx
pipenv install
```

Activate the virtual environment

```jsx
pipenv shell
```
<br>

# Setup
The default database settings are

```jsx
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
        
    },
}
```
💡 Change those settings according to your local setup.
<br>
<br>

Apply the migrations
```jsx
python manage.py migrate
```
<br>

### Endpoints for `littleLemon` app
```jsx
http:127.0.0.1:8000/api/menu-items
http:127.0.0.1:8000/api/menu-items/{menu-itemId}
http:127.0.0.1:8000/api/bookings
http:127.0.0.1:8000/api/bookings/{bookingId}
```
<br>