## Projeto e-diaristas


#### Clonar o projeto
`git clone git@github.com:AllancDev/ediaristas-admin.git`


#### Alterar configurações do BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ediaristas',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'self@2106'
    }
}

```

#### Instalar dependências
`pip install -r requirements.txt`

#### Migrar banco de dados
`python manage.py migrate`

#### Iniciar o servidor
`python manage.py runserver`
