DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'capstone', #2
        'USER': 'root', #3
        'PASSWORD': '1546',
        'HOST': 'localhost',
        'PORT': '3306', #6
    }
}
SECRET_KEY = 'django-insecure-x&1a-w5=!#wa)bspaqariwji*1@e2mw9-z1jwcp67_66!(7g7w'

INSTALLED_APPS = [
    'corsheaders'
]

# MIDLEWARE 상단에 추가
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]



# CORS 설정 - whitelist 에 추가된 주소 접근 허용
CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:8000' ,'http://localhost:3000']
CORS_ALLOW_CREDENTIALS = True

#Databasemy_settings.py
