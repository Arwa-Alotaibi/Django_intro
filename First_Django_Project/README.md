First Django Project

Objectives:

Practice setting up a new Django project
Practice setting up a new Django app
Practice routing in Django
Familiarity with views and how to return a response
It's time to practice routing! Use the checklist below to add routes to your project. 

***Note*** for the assignment, the show, edit, and delete methods will require the use of Route Parameters.  

***Bonus*** result:


Create a new project with a single app

/ - redirects to the "/blogs" route with a method called "root"

/blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"

/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"

/blogs/create - redirect to the "/" route with a method called "create"

/blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15')

/blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"

/blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"

(**Bonus**) /blogs/json - return a JsonResponse with title and content keys.
