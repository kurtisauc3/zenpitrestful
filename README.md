# Zenpit Django RESTful API

A really simple get/post api for mobile device information, built with the [Django REST framework](http://www.django-rest-framework.org/).

 The program has a few `requirements.txt`, which are:

```
certifi==2018.4.16
chardet==3.0.4
Django==2.0.6
idna==2.7
pytz==2018.4
requests==2.19.1
urllib3==1.23
```

## Installation

### 1. virtualenv
Activate your [virtualenv](https://virtualenv.pypa.io/en/stable/installation/), and make an `env` with python3:


    $ cd /path/to/your/envs
    $ virtualenv -p python3 env
    $ source env/bin/activate

If you don't have virtualenv, you will have to install it first. This can be easily done in your terminal:

    $ pip install virtualenv

*pip usually doesn't require `sudo`*
### 2. Download
Grab a copy of the source code and clone it:

    $ cd /path/to/your/workspace
    $ git clone https://github.com/kurtisauc3/zenpitrestful.git
    $ cd zenpitrestful

### 3. Requirements
 *requirements.txt* contains all the packages need to run the website. Make sure your env is activated and run:

    $ pip install -r requirements.txt

### 4. Preparation

#### Initialize the database
You'll need to migrate your database with 2 commands.

Make sure you are still in '/zenpitrestful/'

    $ python manage.py makemigrations
    $ python manage.py migrate

### Ready to Run

    $ python manage.py runserver

See it in action at http://localhost:8000/devicelist.

You can request a single device by adding it's ID to the url like this:

http://localhost:8000/devicelist/1/

IDs are automatically added and incremented by 1, starting at 1.
