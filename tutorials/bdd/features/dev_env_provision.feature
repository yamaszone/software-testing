Feature: Development environment provision
As DevOps
I want to verify all the expected dependencies properly installed
So that development environments for Developers are spun up in a consistent way

Scenario Outline: Assert correct dev and test dependencies are installed properly
	Given a Ubuntu development machine
	When I execute "<command>"
	Then I should see "<expected>"

Examples:
| command               | expected                      |
| cat /etc/os-release   | Ubuntu 14.04                  |
| python --version      | Python 2.7                    |
| nosetests --version   | nosetests version 1.3         |
| coverage --version    | Coverage.py, version 4.2      |
| phantomjs --version   | 1.9                           |
| behave --version      | behave 1.2                    |
