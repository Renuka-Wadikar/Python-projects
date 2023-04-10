# What is this project?

This is an implementation of creating a Web Api for getting the weather information about particular city , on particular date, and in particular year

## API Format


URL format: http://127.0.0.1:5000/api/v1/station/date

Example for a station on particular date: http://127.0.0.1:5000/api/v1/10/1988-10-25

Example for a station on all dates: http://127.0.0.1:5000/api/v1/10

Example for stations on given year: http://127.0.0.1:5000/api/v1/year/10/1988 

## API result

{
  "date": "1988-10-25",
  "station": "10",
  "temprature": -0.9
}

## Project Image

![Screenshot (5)](https://user-images.githubusercontent.com/84169629/230831737-1552c51d-b04e-4341-8c99-43d927b0e11a.png)
![Screenshot (6)](https://user-images.githubusercontent.com/84169629/230831361-ad50bfe3-9479-4b41-805c-a8cf15feccf4.png)
