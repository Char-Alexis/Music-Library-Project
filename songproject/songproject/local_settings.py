SECRET_KEY = 'django-insecure-gs@3guhmdrtxg!t5e^xp5zgz%)-@-ysqarlay9i6w8olb30n=#'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'song_library_database',
        'USER': 'root',
        'PASSWORD': 'codeDean$6',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit':True
        }

    }
}
