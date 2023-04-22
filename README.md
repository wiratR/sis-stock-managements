# Stock Movements

Stock Mangament for seconed line supports

<br />

## ✨ How to use it
>
> Download the code

```bash
git clone https://github.com/wiratR/sis-stock-managements.git
cd sis-stock-managements
```

<br />

### Set Up for `Unix`, `MacOS`

> Install modules via `VENV`  

```bash
virtualenv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

<br />

### Start Application
>
> before start copy file conif_sample.ini to config.ini

```bash
cp config_sample.ini config.ini
```

> and update scerect_key in config.ini

How to generate scerect key

1.activate the Django shell:

```bash
python manage.py shell
```

2.In the Django shell, execute the following code to generate a new secret key for your project:

```bash
from django.core.management.utils import get_random_secret_key print(get_random_secret_key())
```

3.Copy the new secret key and paste it inside your config_file.ini file, replacing the PutYourSecretKeyHereWithoutQuotationMarks information. Don't use quotation marks here.

```bash
[BASE]

SECRET_KEY=PutYourSecretKeyHereWithoutQuotationMarks
```

> Run Migration for create the necessary tables in the database;

```bash
python manage.py makemigrations 
python manage.py migrate 
```

> Sample Run Application

```bash
python manage.py runserver
```

<br />
