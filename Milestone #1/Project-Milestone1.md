## Project Milestone 1
__For Milestone #1, the objectives are to:__
* Know what techniques to use / Consolidate research approach
* Start writing code
* Updated Project Report
* Complete data set, which in my case are appropraite software requirements

__In regards to knowing which techniques to use and consolidating my project approach__
* In the grand scheme, I plan on using Python to create a method of automating extraction of requirements from documents, how-to guides, tutorials, etc.
* For the first steps, I always like to start with the happy path, a route which should encounter no errors or exceptions. It can cover a large portion of the workflow, and if it doesn’t work smoothly, the rest of your testing may be blocked. In this example, the happy path would be something like this:

    1. Purchase items from general search
    2. Click order history from accounts page
    3. Verify that previously ordered items are displayed
    4. Add items to cart from the previously ordered list
    5. Complete purchase of previously ordered items

When the code is delivered to me for testing, this would be the first test case to execute.

__Code__
* From a pseudocode standpint, here is what I want to achieve
'''sh
$git clone
'''

* However, this is at the point I am now:
'''sh
$git clone
'''

__Updated Project Report__
* I will move away from testing educational and medical requirements documents to doing the same with software test cases.
* Here is an example of a test case:

    * Title: Login Page – Authenticate Successfully on gmail.com
    * Description: A registered user should be able to successfully login at gmail.com.
    * Precondition: the user must already be registered with an email address and password.
    * Assumption: a supported browser is being used.

### Test Steps:

   1. Navigate to gmail.com
   2. In the ’email’ field, enter the email address of the registered user.
   3. Click the ‘Next’ button.
   4. Enter the password of the registered user
   5. Click ‘Sign In’

*Expected Result: A page displaying the gmail user’s inbox should load, showing any new message at the top of the page.
