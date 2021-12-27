<h1 align="center">Data Engineer Take Home Assignment</h1>

# Challenge
Thank you for your interest in joining our data engineering team.

In this take-home exercise you’ll be working in an imaginary company. The company’s product is a deal alert app for PC games. For this we will rely on the data provided by the [CheapShark API](https://apidocs.cheapshark.com/#c6e4678d-7ff0-ebd4-59c1-b4d0fb3dac87).

We are interested in keeping information about all the current deals per store. We want to be able to track when a deal has changed or is not available anymore. In order to create the alert we will also need detailed information of the game and the store related to that deal. 

Keep in mind the limitations offered by the API when you develop your solution.

Please take your time, you can submit your results within 3 days of receiving this assignment.

## Task 1
Create an Airflow DAG(s) that will fetch data from the CheapShark API every hour. The data that we are interested in is `Deals`, `Games` and `Stores` information.

## Task 2
Store the data obtained from task 1 in a RDBMS of your choice. Please include the DDL statements of the tables and a visual diagram of the model.

## Task 3
Create a query that shows how much has the price of a game increased in comparison to its `cheaper price ever` and its `costlier price ever`. The query must show the price increase in %, the name of the game, dealId of the costlier price ever and the name of the store of that deal.

## Task 4
Create a query that shows when a `Deal` is not available anymore or when a `Deal` is not on sale anymore.

## Task 5
Imagine that we become partners with CheapShark, and we agreed to get new and updated information from `Deals` through webhook events. Please describe how would you ingest this information to the database using any service(s) from the AWS ecosystem.

The expected input would have the following structure
```
[
  {
      "event": "deal.changed",
      "internalName": "DEUSEXHUMANREVOLUTIONDIRECTORSCUT",
      "title": "Deus Ex: Human Revolution - Director's Cut",
      "metacriticLink": "/game/pc/deus-ex-human-revolution---directors-cut",
      "dealID": "HhzMJAgQYGZ%2B%2BFPpBG%2BRFcuUQZJO3KXvlnyYYGwGUfU%3D",
      "storeID": "1",
      "gameID": "102249",
      "salePrice": "2.99",
      "normalPrice": "19.99",
      "isOnSale": "0",
      "savings": "85.042521",
      "metacriticScore": "91",
      "steamRatingText": "Very Positive",
      "steamRatingPercent": "92",
      "steamRatingCount": "17993",
      "steamAppID": "238010",
      "releaseDate": 1382400000,
      "lastChange": 1621536418,
      "dealRating": "9.6",
      "thumb": "https://cdn.cloudflare.steamstatic.com/steam/apps/238010/capsule_sm_120.jpg?t=1619788192"
   },
  {
    "event": "deal.new",
    "internalName": "THIEFDEADLYSHADOWS",
    "title": "Thief: Deadly Shadows",
    "metacriticLink": "/game/pc/thief-deadly-shadows",
    "dealID": "EX0oH20b7A1H2YiVjvVx5A0HH%2F4etw3x%2F6YMGVPpKbA%3D",
    "storeID": "1",
    "gameID": "396",
    "salePrice": "0.98",
    "normalPrice": "8.99",
    "isOnSale": "1",
    "savings": "89.098999",
    "metacriticScore": "85",
    "steamRatingText": "Very Positive",
    "steamRatingPercent": "81",
    "steamRatingCount": "1670",
    "steamAppID": "6980",
    "releaseDate": 1085443200,
    "lastChange": 1621540561,
    "dealRating": "9.4",
    "thumb": "https://cdn.cloudflare.steamstatic.com/steam/apps/6980/capsule_sm_120.jpg?t=1592493801"
  }
]
```


## Task 6
Please provide a documentation by updating this README.md about what you think important regarding your works in Task 1, 2 and 5.

# Submission
Please create a `private` github repo that contains this file along with your code and share with these users
- `dmartinez-ch`
- `dtroyo-ch`

So that we can see your commits or any activities you like to demonstrate!
Good luck!