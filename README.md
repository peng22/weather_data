# weather_data
This project shows how we collect weather data like humidity and temerature and 
provides a summary for every 10 records.

## Description
- The user can input the weather and humidity data.
- The input is validated to be in a specific range.
- Then the data is lised in a table.
- The data is styled to be red for high values to catch them easily.
- The table has arrows that shows how if the value increases or decreases.
- The summary table provides the summary row for each 10 rows in the main table.

## Instructions
- Clone the project.
- Create python virtual environment.
  python3 -m venv <your-env-name>
- Install the requirements.
  pip install -r requirements.txt
- Make the migrations.
  python manage.py makemigrations && python manage.py migrate
- Run the project.
  python manage.py runserver
  
## Technologies used
- Python 
- Django
- JavaScript
- HTML
- CSS

## Demo
- http://peng23.pythonanywhere.com/list_weather_data

## Author
- Mohamed Elsayed
