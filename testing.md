# Validation Testing

## HTML and CSS

I used the W3.org validator on my HTML and CSS files.  Please see results below:


### HTML

| File                           | URL                                                                                                                                            | Screenshot                                                                                                                                    | Notes                                                                                             |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Homepage (not logged in)       | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2F                                           | ![Screenshot 2023-12-07 at 18 52 31](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/048815c1-1ef8-42da-92ee-175959a77282) | Document checking completed. No errors or warnings to show.                                       |
| Register                       | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Faccounts%2Fsignup%2F#l93c293               | ![Screenshot 2023-12-07 at 18 56 09](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/b60f5593-5cd8-4304-93f2-c0bb36ee66f0) | Error within AllAuth                                                                              |
| Login                          | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Faccounts%2Flogin%2F#l93c293                | ![Screenshot 2023-12-07 at 18 59 30](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/11f92942-f26f-40fa-bced-ab5afd6af881) | Document checking completed. No errors or warnings to show.                                       |
| Recipes (not logged in)        | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Frecipes%2F                       | ![Screenshot 2023-12-07 at 18 54 09](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/d8a3b516-a6e2-43ef-a09f-422862b9d6c9) | Document checking completed. No errors or warnings to show                                        |
| Search Results (not logged in) | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fsearch%2F%3Fq%3DPancakes#l93c293 | ![Screenshot 2023-12-07 at 19 05 50](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/dd1cb632-6f77-468d-a233-3d71433e7b85) | Error showing related to unclosed element - unsure how to fix as content is dynamically generated |
| Full Recipe Page               | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Frecipes%2F30%2F#l93c293          | ![Screenshot 2023-12-07 at 19 12 12](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/e8527226-ae3b-4699-9e5d-50f4a59fcf26) | Error showing related to unclosed element - unsure how to fix as content is dynamically generated |
| Logged in home page            | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fmy_recipes%2F#textarea           | ![Screenshot 2023-12-07 at 19 17 56](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/5bd9c27f-5ae9-4513-9913-ab2344a5c7fb) | Error showing related to unclosed element - unsure how to fix as content is dynamically generated |
| Add Recipe                     | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fadd_recipe%2F#textarea           | ![Screenshot 2023-12-07 at 19 25 49](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/fe8d7257-ca9d-43a4-932e-a4172d5c7bec) | Document checking completed. No errors or warnings to show.                                       |
| Edit Recipe                    | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea            | ![Screenshot 2023-12-07 at 19 34 04](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/4ad1af3d-caf2-4d62-8e86-f3ee492bb058) | Document checking completed. No errors or warnings to show.                                       |
| Delete Recipe                  | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea            | ![Screenshot 2023-12-07 at 19 36 41](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/de6e03b8-db6f-425f-b47b-993905a8450b) | Document checking completed. No errors or warnings to show.                                       |
| Log out                        | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea            | ![Screenshot 2023-12-07 at 19 38 24](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/700ea94f-63b1-431d-bcbe-66666a8a50f9) | Document checking completed. No errors or warnings to show.                                       |

| Issue                                                                                                                                                        | Image                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| I did receive this error when adding the urls for the logged in pages. I copied the source code from the developer tools and pasted in to get the above results. | ![Screenshot 2023-12-07 at 19 29 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/f8ab92ac-08a3-43b5-99b9-15dd3c88d036) |



### CSS

| File     | URL                                                                                                                                 | Screenshot                                                                                                                                    | Notes                                                       |
|----------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Base.css | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea | ![Screenshot 2023-12-07 at 19 43 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/80bfed4a-a1a8-4b82-9772-a79c5fe5f96c) | Document checking completed. No errors or warnings to show. |


### PYTHON

I used the CI Python Linter https://pep8ci.herokuapp.com/# on all my .py files. Please see results below.

| File                   | Screenshot                                                                                                                                    |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| my_project urls.py     | ![Screenshot 2023-12-07 at 18 19 56](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/765148bc-e8ad-4659-9c85-0d61a5508012) |
| my_project settings.py | ![Screenshot 2023-12-07 at 18 26 08](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/a31948da-dec9-472c-ad27-b757460da4ec) |
| home urls.py           | ![Screenshot 2023-12-07 at 18 15 51](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/f49faa61-b794-40cd-8e3d-cc2fb1ccbf65) |
| home views.py          | ![Screenshot 2023-12-07 at 18 04 27](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/1e5b9425-e441-4fc5-bd9d-afc0d005e81a) |
| Recipes admin.py       | ![Screenshot 2023-12-07 at 18 12 48](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ef6e7e04-9cab-422f-be0a-96299043c171) |
| Recipes forms.py       | ![Screenshot 2023-12-07 at 18 05 43](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/a1806f45-df34-42f2-b8ec-7727aa0d7d4e) |
| Recipes models.py      | ![Screenshot 2023-12-07 at 18 02 20](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/ea779dea-51dc-4603-9dd6-8b37cb07907b) |
| Recipes urls.py        | ![Screenshot 2023-12-07 at 18 01 26](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/7df29fff-2cf3-4129-b52a-a7b5670677b4) |
| Recipes views.py       | ![Screenshot 2023-12-07 at 17 59 58](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/52dc1537-b18e-4219-97f4-aa38e1591b36) |
**Lighthouse**


### LIGHTHOUSE

I used Lighthouse to check the quality of all my web pages.  The results for the logged in home page are provided below:

| Desktop                                                                                                                                       | Mobile                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![Screenshot 2023-12-07 at 19 59 20](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/6a7d8cf9-b181-494a-a7c1-4373a9284876) | ![Screenshot 2023-12-07 at 20 03 49](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/da30f0b4-ed88-4a2a-bf9e-fb33dace8cfe) |





### Manual Testing


#### Non-logged in User

| Page         | Action                      | Expected outcome                                            | Testing Performance               | Pass/Fail   |
|--------------|-----------------------------|-------------------------------------------------------------|-----------------------------------|-------------|
| Logo         | Link to home page           | general home for non logged in                              | clicked it when logged in and not | Pass        |
| Home Page    | Click sign up button        | Link to sign up page                                        | Click it                          | Pass        |
| Sign Up Page | Register as user            | If details pass form validation account created             | Created user                      | Pass        |
| Recipes      | Cannot access user recipes  | Only view admin recipes                                     | navigate to page                  | pass        |
| Full Recipe  | Read only access            | Redirected to 403 page                                      | click on edit or delete           | pass        |
| Full Recipe  | Cannot select favourite     | Redirect to sign up                                         | click on favourite                | pass        |
| Search bar   | Cannot view user recipes    | Only searches admin recipes                                 | submit searches                   | pass        |






#### Logged in User

| Page                 | Action                            | Expected outcome                                                            | Testing Performance                          | Pass/Fail                          |
|----------------------|-----------------------------------|-----------------------------------------------------------------------------|----------------------------------------------|------------------------------------|
| Logo                 | Link to home page                 | Link to personalised home otherwise                                         | clicked it when logged in and not            | Pass                               |
| Log in               | Click sign up button              | If details entered correctly, log in (if incorrect warning message)         | Complete form                                | Pass                               |
| forgot password link | click link                        | redirects to enter email page                                               | redirects to enter email page                | Page styled but link does not work |
| Recipes              | Cannot access other user recipes  | Only view admin recipes                                                     | navigate to page                             | pass                               |
| Full Recipe          | Delete own recipe                 | Redirect to confirmation page, then delete recipe                           | click on delete                              | pass                               |
| Full Recipe          | Edit own recipe                   | Edit completed, redirect to top of page                                     | click on edit                                | pass                               |
| Full Recipe          | Delete admin recipe               | Redirect to 403 page                                                        | click on delete                              | pass                               |
| Full Recipe          | Edit Admin recipe                 | Redirect to 403 page                                                        | click on edit                                | pass                               |
| Full recipe          | favourite button                  | Added to favourite page, star icon appears on image in recipe pages         | click button, check pages                    | pass                               |
| Full recipe          | unfavourite recipe                | Icon changed on full recipe page, removed from favourites and icon removed  | click button, check pages                    | pass                               |
| My recipes           | click for favourites              | Should include all owns admin recipes favourited                            | navigate to link                             | pass                               |
| Recipe cards         | Navigate to full recipe page      | From all menus clicking on card will bring full details                     | click in my recipes, recipMes and favourites | pass                               |
| Search bar           | Search own and admin recipes      | Populate search results from admin and users own recipes                    | submit searches                              | pass                               |
| Add Recipe           | Update database                   | Providing all information is correct, recipe added to database              | added recipe                                 | pass                               |
| Log out              | Log out of site                   | Redirect to confirmation page, then log out                                 | click on it                                  | pass                               |
| Footer               | Click links                       | Social media links all active, click on Rachbry lead to my github           | click them                                   | pass                               |
