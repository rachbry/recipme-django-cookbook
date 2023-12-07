### Validation Testing

**HTML and CSS**

I used the W3.org validator on my HTML and CSS files.  Please see results below:

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

| Potential                                                                                                                                                        | Image                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| I did receive this error when adding the urls for the logged in pages. I copied the source code from the developer tools and pasted in to get the above results. | ![Screenshot 2023-12-07 at 19 29 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/f8ab92ac-08a3-43b5-99b9-15dd3c88d036) |


**CSS**

| File     | URL                                                                                                                                 | Screenshot                                                                                                                                    | Notes                                                       |
|----------|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| Base.css | https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Frecip-me-deee77afa86d.herokuapp.com%2Frecipes%2Fedit%2F39%2F#textarea | ![Screenshot 2023-12-07 at 19 43 33](https://github.com/rachbry/recipme-django-cookbook/assets/73660517/80bfed4a-a1a8-4b82-9772-a79c5fe5f96c) | Document checking completed. No errors or warnings to show. |

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
