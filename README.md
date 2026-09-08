# Professional Portfolio
Cameron Wheatley's professional portfolio


# Table of Contents
* [Introduction](#introduction)
    * [Overview](#overview)
    * [Target Audience](#target-audience)
* [Planning](#planning)
    * [User Stories](#user-stories)
    * [Design](#design)
        * [Colour Pallette](#colour-pallette)
        * [Typography](#typography)
    * [Wireframes](#wireframes)
        * [Desktop](#desktop)
        * [Mobile](#mobile)
    * [Database](#database)
* [Development](#development)
    * [Agile](#agile)
    * [Features](#features)
    * [Testing](#testing)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries & Frameworks](#libraries--frameworks)
    * [Hosting](#hosting)
    * [Other technologies](#other-technologies)
* [Credits](#credits)
    * [Media](#media)
    * [Content](#content)
    * [Acknowledgements](#acknowledgements)


# Introduction

Hi there, my name is Cameron, and I'd like to welcome you to my professional portfolio.

Here you will find all the relevent documentation regarding my portfolio, the planning, the testing and everything in between!

Feel free to look around, this is an open book and I am more than happy to answer any questions regarding steps taken when creating this project.

Have fun!

## Overview

As I am writing this I am still in the very early stages of planning what is to be my professional portfolio, and as I strive to become a better developer, I'm holding myself to some of the best development practises I have learnt - one of them being thorough and true documentation.

From where I am currently standing, my portfolio will be the hub listing all of my projects and websites, from small problem-solving apps I have built for my own personal gain, to collaborative projects I contributed to whilst participating in Code Institute Hackathons. I want this portfolio to be a representation of me - solid, clear with a purpose, yet still plenty of room to grow in size!

One of the biggest problems I face as a developer is the excitement I experience when snowballing ideas - now that may sound great to some developers, but to me, not so much. I often forget to walk before I can run, my ideas run me wild and before I know it I am brainstorming ideas which no longer relate to the initial project at hand.

So, all I am asking is that you stick with me here, and hopefully this readme is sewing the seeds for an excellent portfolio which will eventually get me hired as a developer!

## Target Audience

I envisage my portfolio having two main categories of audience - potential clients and recruiters, and this is who I am tailoring my portfolio towards.

**Recruiters**

- My main audience will be recruiters and hiring managers - I want my portfolio to speak for me at the bare minimum, my portfolio should echo absolutely everything I stand for in the professional world.

- With this, I want recruiters to easily infer my professional expertise from simply looking at the projects displayed on my portfolio. I expect my backend to be pristine and expertly coded in order to support my frontend application in the most optimal way possible. For example, I want users to have the ability to search for projects with parameters that matter most to them. Here I am referring to searching by language, or library and framework, instead of just the name of the project. This will allow recruiters to easily narrow down the skillset I harbour, and whether I am a perfect fit for their company.

- Furthermore, I want to ensure that my website is secure from any form of manipulation or attacks through ensuring strict permissions throughout. I plan on having a singular admin user, that being me, who can only send POST, PUT and DELETE requests to the backend. In my mind, my portfolio should be a completely static website for everyone but myself.

**Potential Clients**

- The other demographic that I intend on appealing to are the potential clients - although my main focus of my portfolio is to appeal to recruiters and hiring managers, I also see great value in presenting my work to clients who are in need of my services. Besides, potential clients means more high quality websites I can add to my portfolio!

- With this in mind, I plan on harbouring a portfolio which has a very minimalist yet professional look. I believe that less is more — now more than ever, this is true within the development industry. This is something which I have been keeping an eye on in the forefront of my mind whilst drafting up wireframes.

- It's important to me that clients have a call to action, some form of contact form or contact details for myself, where clients can easily get in touch with me if they want to more forward.

# Planning

## User Stories

## Design

### Colour Pallette

- When considering the colour pallet for my portfolio, I wanted to lead with a rich gold colour. After doing plenty of research, I had settled on `#FEE175` as the base colour for the starting pallet, and I had intentions of building upon that. I experimented further with `#FEE175` and I began looking into darker shades and lighter hues of the colour in order to provide me with more depth when utilising the colour.

- I created a brief colour pallet using [Coolors](https://coolors.co) showcasing the different shades and hues I had come across in order to begin experimenting with.

- The colours below are by no means guaranteed to be featured in the portfolio, but it's a starting point which is what I am aiming for at the moment - a basis to build upon.

![An image showing the golden colour pallet](/assets/images/pallets/gold-pallet.png)

- Once I had the gold colour pallet sorted, I began researching a colour which I could easily contrast with it - I want my portfolio to be easily accessbile to all users, so having a defining constrast was very important to me.

- I had stumbled across a short video online which was experimenting matching a multitude of colours together - one of these colour cominations was constrasting `#FEE175` with `#0D151B`. I really liked this combination as the shadows of `#0D151B` superbly brought out all the positives within `#FEE175`. It really made the gold stand out from the background and provided an excellent, professional appeal which I felt would be a perfect fit for my portfolio. 

- I began experimenting with the dark grays, looking into similar hues and shades which I could work with, colours which would provide furher depth and character. My only concern working with a gray as dark as this is that it can be hard to layer, due to how dark it is - I touch up on this further when designing the wireframes.

![An image showing the gray colour pallet](/assets/images/pallets/grey-pallet.png)

### Typography

## Wireframes

### Desktop

- Below are the wireframes that I have created for the desktop views of what I would like the portfolio website to look like.

- When designing the wireframes, I wanted to go into as much detail as possible. This would give me as much edge as possible when it comes to designing the backend - the backend is there to support the frontend, but the backend can only support the frontend if both are perfectly aligned, and I can ensure this through thorough planning.

- As a side note, as discussed earlier within the colour pallettes section, the gray colouring has proven to be rather problematic when adding depth and levels to the project. In order to combat this, I plan on addding box shadows to layered elements in order to provide the illusion of depth to the user. This is visible within all of the screenshots below.

![A screenshot of the homepage desktop wireframe](/assets/images/wireframes/home-page-desktop.png)

- Here is the home page wireframe when viewing the portfolio on a desktop.

- I want the portfolio to harbour a very minimalist yet professional look. In this day and age of website UI, less is more is definitely the case. 

- Within the hero, the user can text which introduces me to them, along with my trade - website development, along with a photo of me. My thoughts here are that if users are able to put a face to the name, then the  website then has a much more personal feel to it, which may very well drive up leads.

- Under this, I have a link to my social media for users to interact with - and underneath where it says 'For The Recruiters' I will have links to my LinkedIn and GitHUb, as this is what I imagine they will be looking for to begin with. 

---

![A screenshot of the projects list desktop wireframe](/assets/images/wireframes/project-list-desktop.png)

- Above is a screenshot of the desktop wireframe of the project list view.

- The user will be able to search for projects within the search bar, here the user can search based on names of the projects, languages and technologies used, along with where or not the project is a collaborative project.

- The projects are laid out professionally, carrying on the theme discussed earlier using the gold and grey colour scheme. The names along with a short snippet and preview of the project will be seen by the user when viewing this page.

- I plan on adding an infinite scroll feature to the project list - but being realistic, I'm not sure when this will become neccessary, as the amount of projects which I have currently is nowhere near the minimum threshold I plan on using for infinite scrolling.

---

![A screenshot of the projects detail wireframe within a desktop view](/assets/images/wireframes/project-detail-desktop.png)

- Above is a screenshot of the project detail wireframe when viewing on a desktop.

- The wireframe continues the professional look which I have been upholding throughout the project so far. A preview of the project is visible on the left hand side of the panel, and when clicking on the image the user will be directed to the live site. To the right of this, the user can find the name and the description of the project. Underneath this, the user has 3 buttons which they can interact with - view site, which will take them to the live site; view repo, which will take them to the GitHub Repository; and 'more...', which will display further information.

- Within the 'more...' window, I plan on including meta data about the project which will be useful to recruiters, for example the languages, libraries and frameworks used when creating the project. This sort of information does not pose any benefit to a standard user, so I see it as futile including it on the initial page for all users to see.

### Mobile

- Below are the wireframes I have created for the mobile element of my portfolio. I have stayed true to the desktop version, as I want there to be clear synergy between the mobile and desktop variants of the application.

![A screenshot of the home page mobile wireframe](/assets/images/wireframes/Home%20Page%20Mobile.png)

- Here I have created the home page mobile wireframe to look as close to the desktop wireframe as possible. As stated earlier, I want there to be synergy between the mobile and desktop versions of the application. By collapsing the navbar into a hamburger icon, I have saved a lot of space in the header of the home page - I want the website to breathe and to not be too crowed for it's own good.

--- 

![A screenshot of the project list mobile wireframe](/assets/images/wireframes/Project%20List%20Mobile.png)

- For the project list mobile wireframe, there really is not much difference between the mobile and desktop views. The mobile view is essentially a collapsed version of the desktop wireframe - the only real difference here is that the project list is more condensed and looks very similar to the desktop. I am very satisfied with the fact there is no real difference between the two.

---

![A screenshot of the project detail mobile wireframe](/assets/images/wireframes/Project%20Detail%20Mobile.png)

- This wireframe is a similar story to the project list wireframe in the sense that it is just a collapsed version of the desktop view. The presentation looks very smart since all of the elements are neatly stacked upon each other and the space is being utilised in the most efficient way.

- I am unsure what to include within the 'more' button located at the bottom of the pannel. If not I will just remove it.

## Database

![A screenshot of the database schema](/assets/images/schema/database-schema.png)

- Above is a screenshot of the database schema which I am planning to follow for the creation of my portfolio. As seen above, I am planning on using 4 different models that will make up the database.

#### Projects

- The largest model is the projects model, and this model will contain the information which relates to the portfolio projects I created whilst studying with the Code Institute. The projects model will be linked to the technologies model, and user will be able to filter projects based on the technologies used.

#### Technologies

- The technologies model will be one of the smaller models within this project and it will serve as a means for filtering projects when users are looking at my portfolio.

#### Certification

- The certification model is the second largest model I plan to create for my portfolio. It will contain 6 different fields with one field being tied to the skills model. The certifications model will also list the completion date of the certificate, the expiry date and the institution and live URL.

#### Skills

- The final model which I have included is the skills model. This model documents the skills which I have learned throughout my journey, and ties them to physical projects for recruiters to see. I do not plan on adding any filter functionality to the skills model as I want to focus solely on creating the portfolio instead of adding countless dynmaic features.

# Development

## Agile

## Features

## Testing

# Technologies Used

- [Coolors](https://coolors.co) used to create the colour pallette.

- [Figma](www.figma.com) used for creating wireframes.

- [LucidChart](https://lucid.co/) used for creating database schemas.

## Languages

## Libraries & Frameworks

## Hosting

## Other Technologies

# Credits

## Media

## Content

## Acknowledgements
