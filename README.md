# Zenpit Django RESTful API

A really simple get/post api for mobile device information, built with the [Django REST framework](http://www.django-rest-framework.org/).

 The program has a few `requirements.txt`, which you will need to install later (see Installation):

```
Django==2.0.7
djangorestframework==3.8.2
pytz==2018.5
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
*feel free to name the environment something other than 'env'*
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

    $ python manage.py migrate

### Ready to Run

    $ python manage.py runserver

See it in action at http://localhost:8000/device.

You can request a single device by adding it's ID to the url like this:

http://localhost:8000/device/1/

IDs are automatically added when to create a device, and incremented by 1, starting at 1.
