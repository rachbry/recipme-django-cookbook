# Welcome to RecipMe

## Introduction

Are you tired of looking through recipe books, sifting through notes, scrolling through blog posts or bookmarks trying to find the recipe that you know you have somewhere? 

Welcome to RecipMe, a place where you can easily store, retrieve and edit your favourite recipes all in one place.  This website if for anyone who loves to cook but doesn’t love wasting valuable cooking time searching for their favourite recipes. 

![Screenshot 2023-12-07 at 11 04 34](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/e891dd76-414b-40aa-89f0-7e343ef8a5fa)

## Why choose RecipMe? 

From the latest trends to secret family recipes, the simple interface and navigation within RecipMe enables you to not only input your recipes but to edit, tweak or customise them with ease.  Our search functionality ensures these are all easily accessible. 

Browse through our own recipes for inspiration and to your collection.

RecipMe is accessible on all devices, meaning whether you are at home, cooking with others or in the supermarket, you can access your recipes anywhere, anytime.   

---

## Persona
Persona: Meet Cooking Enthusiast Sarah 

### Background: 
- **Age:** 30 
- **Occupation:** Marketing Professional 
- **Hobbies:** Cooking, hosting dinner parties, exploring new cuisines 

### Challenges: 
- Sarah loves to cook and often experiments with various recipes. 
- She has a collection of recipe books, handwritten notes, and bookmarked online recipes. 
- Finding a specific recipe quickly is challenging, especially when she's short on time. 

### Goals: 
- Emily wants a centralised platform to organize her favorite recipes. 
- She desires a user-friendly solution that saves her time in the kitchen. 
- Accessing her recipes from any device is important for her busy, on-the-go lifestyle. 

### Needs: 
- An easy-to-use platform to store, categorise, and retrieve recipes. 
- Quick editing capabilities for personalizing recipes based on her preferences. 
- Mobile-friendly access for convenience while shopping or cooking. 

### How RecipMe Helps: 
- RecipMe provides Sarah with a digital recipe organiser. 
- She can easily add, edit, and categorise recipes, making them easily accessible. 
- The platform's responsive design ensures she can access her recipes from her smartphone or tablet in the kitchen. 

## Target Audience: 
Cooking Enthusiast Sarah represents the target audience for RecipMe: 

- **Age:** 25-40 
- **Occupation:** Professionals with busy lifestyles 
- **Hobbies:** Cooking, food blogging, exploring new recipes 
- **Pain Points:** Difficulty in organising and finding recipes quickly 

**RecipMe caters to individuals like Sarah who are passionate about cooking and seek a convenient solution to manage their recipe collections efficiently.** 


## User Stories

As a non-logged in user:

|I want to.. | So that I can.. | Acceptance Criteria
| ----------- | ----------- | ----------- |
| Create an account | Store my personal recipes | 1: user can create account  2: user can log in  AC 3: user can log out
| Browse through recipes | Find some new meals ideas | 1: Admin created recipes are available to all users 2: Non logged in users can view admin created recipes 3: Non-logged in users have read only access |


As a logged in user:

|I want to.. | So that I can.. | Acceptance Criteria
| ----------- | ----------- | ----------- |
| Create an account | Store my personal recipes | 1: user can create account 2: user can log in 3: user can log out  |
| Edit or delete my recipes | Update them  | 1: Edit recipes functionality 2: Delete recipes functionality 3: Only for user who created the recipe, 403 error returned otherwise |
| Add picture and description to my recipes  | I can easily find the one I am looking for  |  1: add picture when uploading recipes 2: Pictures automatically resized 3: Can add a  recipe description |
| Store my recipes in one place  | I can easily browse and retrieve them  |  1: Create list view of all user recipes 2: Make each object a link to the full recipe |
| View the ingredients and method for my recipes  | Follow the recipe without having to touch the screen |  1: Put ingredients and methods side by side so both available on md and lg screens without scrolling |
| Have a personalised home page | View my own recipes | 1: Have generic home page 2: Have logged in user home page 
| Categorise my recipes by cooking method | Plan my meals easily |  1: Have categories to choose from on add recipe  2: Be able to filter recipes using these categories |
| Be able to log into the same account as my family  | my household can share an account |  1: Be able to log in by username 2: Have keep logged in function available |
| Search my recipes | To quickly find the recipe I want  |  1: Search bar in navigation 2: search bar functionality added 3: Have a variety of parameters to search with |
| Add recipes to favourites | View my favourite recipes easily |  1: Create add favourite button 2: Apply to user or admin recipes 3: Display these on their own page 4: Have indicator on recipe to skow if favourite or not |


Out of scope for this release:

|I want to.. | So that I can.. | Acceptance Criteria
| ----------- | ----------- | ----------- |
| Share recipes I have created | family and friends can view them  |  1: Share by email 2: Share read only with other users |
| Add notes to my recipes  | Record any tweaks or changes made | 1: Create note box 2: Be able to add text to this and save without admin approval |
| Prevent my device going into sleep mode on the recipe detail page | Prevent my device going into sleep mode on the recipe detail page | 1: Create button on full_recipe.html for no sleep mode 2: Create functionality for this |
| Submit my recipe to admin to be available for all users | Share this recipe with everyone on the site | 1: Be able to submit admin recipe request 2: Admin can approve and submit to general site |



## Workflow
### Agile Methodology
For this project I adopted an Agile methodology.  This is the first time I have used this on a solo project although I have used it as a group during the hackathons.  I feel this has helped me to:
- Organise and prioritise my workflow.  This has been essential due to the very limited timeframe we had to complete this project.
- Enabled me to adjust my expectations and still produce the required MVP

I created a site map and workflow diagram:
![Screenshot 2023-12-07 at 14 12 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/c5ed706d-1b01-4a22-8e40-6e4ff5511e61)

I used Github projects to convert my user stories into actionable tasks.  The acceptance criteria was very helpful to ensure all necessary tasks were completed.
![Screenshot 2023-12-07 at 14 17 28](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/3e491c10-88c9-4477-96e9-c529f37d60bc)

### Models
In RecipMe I used the Django AllAuth User Model and created a custom Recipe Model.  This included the following fields:

|      Name            |     Type                   |     Key  |
|----------------------|----------------------------|----------|
|      user            |     User Model             |     FK   |
|      title           |     CharField              |          |
|      slug            |     CharField              |          |
|      description     |     CharField              |          |
|      instructions    |     RichTextField          |          |
|      ingredients     |     RichTextField          |          |
|      freezable       |     boolean                |          | 
|      serving         |     CharField              |          |
|      image           |     ResizedImageField      |          |
|      image_alt       |     CharField              |          | 
|      Recipe_type     |     CharField  dropdown    |          |
|      Cooking_method  |     CharField  dropdown    |          |
|      posted_date     |     DateTimeField          |          |

I also added a many to many field called is_favourite to enable the favourite functionality.


## Design
### Wireframes and Features
The site will be fully responsive and accessible on mobile, tablet and desktop devices.

The homepage will feature a jumbotron image and call to action button.  Reasons why you should join will be listed here.

![Screenshot 2023-12-07 at 13 50 23](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/112af580-6678-4e52-b3f3-76db12c4f240)


**All Users:**
- Are able to view admin added recipes
- Are able to use the search functionality

**Logged In Users:**
- Can add recipes
- Can view, edit and delete their own recipes
- Can add recipes to their favourites
  
They will have a personalised home page with all their recipes on it and will be able to view recipes they have favourited, both from their own and the site recipe collections.  Each recipe card will be a clickable link to the full recipe.  The same page layout will be used for the recipe collection, the users homepage and the favourite recipes page to maintain consistency and simplicity throughout.

![Screenshot 2023-12-07 at 13 33 50](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/f688c986-8040-48cb-938a-64b20b189f72)


**The Full Recipe Page:**
Will contain all the relevent information for each recipe.  Design will ensure all ingredients and instructions are available on one screen for desktop and tablet.

![Screenshot 2023-12-07 at 13 36 14](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/3e8edc07-582b-41de-8cd6-6ce59475f3be)


**Add / Edit Recipe Page:**
Front End CRUD will be available to add / edit recipes for logged in users.  The form will include category dropdowns and the ability to upload an image.

![Screenshot 2023-12-07 at 13 42 11](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/42943578-41c6-4061-b0e4-e9debaa239bd)

## Design Choices
###  Colours
### Typography
Colour Pallete:

![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/027c781a-346b-4ed8-93ed-9a42815c0f0f)

Logo:
![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ea618f02-99f6-4947-a764-8ffe40bb4155)
### Walkthough of site including screenshots of every page

### Future Features
Future features not implemented at this time include:
- The ability on the full recipe page to toggle on/off dark mode and prevent your screen turning off, a feature I feel would be very useful when following a recipe
- Recipe sharing - To be able to share recipes with other users of the site or to email them to others
- Upload recipes to main site - The ability to request admin approval for a recipe to be added to the site wide collection

## Testing
### Validation Testing
**HTML**

I used the W3.org validator on my HTML and CSS files.  Please see results below:

|File | URL | Screenshot | Notes |
|-----|-----|------------|-------|
|Homepage (not logged in) | [URL](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2F) | ![Screenshot 2023-12-07 at 18 52 31](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/048815c1-1ef8-42da-92ee-175959a77282)
 | Document checking completed. No errors or warnings to show. |
 | Register | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Faccounts%2Fsignup%2F#l93c293 | ![Screenshot 2023-12-07 at 18 56 09](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/b60f5593-5cd8-4304-93f2-c0bb36ee66f0)
 | Error within AllAuth |
| Login | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Faccounts%2Flogin%2F#l93c293 | ![Screenshot 2023-12-07 at 18 59 30](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/11f92942-f26f-40fa-bced-ab5afd6af881)
| Document checking completed. No errors or warnings to show. |
 |Recipes (not logged in) | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Frecipes%2F | ![Screenshot 2023-12-07 at 18 54 09](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/d8a3b516-a6e2-43ef-a09f-422862b9d6c9)
 | Document checking completed. No errors or warnings to show. |
  |Recipes (not logged in) | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Frecipes%2F | ![Screenshot 2023-12-07 at 18 54 09](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/d8a3b516-a6e2-43ef-a09f-422862b9d6c9)
 | Document checking completed. No errors or warnings to show. |
 | Search Results (not logged in) | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fsearch%2F%3Fq%3DPancakes#l93c293 | ![Screenshot 2023-12-07 at 19 05 50](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/dd1cb632-6f77-468d-a233-3d71433e7b85)
 | Error showing related to unclosed element - unsure how to fix as content is dynamically generated |
 | Full Recipe Page | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Frecipes%2F30%2F#l93c293 | ![Screenshot 2023-12-07 at 19 12 12](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/e8527226-ae3b-4699-9e5d-50f4a59fcf26) | Error showing related to unclosed element - unsure how to fix as content is dynamically generated |
 | Full Recipe Page | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Frecipes%2F30%2F#l93c293 | ![Screenshot 2023-12-07 at 19 12 12](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/e8527226-ae3b-4699-9e5d-50f4a59fcf26) | Error showing related to unclosed element - unsure how to fix as content is dynamically generated |

  | Logged in home page | [https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Frecipes%2F30%2F#l93c293](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fmy_recipes%2F#textarea) | ![Screenshot 2023-12-07 at 19 17 56](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/5bd9c27f-5ae9-4513-9913-ab2344a5c7fb)
 | Document checking completed. No errors or warnings to show. | 
| Add Recipe | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fadd_recipe%2F#textarea | ![Screenshot 2023-12-07 at 19 25 49](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/fe8d7257-ca9d-43a4-932e-a4172d5c7bec) | Document checking completed. No errors or warnings to show. |
| Edit Recipe | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea | ![Screenshot 2023-12-07 at 19 34 04](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/4ad1af3d-caf2-4d62-8e86-f3ee492bb058)
| Document checking completed. No errors or warnings to show. | 
| Delete Recipe | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea | ![Screenshot 2023-12-07 at 19 36 41](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/de6e03b8-db6f-425f-b47b-993905a8450b) | Document checking completed. No errors or warnings to show. |
| Log out | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea | ![Screenshot 2023-12-07 at 19 38 24](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/700ea94f-63b1-431d-bcbe-66666a8a50f9) | Document checking completed. No errors or warnings to show. | 

I received this error when add the urls for the logged in pages.  I copied the page source and pasted in to get the above results.
![Screenshot 2023-12-07 at 19 29 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/f8ab92ac-08a3-43b5-99b9-15dd3c88d036)


**CSS**
| Base.css | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea | ![Screenshot 2023-12-07 at 19 43 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/80bfed4a-a1a8-4b82-9772-a79c5fe5f96c)
 | Document checking completed. No errors or warnings to show. |

**PYTHON**

I used the CI Python Linter https://pep8ci.herokuapp.com/# on all my .py files. Please see results below.

**In the My_project Directory:**
- urls.py:
![Screenshot 2023-12-07 at 18 19 56](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/765148bc-e8ad-4659-9c85-0d61a5508012)

- settings.py:
![Screenshot 2023-12-07 at 18 26 08](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/a31948da-dec9-472c-ad27-b757460da4ec)


**In the Home App:**

- urls.py
![Screenshot 2023-12-07 at 18 15 51](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/f49faa61-b794-40cd-8e3d-cc2fb1ccbf65)

- views.py
![Screenshot 2023-12-07 at 18 04 27](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/1e5b9425-e441-4fc5-bd9d-afc0d005e81a)


**In the Recipes App:**

- admin.py
![Screenshot 2023-12-07 at 18 12 48](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ef6e7e04-9cab-422f-be0a-96299043c171)

- forms.py
![Screenshot 2023-12-07 at 18 05 43](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/a1806f45-df34-42f2-b8ec-7727aa0d7d4e)

- models.py 
![Screenshot 2023-12-07 at 18 02 20](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ea779dea-51dc-4603-9dd6-8b37cb07907b)

- urls.py
![Screenshot 2023-12-07 at 18 01 26](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/7df29fff-2cf3-4129-b52a-a7b5670677b4)

- views.py               
![Screenshot 2023-12-07 at 17 59 58](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/52dc1537-b18e-4219-97f4-aa38e1591b36)


**Lighthouse**

I used Lighthouse to check the quality of my web pages.  Some results are shown below:

-logged in home page Desktop
![Screenshot 2023-12-07 at 19 59 20](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6a7d8cf9-b181-494a-a7c1-4373a9284876)

- logged in home page Desktop
![Screenshot 2023-12-07 at 20 03 49](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/da30f0b4-ed88-4a2a-bf9e-fb33dace8cfe)




### Manual Testing
| `Feature` | `Expected Outcome` | `Testing Performance` | `Result` | `Pass/Fail`|
| ----------|--------------------|-----------------------|----------|------------|
| `Navbar` |  |
| Logo  | When clicked user will be able to be redirected to the Home Page. | Clicked on logo | Redirected to the Home Page  | Pass |
| Home link | When clicked user will be able to be redirected to the Home Page. | Clicked on Home  | Redirected to the Home Page | Pass |
| Menu link | When clicked user will be able to be redirected to the Menu Page. | Clicked on Menu  | Redirected to the Menu Page | Pass |
| Register link | When clicked user will be able to be redirected to the Sign Up Page. | Clicked on Register  | Redirected to the Sign Up Page | Pass |
| Login link | When clicked user will be able redirected to the Sign In Page. | Clicked on Login  | Redirected to the Sign In Page | Pass |
| Booking Details | When clicked user will be able redirected to the Booking Details Page. | Clicked on Booking Details  | Redirected to the Booking Details Page | Pass |
| `Header`  | |
| "Book Now!/Register To Book A Table!" Button    | When clicked the user will be redirected to the Booking/Sign Up Page  | Clicked Button  |  Redirected to the Booking/Sign Up Page  | Pass |
| `Sign Up Form` |
| Sign In link | Redirected to sign in page | Clicked | Redirected to sign in page  | Pass |
| Taken Username | Sign up is unsuccessful | Entered a taken username | Sign up was unsuccessful  | Pass |
| Taken Email | Sign up is unsuccessful | Entered a taken Email | Sign up was unsuccessful  | Pass |
| Email without @ | Sign up is unsuccessful | Entered an Email without @ | Sign up was unsuccessful  | Pass |
| Password that's similar to username/email | Sign up is unsuccessful | Entered a password that's similar to username/email| Sign up was unsuccessful  | Pass |
| Password with less than 8 characters | Sign up is unsuccessful | Entered a password with less than 8 characters | Sign up was unsuccessful  | Pass |
| Commonly used password | Sign up is unsuccessful | Entered a commonly used password | Sign up was unsuccessful  | Pass |
| Numbers only password | Sign up is unsuccessful | Entered a numbers only password | Sign up was unsuccessful  | Pass |
| Valid Sign Up Form | Sign up is successful | Entered a valid sign up form | Sign up was successful  | Pass |
| `Sign In Form` |
| Sign Up link | Redirected to sign up page | Clicked | Redirected to sign up page  | Pass |
| Incorrect username | Sign in is unsuccessful | Entered a incorrect username | Sign in was unsuccessful  | Pass |
| Incorrect password | Sign in is unsuccessful | Entered a incorrect password | Sign in was unsuccessful  | Pass |
| Correct username & password | Sign in is successful | Entered a correct username & password | Sign in was successful  | Pass |
| Remember Me | Stayed logged in next time I enter site | Re-entered site | Still signed in  | Pass |
| `Sign Out Page` |
| Sign Out Button | Signed Out | Clicked Sign Out Button | Was signed out  | Pass |
| `Booking Form` |
| Past Date Submitted | Booking is unsuccessful | Entered a past date | Booking was unsuccessful  | Pass |
| Booking for an already booked time of the same user. | Booking is unsuccessful | Entered an already booked time | Booking was unsuccessful  | Pass |
| Valid Form | Get a booking confirmation | Entered a valid form | Got a confirmation of my booking  | Pass |
| `Booking Details Page` |
| Cancel Booking Button | Be able to confirm if I want to cancel booking | Clicked | Able to confirm if I want to cancel booking | Pass |
| Update Booking Button | Be able to update booking | Clicked | Able to update booking | Pass |
| `Update Booking` |
| Update Booking Form | Be able to update booking | Entered valid form | Able to update booking | Pass |
| `Cancel Booking` |
| Cancel Booking | Booking is canceled | Clicked confirm button | Booking was canceled | Pass |
| `Cancel Other User Booking` |
| Enter other user cancel booking url | Redirected to the 404 page | Enter url | Redirected to the 404 page | Pass |
| `Update Other User Booking` |
| Enter other user update booking url | Redirected to 404 the page | Enter url | Redirected to hte 404 page | Pass |
| `Footer` |
| Facebook Link | Redirected to Facebook page | Clicked | Redirected to Facebook page | Pass |
| Twitter Link | Redirected to Twitter page | Clicked | Redirected to Twitter page | Pass |
| Instagram Link | Redirected to Instagram page | Clicked | Redirected to Instagram page | Pass |
| YouTube Link | Redirected to YouTube page | Clicked | Redirected to YouTube page | Pass |

## Bugs

## Technologies Used
CSS, Django, HTML, JS, Python
ElephantSQL Database

Deployment
To deploy the project to Heroku, I followed these steps:
#### **Creating Heroku App:**
+ Logged into Heroku.
+ Selected 'Create New App' from the dashboard.
+ Chose a unique app name.
+ Selected region based on the location.
+ Clicked 'Create App'.

#### **Connecting to GitHub:**
+ From the Heroku dashboard, navigated to the 'Deploy' tab.
+ Under 'Deployment Method', chose 'GitHub'.
+ Searched and selected the repository by name.
+ Clicked 'Connect'.

#### **Setting Environment Variables:**
+ Went to the 'Settings' tab.
+ Located 'Config Vars' and clicked 'Reveal Config Vars'.
+ Added the necessary variables.

#### **Manual Deployment:**
+ Went back to the 'Deploy' tab.
+ Located 'Manual deploy' at the bottom of the page.
+ Clicked 'Deploy Branch' and waited for the build to finish.

#### **Accessing the App:**
+ After the deployment was successful, I found and clicked 'Open app' at the top of the app dashboard.

These steps ensured that the project was successfully deployed to Heroku.
The live link can be found here - [Samburger Website](https://project-portfolio-4-sam-335106eed664.herokuapp.com)

Credits

# Credits
## Code Used/Inspired
 * [CreateView](https://www.geeksforgeeks.org/createview-class-based-views-django/?ref=lbp)
 * [ListView](https://www.geeksforgeeks.org/listview-class-based-views-django/)
 * [UpdateView](https://www.geeksforgeeks.org/updateview-class-based-views-django/)
 * [DeleteView](https://www.geeksforgeeks.org/deleteview-class-based-views-django/)
 * [404 & 500 pages](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page)
 * [Avoid past booking dates](https://stackoverflow.com/questions/70671189/avoid-booking-past-dates-with-django)
 * [Unique Together](https://docs.djangoproject.com/en/4.2/ref/models/options/)
 * [Avoid past booking dates](https://stackoverflow.com/questions/70671189/avoid-booking-past-dates-with-django)

## Media
* Landing Page image from [Pexels](https://images.pexels.com/photos/1199960/pexels-photo-1199960.jpeg)
* Booking Page image from [Pexels](https://images.pexels.com/photos/1484516/pexels-photo-1484516.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)
* [Favicon](https://www.flaticon.com/free-icon/hamburger_106277)
* [Favicon Generator](https://realfavicongenerator.net)
Persona generated by chatgpt

