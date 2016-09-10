Feature: Search

Scenario Outline: Assert search works
	Given I navigate to "<url>"
	When I search for "<keyword>"
	Then I should see "<expected>" in the page title

Examples:
| url                     | keyword               | expected              |
| http://www.google.com   | Mazedur Rahman        | Mazedur Rahman        |
