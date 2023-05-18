Feature: Karate Test

Scenario: GET DEMO 1
Given url 'http://reqres.in/api/users?page=2'
When method GET
Then status 200
And print responseStatus
And print response