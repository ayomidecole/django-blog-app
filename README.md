Steps
1. Define data model (models.py)
2. Set up admin panel (admin.py)
3. Set up views (views.py) - what is rendered to the user from the model/database
4. Set up URLs (urls.py) - what URLs are available to the user from the views
5. Set up templates (templates/) - what the user sees

The request/response cycle (update at the end)
1. User makes a request to the server
2. Django checks urls.py to see what view to use
3. Django calls the view, which returns a response and selects the appropriate html template specified in the view, it also gets data from the model
4. Django sends the response back to the user with the html template 

Extending Functionality