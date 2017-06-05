"""All journal entries."""

ENTRIES = [
    {
        "id": 0,
        "title": "May 15, 2017",
        "creation_date": "May 15, 2017",
        "body": '''Through the Python 401 intro page, I discovered two data science meetups at Galvanize. I signed up for a meetup next week there. I also got a better grasp on what exactly several common errors are telling me is wrong with my code.'''
    },
    {
        "id": 1,
        "title": "May 16, 2017",
        "creation_date": "May 16, 2017",
        "body": '''I wasn't initially planning on using recursion to tackle the Fibonacci and Lucas sequence, but Lynn opened my eyes to it. I didn't understand it at first, and I'm still on the fence about it, so I will likely need to meditate on it later. Otherwise, the parametrized tests were really cool and sped things up.'''
    },
    {
        "id": 2,
        "title": "May 17, 2017",
        "creation_date": "May 17, 2017",
        "body": '''I learned a lot today. Here's a sampling: -dict() doesn't want an expression as an argument. It wants a damn value that requires no additional work to figure out -setdefault() is nice -Learned about io, will read the docs later. -Constantly learning how to be a better communicator
I think I am underestimating the workload of assignments. I think I know what to do, but then it's all the little baby in-between steps that I get hung up on. Also, communicating what's in my head and understanding someone else has consistently been challenging in pair programming spanning 201, 301, and 401.
'''
    },
    {
        "id": 3,
        "title": "May 18, 2017",
        "creation_date": "May 18, 2017",
        "body": '''The setup.py was pretty interesting. I need to look up more about iterators. I'd like to know what's happening in between calling for a set of keys or values, getting an iterator, and then having to make a list of the keys or values, rather than a list automatically being returned. Also, Lynn raised some good questions. We clarified hoisting and the position of definitions in relation to where they are being called. For the mailroom assignment, the flow chart and pseudocode helped considerably in getting on the same page. Also, writing tests is difficult. We are still learning to be better at writing the tests first.'''
    },
    {
        "id": 4,
        "title": "May 19, 2017",
        "creation_date": "May 19, 2017",
        "body": '''
Learned to implement a dictionary comprehension and got some more practice with list comprehensions. Corrected some issues that were preventing me from using tox. I think I'm not using dictionaries enough; they've been very handy when I've used them.'''
    },
    {
        "id": 5,
        "title": "May 22, 2017",
        "creation_date": "May 22, 2017",
        "body": '''During our sockets assignment, I learned that the conn.recv will stall if the message it received was exactly equal to the buffer length. If it was less than our buffer length, our logic would catch this and terminate the while loop. Otherwise, it restarts the while loop and sits at that part of the script. After doing some reading on line, some posts recommended using terminators, so a specific combination of characters that our logic can interpret as the end of the message. There's an arbitrary terminator, but I'm wondering how we can make this more reliable, cause I still there are edge cases we're missing.
As far as the data structures assignment goes, I had a hard time grasping linked lists, but after looking at stuff with Anna, I think I understand how to move forward with creating our linked list class.'''
    },
    {
        "id": 6,
        "title": "May 23, 2017",
        "creation_date": "May 23, 2017",
        "body": '''Working through tests with Anna has been really great. We really got into a rhythm with writing tests for our linked list methods until we got to the delete method. That was a little more challenging since you to change attributes of several different nodes. Also, reviewing blocking sockets and developing some terminators for our echo script was great.'''
    },
    {
        "id": 7,
        "title": "May 24, 2017",
        "creation_date": "May 24, 2017",
        "body": '''With the constant exposure to http headers, I've started to retain more information about them. The format of the headers, particularly. I tried to wrap my head around when to use class methods, but Patrick and Nick helped me get to a point that I think I understand them.

Anna and I have caught up on our data structures. Removing a a few methods and adding a dash of logic and new attributes, I think we'll have our double linked list tomorrow.'''
    },
    {
        "id": 8,
        "title": "May 25, 2017",
        "creation_date": "May 25, 2017",
        "body": '''I learned you could raise an exception and store whatever is in parentheses into a variable, or you could pass it as an argument into another function. This was useful in managing our exceptions in step2 of the server. I'm very happy with how Morgan and I have used regular expressions to simplify the logic in parsing the header; I think we saved ourselves a lot of time this way even though we had to work through some other logic!'''
    },
    {
        "id": 9,
        "title": "May 26, 2107",
        "creation_date": "May 26, 2017",
        "body": '''Munir helped me and Morgan today, where we learned an awesome thing: exception arguments can be accessed like a tuple. This was a speed bump that we ran into a few times in some shape or form, and we finally got through it. I appreciated the tone of the Python grads today; they seemed both realistic yet optimistic and positive.'''
    },
    {
        "id": 10,
        "title": "May 31, 2017",
        "creation_date": "May 31, 2017",
        "body": '''Applying what we learned today to our pyramid learning journal wasn't too hard, jinja seems like a pretty awesome and convenient thing to use. For some reason I find it more intuitive than handlebars.js. Refactoring using the config_views was pretty awesome, and Ophelia and I made some great progress on her project. I think I got the hang of the matchdict method, which was only a minor hang up during our lecture today. I was really happy when we are able to import the entries dictionary from the data file in our data folder.
This heap data structure has proven challenging, but I think Anna and I are going to take care of business.'''
    }
]
