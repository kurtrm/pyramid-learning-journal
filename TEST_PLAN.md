#Pyramid Learning Journal Test Plan

#So Far:
-Test that the create view returns a response object:
    -- Returns an empty dictionary when the page is loaded.

-Test that the the create view returns an error:
    -- Ensure that either the title or price is filled out.

-Test that the POST goes through:
    -- Updates database with at least title filled out.

-Test that create view redirects after submission:
    -- Ensure that the view redirects to the home page that will contain their new listing.

-Test that the application redirects to the list view:
    -- Ensure the test application functions properly by sending the user back to the home page.

-Test page contains proper html:
    -- Ensure the home page contains the new entry title.


#To Do:
-Test that we can update a journal entry:
    -- Test that the information is updated by the edit view.

-Test that the application updates a journal entry:
    -- Test the routes and views are set up properly.

-Test that the user is redirected to the detail view after edit submission:
    -- Ensure the contains the updated information.

-Test that edit view contains info in boxes when edit is clicked on detail view:
    -- Ensure jinja is putting the information in the html.

-Test that application follows through with functionality:
    -- Functional test will ensure application itself is working by providing the user with the previous data of an entry and properly submitting it to the database.

-Test 404s for incomplete information:
    -- Ensure 404 is raised if no fields are filled out upon submission.