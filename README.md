# Password Manager

A simple and secure password manager written in Python using MariaDB for storage. This password manager encrypts your passwords using AES-256 encryption, which is securely derived from a combination of a MASTER PASSWORD and a DEVICE SECRET using the PBKDF2 algorithm.



## Installation

You need to have python3 to run this on Windows, Linux or MacOS


## Requirements
-Python 3.x

-Python Libraries:

-cryptography

-mysql-connector-python

-bcrypt

--MariaDB (or MySQL)


### how to use and create pm



Login to database sql
```
sudo mysql -u root
```
### create user

```
CREATE USER 'pm'@localhost IDENTIFIED BY 'password';
```

### Grant privileges

```
GRANT ALL PRIVILEGES ON *.* TO 'pm'@localhost IDENTIFIED BY 'password';
```

## Windows
### install Python Requirements

```
pip install -r requirements.txt
```

## MariaDB
### Install

install MariaDB on Windows on this  https://www.mariadbtutorial.com/getting-started/install-mariadb/

## Run

### Configure
 You need to first configure the password manager by choosing a MASTER PASSWORD. This config step is only required to be executed once.
 ```
 python config.py make
 ```

 The above command will make a new configuration by asking you to choose a MASTER PASSWORD. This will generate the DEVICE SECRET, create db and required tables.

 ```
 python config.py delete
 ```

 The above command will delete the existing configuration. Doing this will completely delete your device secret and all your entries and you will loose all your passwords. So be aware!
 ```
 python config.py remake
 ```
 The above command will first delete the existing configuration and create a fresh new configuration by asking you to choose a MASTER PASSWORD, generate the DEVICE SECRET, create the db and required tables.


 ## Usage

 ```
 python pm.py -h
usage: pm.py [-h] [-s NAME] [-u URL] [-e EMAIL] [-l LOGIN] [--length LENGTH] [-c] option

Description

positional arguments:
  option                (a)dd / (e)xtract / (g)enerate

optional arguments:
  -h, --help            show this help message and exit
  -s NAME, --name NAME  Site name
  -u URL, --url URL     Site URL
  -e EMAIL, --email EMAIL
                        Email
  -l LOGIN, --login LOGIN
                        Username
  --length LENGTH       Length of the password to generate
  -c, --copy            Copy password to clipboard
  ```

  ## Add entry
  
  python pm.py add -s mysite -u mysite.com -e hello@email.com -l myusername

 ### Retrieve entry
 ```
 python pm.py extract
 ````

 The above command retrieves all the entries whose site name is "mysite"
 ```
 python pm.py e -s mysite -l myusername
 ```

 ## Generate Password
 ```
 python pm.py g --length 15
 ```