Feature: Karate Test

Scenario: GET DEMO 1
Given url 'http://reqres.in/api/users?page=2'
When method GET
Then status 200
And print responseStatus
And print response

Scenario: Post student
Given url 'http://localhost:5000/students/add'
And request
"""
{
    "FirstName": "Giovani",
    "LastName": "Picolini",
    "class": "2b"
}
"""
When method POST
Then status 201