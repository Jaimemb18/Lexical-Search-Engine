# Lexical-Search-Engine
A simple lexical search engine used to search for keywords in a database

## Setup
**Requires Python 3**

### Python Dependencies
Using virtualenv is recommended when installing packages for python.
* `yaml` - used for reading and writing a conf.yaml file
* `getpass` - used to securely read in a mysql password
* `mysql` - used to connect to a mysql database

### Prerequisites 
* Mysql database to use for storing information

### Initializing Conf and Mysql
Run `python3 start_script.py` to start generation of a `conf.yaml` file and to create the tables in mysql required for `engine.py` to run.

This will prompt the user for a mysql connection information which is then recorded in a `conf.yaml` file.

## Usage
Run `python3 engine.py` to print usage information
