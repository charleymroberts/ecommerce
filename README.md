# VeganDirect

Vegan Direct is an online retail shop selling innovative, high-quality vegan food products to individual consumers (B2C) from brands and producers which are not commonly stocked in supermarkets.  

![homepage screenshot on desktop](doc/desktop-homepage-screenshot.png)

![homepage screenshots on mobile](doc/homepage-mobile-screenshots.png)

The deployed site can be accessed on Heroku: [VeganDirect on Heroku](https://vegandirect-2d439acd3be5.herokuapp.com/)

## About VeganDirect

### Purpose and benefits of the business

VeganDirect offers its customers:

**Choice and convenience**

It enables its customers to have access to a wide range of products that is more varied than the usual big brands stocked by the big supermarket chains, all in one place, and delivered to their door. 

**Ethical shopping**

Many of the products are made by small companies or sole traders, who are often vegans themselves, meaning customers are able to spend their money supporting small businesses that share their ethical values. 

**High-quality products**

Because many of the products are produced in small batches and do not have to contain the array of food additives and preservatives required to make a product long-life and durable enough to withstand a centralised supermarket supply chain, they are often of higher quality than typical supermarket products, and some are even of a handcrafted, artisan nature.

**Help achieving lifestyle goals**

People who have decided to become vegan, or are considering becoming vegan, often seek out alternatives to a particular favourite food that they are worried about missing. Vegan Direct enables them to find a wider selection of good-quality vegan food products than in their local supermarket, and locate specific alternatives to a favourite non-vegan food or ingredient, helping them to achieve their goal of maintaining a vegan lifestyle without having to ‘give up’ favourite foods.

### Target audience

VeganDirect's target audience is:

**UK-based…**

The site is based in the United Kingdom and ships solely within this area (as the practicalities of shipping chilled/frozen goods overseas and the complexity and cost of shipping from the UK into the EU since Brexit are now sadly outside the scope of a small business).  

**…individual retail customers…**

VeganDirect is a B2C (business-to-customer) retailer, selling single items directly to private customers, rather than in wholesale quantities to other retailers or caterers.

**…with an interest in vegan food**

This could include:
-	People who are already vegan
-	People who are interested in making the change to become vegan
-	People purchasing food or gifts for vegan friends, family members or colleagues
-	People who purchase ‘free-from’ foods for other reasons, such as food intolerances

## Business and customer goals

In designing any product, we must always bear in mind, who are our end users and what will be useful to them?

This section addresses the first two planes of UX design: Strategy and Scope.

The Strategy plane of UX design tells us that the product we’re designing should be useful, useable and valuable.

The product goals come under the Strategy plane of UX design: what we are aiming to achieve in the first place and for whom?  The features based on these goals are within the Scope plane of UX design: based on the goals of the business, what features should the design include?


The goals of the customer and the retailer are summarised here under the five Epics used in the development of this product.

Some are only relevant to retailers, and some are relevant to both groups.

(Note that the user who is purchasing items from the webshop is referred to throughout this document as the 'customer', although in software development terms, the customer of the software developer would be the retailer.)

### Epic 1: UX/UI

**Retailer**
1. An interface that is intuitive to use and doesn't require busy store owners to spend a long time learning how to use it

**Customer**

2. Easily find their way around an Intuitive interface
3. Enjoy using a visually attractive interface that makes the site feel trustworthy
4. Easy to find the products they want and view information about those products

### Epic 2: User Authentication and Accounts

**Retailer**

1. User has an account for the back end of the application which they can log into to add, edit and delete products from their database
2. Differing levels of permissions for the store owner and for any employees if required
3. User can clearly see who is logged in, or whether or not they are logged in, at any given time

**Customer**

4. User can sign up for an account which they can log in and out of
5. User can input all the details needed for shipping
6. Account should save their shipping details for next time if requested by the user
7. Account could allow for extended features such as loyalty points and favourite products lists
8. User can check out without creating an account
9. User can create an account by signing in with their social media account

### Epic 3: CRUD (create, view, update and delete) functionality

**Retailer**

1. Ability to add new product information
2. Ability to edit and delete existing products

### Epic 4: Basket/Purchasing

**Retailer**

1. Set shipping costs and communicate these to the customer before they make a purchase (especially if there are different rates for chilled products etc).
2. Communicate to the customer that their shipping address needs to be in the UK to make a purchase. 

**Customer**

Ability to:
3. Add products to their shopping basket
4. Provide all the details needed for shipping
5. Submit their order and pay securely

### Epic 5: Marketing

**Retailer**

1. Be able to upsell, by highlighting specific products on the homepage and through a 'products you may also like' section at the bottom of individual product pages
2. Encourage customers to sign up for their social media feeds and email list
3. Encourage return visits through loyalty points and favourites lists

## User Stories

These epics and goals were then broken down into User Stories, which each have 
tasks and acceptance criteria, which were used to guide the development of this
project.  

The User Stories (plus their tasks and acceptance criteria) can be viewed on the 
project's [GitHub Project Board](https://github.com/users/charleymroberts/projects/4/views/1).

The User Stories, including those which did not make it into this iteration of the development cycle,
can also be [viewed on a Google Sheet here](https://docs.google.com/spreadsheets/d/1NterIj0KVUP2ewTUQz0VWNVGJCWMlNIqcNa3cIOfBlU/edit?usp=sharing).

(To avoid duplication, the user stories are written from the perspective of the person 
primarily carrying out the action, which in some cases is the retail customer and 
in some cases is the webshop owner, even though many actions are relevant to both groups.)

## Database design

The database models were planned using an Entity Relationship Diagram:

![entity relationship diagram for VeganDirect](doc/database-er-diagram-vegandirect.png)

**Apps and Models**

| Django App                    | Model |
|-------------------------------|--------------|
| Checkout                      | Order, OrderLineItem |
| Products                      | Product, Category, Brand |
| Profiles (customer accounts)  | ShippingAddress, UserInfo 

The 'User' model is the standard model already provided by Django. The rest are custom models created for this project.

(UserInfo was not yet used by the time of deployment of the MVP - in future this could be used to store customer loyalty points earned with each purchase.)

**More detail about the ERD**

**User** 

The standard user model provided by Django

Relationships to other models:

OneToOne with UserInfo to extend User (UserInfo is currently only used to store loyalty points data,  but could have other information added to it in future)

**ShippingAddress**

Included as its own model so that each user can save multiple shipping addresses (home, work, etc)

Relationships to other models:

Includes ForeignKey (i.e. one to many) of User (one user can have multiple addresses)

**Product**

Information about each individual product

Relationships to other models:

ForeignKey to Brand (one brand can have many products)
ManyToMany between ‘liked’ and User (so that each user can have a list of favourite products)
ManyToMany to Category (each category contains multiple products, and each product can be assigned to multiple categories)

**Brand**

The name of each brand plus an optional description to appear on the webshop

**Category**

Determines where the product appears in the site’s navigation menus.
The name of each category plus an optional description to appear on the webshop
‘Parent’ is used to assign the category as the parent category of a subcategory (e.g. Chilled > Dairy Alternatives > Vegan Cheese – Chilled is the parent category of Dairy Alternatives, which itself is the parent of Vegan Cheese)

**Order**

Information about each order placed by a user, which is saved as an order history (i.e. so if the price of a product changes or the user changes their address, the information in their order history is not altered)

Relationship to other models:

Includes ForeignKey of User (one user can have multiple orders)

**OrderLineItem**

Each item (or multiple quantites of the same item) in a customer’s order

Relationship to other models:

Includes ForeignKey of Product (one product can be included in multiple orders) 
Includes ForeignKey of Order (multiple lines can be in one order)

Database design is related to the Structure plane of UX Design: how we structure and present our information.  Further aspects of Structure are covered below under the user interface design.

## UX/UI design

An excellent user interface design and user experience are particularly crucial for a retail business, as their customers have a choice about where they buy products from and can easily choose to go elsewhere (unlike, say, interacting with the Government or the NHS online where you have no choice but to use whatever interface is presented to you). 

### First of all

**Some guiding principles of retail that were used in the planning of this design:**

- If online customers can’t quickly find what they want, they will navigate away and look elsewhere 

Address by: making sure search, filters and category layout are effective and make it easy to find information

- If you offer customers too much choice, it can get overwhelming and they might not make a purchase 

Address by: Don’t over-clutter things. Online supermarkets tend to be bad for this, especially on home pages.

- There are two main ways to increase sales: increase the number of customers, and increase the amount of items each customer buys per visit 

Incresing the number of customers: consider SEO at all stages. 

Increasing the spend per visit: 
find ways to upsell, such as the 'similar products you might like' section suggesting 
additional products at the bottom of product pages

### Market research

I began my planning by visiting other similar online shops and supermarkets, to
familiarise myself with UI conventions and likely customer expectations.

These included:
- [Holland and Barrett](https://www.hollandandbarrett.com/) (UK-based 'health store' chain)
- [VeganStore.co.uk](https://www.veganstore.co.uk/) (the UK's original vegan online shop)
- [AlternativeStores.co.uk](https://alternativestores.com/) (another well-known vegan online store)
- [Morrisons.com](https://groceries.morrisons.com/webshop/startWebshop.do) and [Sainsburys.co.uk](https://www.sainsburys.co.uk/) for the conventional supermarket experience

Design features that are common across these online food shops/supermarkets include:

Header:
-	Company's name/logo
-	Modern-looking icons in the top right corner for favourites, account, basket etc.
-	Search box (or sometimes this is lower down the page under the banner image)

Homepage:
-	Big colourful banner image on homepage (could be carousel or static)
-	Extra info banner: e.g. saying how much to order for free delivery
-	Lists of products underneath the homepage banner (often too many in my opinion, the customer is unlikely to scroll that far down below the fold. Amazon does it though, so it’s expected.)
Menu bar (on all pages):
- Top level menu items which group products in an obvious way, including ‘new’, ‘sale/clearance’ as well as product categories

Individual product pages:
- Breadcrumb menu trail across the top on some
- Key info at top: usually half a row for product photo and the other half for name/price/add to basket
- Other info below that, sometimes with accordion sections or tabs
(there’s a lot that has to be provided, especially with food products, so it’s a good idea to make it more manageable)

Product list pages:

- Banner across the top displaying the name of the category, or the category name in bold
- Either above or below banner image: dropdown menu for 'sort by' a-z, price low-high
- ‘Filter by’ box on left hand side: e.g. category, brand, price, allergens
- Products displayed in a grid layout contained in the style of Bootstrap Cards or similar, (photo above, text below) between three and five to a row (or up to seven for supermarkets)

Footer:

- Links to delivery information/terms and conditions/privacy policy
- Marketing links: mailing list signup box, social media links. Often using friendly-sounding headings such as: 'Join the community', 'Keep in touch', 'Become part of the family' (rather than 'Sign up to our newsletter'/’Follow us on social media’)

Based on these observations, the next step was to create some wireframes to plan my design.

### Wireframes



