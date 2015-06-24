## Setup Unit Test Environment
 
- Install pip in [Koding.com VM](koding.com): `kpm install pip`
 
- Install nose: `sudo pip install nose`

- Install coverage: `sudo pip install coverage`

## Run all tests
- Change directory to the location of source and test code
- Run tests: `nosetests`
- Run tests with coverage report: `nosetests --with-coverage --cover-package=.`
