# Welcome to RecipMe

## Introduction

Are you tired of looking through recipe books, sifting through notes, scrolling through blog posts or bookmarks trying to find the recipe that you know you have somewhere? 

Welcome to RecipMe, a place where you can easily store, retrieve and edit your favourite recipes all in one place.  This website is for anyone who loves to cook but doesn’t love wasting valuable cooking time searching for their favourite recipes. 

![Screenshot 2023-12-07 at 11 04 34](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/e891dd76-414b-40aa-89f0-7e343ef8a5fa)


[Link to RecipMe website](https://recip-me-deee77afa86d.herokuapp.com/)

## Why choose RecipMe? 

From the latest trends to secret family recipes, the simple interface and navigation within RecipMe enables you to not only input your recipes but to edit, tweak or customise them with ease.  Our search functionality ensures these are all easily accessible. 

Browse through our own recipes for inspiration and add them to your collection.

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

I used [coolors.co] (https://coolors.co/palette/253439-ff5757-545454-ffbd59-f5f4f3) to generate my colour palette:

![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/027c781a-346b-4ed8-93ed-9a42815c0f0f)

I aimed for a clean and simple website design that keeps the focus on the content. Opting for a vibrant colour scheme, I wanted to strike a balance between minimalism and boldness. The light off-white background (#f5f4f3) keeps things simple and clean, while introducing splashes of colour add a touch of visual interest that contrasts against the neutral backdrop. This combination creates a modern look without being too over the top.

Coral and yellow form a complementary pairing, and their warmth complemented by cool grey tones, ensures a visually cohesive and balanced palette.  The neutral colours help maintain an overall sense of harmony.

The result is a carefully chosen color palette that enhances the design without overwhelming it, adding sophistication and vibrancy.

### Branding

![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ea618f02-99f6-4947-a764-8ffe40bb4155)

### Typography

I created a logo on Canva using Josefin Sans, and used this for the headers and titles in my website for continuity of design.  While Josefin Sans has a geometric feel I paired this with Lato for a modern, clean appearance.  This pairing ensures readability, making text clear and easy to read. The fonts are versatile, suitable for various contexts like web and print designs. Despite their unique characteristics, they maintain consistency in proportions and weights, contributing to a cohesive and professional look. The combination strikes a balance, creating an aesthetically pleasing design that blends the vintage charm of Josefin Sans with the clean modernity of Lato.



## RecipMe

### Homepage

![Screenshot 2023-12-08 at 12 03 20](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/7abfbfb0-59bd-4442-b208-c1ee634a79dd)


### Sign In

![Screenshot 2023-12-08 at 12 09 17](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ffcb1ee2-5192-4d04-8a76-0dd7d61798ea)


### Add / Edit Pages

![Screenshot 2023-12-08 at 12 20 19](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/62545a43-e46b-41b8-95e3-9edece069e07)


### RecipMe, Favourites

![Screenshot 2023-12-08 at 12 30 57](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/af2e5cb7-a489-4239-96bb-fbb5e76963b4)


![Screenshot 2023-12-08 at 12 35 16](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6fdb2dd1-56c0-4c7f-9388-f22b00e5368b)


###  Personalised Home Page 

![Screenshot 2023-12-08 at 12 40 17](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/2049f4cc-a85e-4ed7-9010-0197f17aac23)


### Full Recipe Page

![Screenshot 2023-12-08 at 12 46 15](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/9e79d26c-09d0-43ac-96e4-cc291166ec50)




### Future Features
Future features not implemented at this time include:
- The ability on the full recipe page to toggle on/off dark mode and prevent your screen turning off, a feature I feel would be very useful when following a recipe
- Recipe sharing - To be able to share recipes with other users of the site or to email them to others
- Upload recipes to main site - The ability to request admin approval for a recipe to be added to the site wide collection
- Notes - the ability for a user to leave notes on their recipes outlining any tweaks they may have made


## Testing

Results of manual testing:
[Testing](testing.md)

## Responsiveness
This website has been tested and is fully responsive on Desktop, Mac book, Ipad and mobile devices.

                                      

## Browser Compatibility

The website has been tested and is being displayed as expected on Safari, Google Chrome and Firefox as well as on android and apple devices.

| Screenshots                                                                                                                                      | Ipad and Iphone SE                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![53d76d73-ebe8-46ee-9860-8137adc34f04](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/18cdc571-d3ce-4f13-972f-9b7e98cd6936) | ![ipad](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6124121e-03e9-4085-9200-746d3aa4812c)     |
| ![IMG_0144](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/62afc582-cedd-4e03-802c-9afeeb5f1c8d)                             | ![IMG_0143](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ae16c7b3-08dc-4077-8fe7-b314cd527072) |

## Bugs
- On the edit recipe page there is no success message appearing.  It does reload the page if successful and return to the top of page
- The only feature not currently working is the 'forgot your password' link, email authentication was out of scope for this project.


## Technologies Used
- CSS
- Django
- HTML
- Bootstrap
- Python
- ElephantSQL Postgres Database
- Cloudinary - All user submitted recipe photos are uploaded to cloudinary

- GitPod development environment used
- GitHub used for version control and code hosting
- GitHub Projects used for Agile Methodology

## Deployment
- I followed the following screenshot to deploy my project to Heroku:

![image (2)](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/26d212cb-0a51-4bb3-8485-d2fb189eebdc)


# Credits

- The Structure of my website was based around this tutorial with Dee Mc:
https://youtu.be/JzDBCZTgVyw?si=w3BBwJswUjBTm1xw 
- This tutorial was used to assist in the creation of my favourite button:
https://www.youtube.com/watch?v=H4QPHLmsZMU
- ChatGPT was used for troubleshooting, bug fixing and content generating.  Also used to create my persona.
- Thanks to Stacey Robson for the Heroku deployment guide
- Thanks to the other members of the Bootcamp for their technical and moral support
- Recipes used were from the bbc good food website
- Hero on image home page retrieved ella-olsson-KPDbRyFOTnE-unsplash.jpg https://images.unsplash.com
- Fontawesome was used for icons
- Google fonts was used
- Wireframes created in Balsamiq
- Logo and flow chart created in Canva
 



