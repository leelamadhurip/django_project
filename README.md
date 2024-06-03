Movie Search Application:
Overview
The Movie Search Application is a web-based platform that allows users to search for movies and manage personalized movie lists. Users can create new movie lists, add movies to existing lists, and view movie details fetched from the OMDb API.

Features
Movie Search: Users can search for movies by entering keywords in the search bar.
Movie Details: Display detailed information about each movie, including the title, year, and poster image.
Movie Lists: Users can create new movie lists and add movies to these lists.
Interactive UI: The application features an attractive and responsive user interface.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Django (Python)
API: OMDb API for fetching movie details
Database: SQLite (or any other database supported by Django)

Movie Search
Search for a movie: Enter the movie name in the search bar and click the "Search" button.
View movie details: The search results will display the movie title, year, and poster. Clicking on a movie will display more details.
Movie Lists
Create a new list:
Scroll down to the "Create New Movie List" section.
Enter a name for your list and click the "Create List" button.
Add a movie to a list:
In the search results, select a list from the dropdown menu.
Click the "Add to List" button.

API Integration
This application uses the OMDb API to fetch movie details. You need to obtain an API key from OMDb and add it to your environment variables or settings file.

Security
CSRF Protection: Forms are protected against Cross-Site Request Forgery (CSRF) attacks using Django's built-in CSRF protection.
Authentication: User authentication is managed using Django's built-in user model and admin interface.


Please run it in VS Code to view the results
