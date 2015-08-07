Feature: nosetests

Scenario: nosetests runs all tests
	Given nose is installed
	When I execute "nosetests"
	Then I should see "OK"
