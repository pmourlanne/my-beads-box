# Readme

[![We'll see who brings in more honey](https://i.imgur.com/wMkCR56.jpeg "How hard can it be...zzz?")](https://www.youtube.com/watch?v=5J2kc4oZTVU)

## Instructions

See this [document](https://docs.google.com/document/d/1-S2WosY3p9mXEp-HihGk2FQkTUGbbej8hQm16LtJirQ/edit)

## System design

I'll be showing off here what I would do if I had one or two weeks' time to work on this :)

### [High level architecture](https://excalidraw.com/#json=UsHdLiYZ3lH4KWX6hMJbd,Jn3s-jOezOMJCpaNkpFQkw)

Some notes:
- "VPC" stands for [Virtual Private Cloud](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). This is a nifty tool that allows us to have AWS resouces isolated from one another
- The Application Load Balancer holds the SSL certificate: all the traffic pass the ALB is unencrypted
- Bastions allow us to reduce the attack surface from the outside
- The "Engineering" bastion is used by engineers to be able to SSH onto machines (web servers and databases)
- The "OPS" bastion is intended for non tech people to be able to access a database replica (in read-only). This is usually helpful to BizDev / Finance / CSM / Data Science people

### [Application Web server](https://excalidraw.com/#json=D9wcDllXdytkF_JQKfmMN,Cz9kCbw5z46fjWA5d0qZUQ)

This is pretty standard :o  
Celery is used for asynchronous task (eg. sending emails), and RabbitMQ is the broker for Celery.  
Redis is only used to cache simple things (nothing comes to mind right now, but the need often shows up soon enough 🤔)

I put in different Gunicorn services for the API and for the admin. This is probably some premature optimisation :> The upside of this setup is that it allows for different configurations (nb. of workers, timeout, etc.) for the two very different needs of the API and the admin.

### Other choices of tools

Here are some tools I would want to use:
- Terraform to manage AWS resources
- Ansible to manage what actually live inside the AWS resouces (in particular the web server and the databases)
- Github Actions to run the CI, the Terraform plans and the Ansible playbooks
- Datadog to monitor the health and performance of our services
- Sentry for the logs and the application monitoring

## My focus in this repo

In this repo I'm going to focus on building a simple Django application. If I had more time, I would go the SPA + API (DRF) route, but I want to get something working quickly, to spark a discussion :)  

For time purposes, I'm also not going to actually deploy this code in production. Working on CD, infrastructure and how we release has been my primary focus for two years at my last job. It's something I know how to do, and I'd be happy to talk about it.  
Here are two of my personal projects I *have* deployed in production:
- [TAW](https://github.com/pmourlanne/taw/), released with Vercel at [taw.petmyc.at](https://taw.petmyc.at/)
- [37tubes](https://gitlab.com/pmourlanne/37tubes), released with Ansible on a bare metal machine at [37tub.es](http://37tub.es/)

### Installation

In a Python 3.12 virtualenv, run:
```shell
$ pip install -r requirements.txt
```

Create the database and the user in PG:
```shell
$ sudo -u postgres psql

postgres=# create database mybeadsbox;
CREATE DATABASE

postgres=# create user mybeadsbox with encrypted password 'test';
CREATE ROLE

postgres=# grant all privileges on database mybeadsbox to mybeadsbox;
GRANT
```

Run the migrations:
```shell
$ cd mybeadsbox
$ python manage.py migrate
```

### Running the server locally

```shell
$ cd mybeadsbox
$ python manage.py runserver
```

Access the local server on `localhost:8000/vouchers/`

### Running the tests

TODO
