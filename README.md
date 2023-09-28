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