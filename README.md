# HelpU

Empowering the ones who never give up! HelpU is a portal where disabled people can check whether the place are visiting are has specefic facilities for them or not

[![GitHub issues](https://img.shields.io/github/issues/RyanWalker277/HelpU)](https://github.com/RyanWalker277/HelpU/issues)
[![GitHub forks](https://img.shields.io/github/forks/RyanWalker277/HelpU)](https://github.com/RyanWalker277/HelpU/network)
[![GitHub stars](https://img.shields.io/github/stars/RyanWalker277/HelpU)](https://github.com/RyanWalker277/HelpU/stargazers)
[![GitHub license](https://img.shields.io/github/license/RyanWalker277/HelpU)](https://github.com/RyanWalker277/HelpU/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/RyanWalker277/HelpU) 
<br>


## Demo

The live demo of the project can be found at 
http://anvansh.pythonanywhere.com/


## Setup Instructions

Clone the repo in your local system

```bash
git clone https://github.com/RyanWalker277/HelpU.git
```
Install virtualenv

```bash
py -m pip install --user virtualenv
```
Create a new Virtualenvironment

```bash
py -m venv env
```
Activate the Virtualenvironment with

```bash
.\env\Scripts\activate
```
Change directory to the folder

```bash
cd folder-where-you-cloned-the-repo
```
Install all the requirements with

```bash
pip3 install -r requirements.txt
```
Apply all the migrations with 

```bash
python3 manage.py migrate
```
Run the developement server with 

```bash
python3 manage.py runserver
```
You'll see output like this
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 05, 2022 - 23:22:15
Django version 4.0.6, using settings 'SIH2022.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
## Creating Superuser

Clone the repo in your local system

```bash
python3 manage.py createsuperuser
```
You will see a screen like this

```bash
Username (leave blank to use 'default'):
```
Enter a username and press enter , you will see a screen like this

```bash
Email address:
```
Enter an email and press enter , then you will see a screen like this

```bash
Password:
```
Enter a password , then you will see a screen like this

```bash
Password (again):
```
Re-enter the password and you are done! You will see a screen like this

```bash
Superuser created successfully
```
## Tech Stack

**Client:** HTML , CSS , Javascript , Tailwind CSS

**Server:** Django , Python

## Features

- Search feature to search for places with facilities for disabled people
- API to return model data of places in JSON format
## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.


##
Made with ❤ by Anvansh ([@RyanWalker277](https://github.com/RyanWalker277))
