# django-models3-cw_b

### Exercise 1
Create a Book model with name, pageNumber, genre, and publishDate attributes. Create 2 entries using 2 different methods (admin site and class construtor using an endpoint).

Create an 'all/' endpoint that prints out all entry names, create a new endpoint that only prints entries with publish dates greater than or equal to 01/01/2018.

### Challenge
In Exercise 1 create another new endpoint to change genre of at least one entry with a publish date greater than or equal to 01/01/2018 to "fiction".


September 25, 2019 - 17:02:34
Django version 2.0.6, using settings 'myProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[25/Sep/2019 17:02:36] "GET / HTTP/1.1" 200 11
[25/Sep/2019 17:03:08] "GET /allBooks HTTP/1.1" 301 0
Alchemist
Seven Habbits
[25/Sep/2019 17:03:08] "GET /allBooks/ HTTP/1.1" 200 9
