# Projeto E-diaristas

## Instalando o projeto

### Clonando o projeto

`https://github.com/eneassena/multistack-ediarista-api-python.git`

### Instalar as dependências

`pip install -r requirements.txt`

### Alterar as configuração do banco de dados em settings.py no dicionário `DATABASES`

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_db',
        'HOST': 'host_db',
        'PORT': 'porta_db',
        'USER': 'usuario_db.',
        'PASSWORD': 'senha_db'
    }
}
```

### Realizar a migração

`py manage.py migrate`

### Roda o servidor

`py manage.py runserver`
