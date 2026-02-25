---
title: "How to add a new author in a Jekyll site?"
author: jeny-amatya-qed
categories: public
tags: [technology]
date: 2023-03-06 23:00:00
updatedBy: jeny-amatya-qed
updated: 2023-06-13 04:46:38
likes: 0
publishedOn: 2023-06-13 04:46:38
---

To add author information to a Jekyll site, you can create a data file that contains author information and then reference that data in the front matter of each post.

Here are the steps to add author information to a Jekyll site:

1. Create a *\_data* directory in your site's root directory if it doesn't already exist.
2. Inside the *\_data* directory, create a new YAML file named *authors.yml*.
3. In *authors.yml*, add the information for each author. For example:

    ```yaml
    johndoe:
    name: John Doe
    email: john@doe.com
    bio: Software developer and blogger
    janedoe:
    name: Jane Doe
    email: jane@doe.com
    bio: Writer and editor
    Billy Rick:
    name: Billy Rick
    picture: /images/authors/bio-photo-2.jpg
    twitter: "@billyrick"
    links:
        - title: Twitter
        url: https://twitter.com/billyrick
        icon: fab fa-twitter-square
    Cornelius Fiddlebone:
    name: Cornelius Fiddlebone
    picture: /images/authors/bio-photo.jpg
    twitter: corneliusfiddlebone
    ```

    In this example, four authors, John Doe, Jane Doe, Billy Rick and Cornelius Fiddlebone, have been added to the file along with their name, email, bio, profile picture and links to their social media accounts.
4. Save the changes to authors.yml.
5. Open a post that should have author information and add the author's identifier to the post's front matter. For example:

    ```yaml
    ---
    layout: post
    title: "My Post Title"
    author: johndoe
    ---
    ```

In this example, the post has been assigned to the "johndoe" author.

6. Save the changes to the post's front matter.
7. Finally, you can display the author information on each post by updating the post's layout file to include the author information. For example, you can add the following code to the bottom of your post's layout file:

```html
<p>Written by {{ site.data.authors[page.author].name }}</p>
<p>{{ site.data.authors[page.author].bio }}</p>
<p>Email: <a href="mailto:{{ site.data.authors[page.author].email }}">{{ site.data.authors[page.author].email }}</a></p>
```

This code will display the author's name, bio, and email address on each post.

In summary, to add author information to a Jekyll site, you need to create a data file that contains author information, reference that data in the front matter of each post, and update the post's layout file to display the author information.