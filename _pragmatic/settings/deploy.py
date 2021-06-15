from .base import *

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file

environ.Env.read_env(str(BASE_DIR.joinpath('.env')))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django', # 우리가 연결하는 mariadb 내에서 이 이름으로 만들거다.
        'USER': 'django', # 그냥 django로 하겠습니다.
        'PASSWORD': 'roqkf1234', #
        'HOST': 'mariadb', # 장고 컨테이너 이름으로 연결된다고 했었듯이 여기에 mariadb의 컨테이너 이름을 정해준다.
        'PORT': '3306', # 포트는 3306이 보통 mysql 기본인듯. 어딜가도 맨날 이 포트임.
    }
}