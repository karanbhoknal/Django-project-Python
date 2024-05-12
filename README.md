# Django-project-Python

Project Nmae : Python Knowledge Share site

# INTRODUCTION

I created Python Knowledge Share Site In this project I am using Django (python frameworks) SQlite Database,HTML,CSS etc.

This site is will be very helpful for Basic python knowledge for beginner. In this Site covered 10-12 Basic Important python points those are mandatory for any beginner.

The following are the python features points that 1 covered in this site
1 Python Introduction 
2. Python overview 
3. Python variable 
4.Python keywords and identifie 
5. Python loops 
6. Python conditions 
7. Python tuple 
8.Python set
9. Python directory 
10.Python dictionary 
11.Python Different Modules 
12.Python Functions

# Features of Django
The versatility of Django: Django can build almost any type of website. It can also work with any client-side framework and can deliver content in any format such as HTML,JSON, XML, etc. Some sites which can be built using Django are wikis, social networks, new sites etc.

# Security:
Since the Django framework is made for making web development easy, it has been engineered in such a way that it automatically do the right things to protect the website. For example, In the Django framework instead of putting a password in cookies, the hashed password is stored in it so that it can’t be fetched easily by hackers.

# Scalability:
Django web nodes have no stored state, they scale horizontally – just fire up more of them when you need them. Being able to do this is the essence of good scalability. Instagram and Disqus are two Django based products that have millions of active users,this is taken as an example of the scalabilit of Django.

# Portability:
All the codes of the Django framework are written in Python, which runs on many platforms.Which leads to run Django too in many platforms such as Linux, Windows and Mac OS.

# Django Architecture
Django is based on MVT (Model-View-Template) architecture which has the following three parts –

# Model:
The model is going to act as the interface of your data. It is responsible for maintaining data. It is the logical data structure behind the entire application and is represented by a database generally relational databases such as MySql, Postgres).

# View:
The View is the user interface that you see in your browser when you render a website. It is represented by HTML/CSS/Javascript and Jinja files.

# Template:
A template consists of static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. To check more, visit – Django Templates Django Architecture

#Installation and Setup of Django Project
Install python3 if not installed in your system download the latest version of python it’s python 3.11.0 this time.

open the command prompt and make directory folder
mkdir Django_project

3.Setting up the Virtual Environment
Create virtual environment in django: We should first go the directory where we want to createthe virtual environment then we type the following command to create virtual environment in django

1.It is create venv in Django project directory

python -m venv .venv

2.It is Activate the venv in Django project directory

.venv\Scripts\Activate [for Windows]

For MacOs/Linux:

source env_site/bin/activate

5 .Install Django: Install django by giving following command
Command => pip install django

Start a project by following command
django-admin startproject django_proj

7.Change directory to django_proj
cd django_proj

8.Create an empty development database by running the following command
python manage.py migrate [db.sqlit3]

9.Start the server- Start the server by typing following command in cmd-
python manage.py runserver

Open the folder Django project in Vscode & hit this command
python manage.py startapp projectApp
