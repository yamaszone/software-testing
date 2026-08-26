## Setup BDD Test Environment
 - Install `virtualenv` (for example, `sudo apt-get install -y python-virtualenv`)
 - Create a virtual environment: `virtualenv venv`
 - Activate the virtual environment: `. venv/bin/activate`
 - Install `pexpect` using `pip`: `pip install pexpect`
 - Install `behave` using `pip`: `pip install behave`
 - Deactivate the virtual environment when finished: `deactivate`
 
## Run all tests
- Change directory to `tutorials/bdd/features/`
- Run tests: `behave`
