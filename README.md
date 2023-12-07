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

Colour Pallete:

![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/027c781a-346b-4ed8-93ed-9a42815c0f0f)

Logo:
![image](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ea618f02-99f6-4947-a764-8ffe40bb4155)

Credits
Persona generated by chatgpt

