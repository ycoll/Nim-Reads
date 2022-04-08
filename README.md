# Nim Reads



I have created a book review website that has full CRUD functionailty and works on all devices. Users can Create reviews through a form, Read reviews on the landing page, Edit and Delete reviews with the click of a button.

[Heroku Website link here](https://nim-reads.herokuapp.com/) 
## UX
 
My main goal when designing this website was to create something that fully implements CRUD functionality in an easy to use and visually appealing way. I went for dark blue and white for a clean look that promotes readability and I wanted the books/reviews to be the main focal point. I decided on typography that was visually interesting but also easy to read.   

User Stories:
- As a user, I want to read reviews.
- As a user, I want to add my own reviews.
- As a user, I want my review to display nicely.
- As a user, I want to edit a review.
- As a user, I want to delete a review.
- As a user, I want to contact someone if I have a question.
- As a user, I want to easily navigate this website.
- As a user, I want to use this website on my phone. 


I have included my plans for the project in a wireframes directory. These include hand drawn wireframes for both desktop and mobile devices.

## Features
 
- Sticky navbar - Allows user to easily navigate at any time.
- Collapsible navbar/sidenav - Allows user to navigate easily on a small screen.
- Clickable book review card - The user can click the cover and the review appears, allows easy access to content.
- Edit button - On click the user is taken to an edit review page where they can edit the clicked review or delete it using the delete button.
- Add a review page - This contains a form that allows the user to submit their own review.
- Get in touch page - This contains a fully functioning form that allows the users to contact me through my email.

## Technologies Used


- HTML
- CSS
- Javascript
- JQuery
- Materialize - Used to layout my website

- Python - Back-end language used
- PyMongo - API for MongoDB
- Flask - microframework used

- MongoDB Atlas - Database storage

- gitpod - IDE used for writing all code
- GitHub - Version control
- Heroku - Hosting app

## Testing

1. Nav:
   1. Click on each link and verify they work.
   2. Whilst on each page verify the links work from there.
   3. Use different screen sizes and verify that navbar collapses into icon.
   4. Click icon and verify that a sidenav opens, verify each link is there and functioning.
   4. Repeat clicking each link with each different screen size and verify they work. 

2. Review card/ Edit/ Delete:
    1. Click on cover and verify review appears.
    2. Click X button and verify review disappears.
    3. Click edit button and verify that we are taken to edit review page 
    4. Change content in form and click update button, verify we are taken back to landing page.
    5. Click on cover and verify content has changed.
    6. Check database to check that content was updated.
    7. Click edit button again, once on edit review page click delete button, verify we are taken back to landing page.
    8. Once on landing page, verify review is gone.
    9. Check database to verify review was deleted.

3. Add a review form:
   1. Click on add a review link and verify that we are taken to correct page.
   2. try to submit empty form and verify that fields are required.
   3. Fill in form and submit, verify that we are taken to landing page.
   4. Check to see if new review is there and verify form worked.
   5. Check database and verify that is was added.

4. Contact Form:
   1. Click on get in touch link and verify that we are taken to correct page.
   2. try to submit empty form and verify that fields are required.
   3. Fill in form and submit, verify that the fields empty.
   4. Check email to see if message is there and verify form worked.

I have extensively tested this website on different screen sizes and have found it to be fully responsive.



  ### Bugs

  - When tested on small mobile screens my text would spill out way to far down. I corrected this by changing the text size to be more responsive using rem.
  - On medium screens my book review covers would stretch and become unsightly so I changed it so two could fit on the screen at the same time in a more visually appealing way. 

  - I had some trouble setting up an enviroment variable because I was taught to do it using cloud9 and am now using gitpod. In cloud9 you place in in the bashrc file but that doesn't work with gitpod. I learned how to do it and it is all correct now.  


### Validators

  - I used validators for all my code, all of them came back with no errors. Screenshots of each are included in a seperate directory called validator-results.


## Deployment

I deployed my app on Heroku.

To do this I did the following:

1. I created my Heroku Account and made an app.
2. I created a requirements.txt file in the CLI by typing: pip3 freeze --local > requirements.txt.
3. I created a Procfile in the CLI by typing: echo web: python run.py > Procfile
4. I then went back to my Heroku Dasboard and went to the Deploy section
5. I chose Github as my deployment method and linked my accounts.
6. I then updated my config vars and my app was ready.


To run code locally:

1. Run- "python3 app.py" in the CLI 
2. This will reveal the open port 8080 which you can open in the browser by clicking that option. 

## Credits

### Content
- The text for each review was copied from the corresponding wikipedia page:
            - [The Alchemist](https://en.wikipedia.org/wiki/The_Alchemist_(novel))
            - [Harry Potter](https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone)
            - [The Hobbit](https://en.wikipedia.org/wiki/The_Hobbit)

### Media
- The photos used in this project are from pexels.com

### Acknowledgements

- I received inspiration for this project from mini projects that are in my course and goodreads.com.
