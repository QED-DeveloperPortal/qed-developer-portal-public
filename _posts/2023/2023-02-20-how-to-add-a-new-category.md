---
title: "How to add a new category in a Jekyll site?"
author: jeny-amatya-qed
categories: [public]
classification: Public
tags: [technology]
date: 2023-05-08 06:10:26
updatedBy: Joyclyn
updated: 2023-05-11 04:15:40
likes: 0
---

Adding a new category to a Jekyll site involves modifying the site's configuration file and updating the front matter of each post that should be included in the new category.

Here are the steps to add a new category:

1. Open your site's configuration file, ***`_config.yml`***, in a text editor.
2. Add the new category to the defaults section of the configuration file. For example:

```yaml

defaults: 
  - scope:
      path: ""
      type: posts
    values:
      category: blog
   - scope:
      path: ""
      type: posts
    values:
      category: news
```

In this example, two new categories, 'blog' and 'news', have been added to the ***`defaults`*** section.

3. Save the changes to ***`_config.yml`***.
4. Open each post that should be included in the new category and add the category to the post's front matter. For example:

```yaml
---
layout: post
title: "My Post Title"
category: "news"
---
```

In this example, the post has been assigned the 'news' category.

5. Save the changes to each post's front matter.
6. Finally, you can create a new page that displays all posts in the new category by creating a new Markdown file in the ***`_pages`*** directory with the following front matter:

```yaml
---
layout: category
title: <Category Title>
category: <Name of the category>
---
```

In this example, replace Category Title with the title of the new category and ***`categoryname`*** with the name of the new category.

Next, add the following code to the bottom of the new page to display all posts in the new category:
{% raw %}
html {% for post in site.categories[page.category] %} <a href="{{ post.url }}">{{ post.title }}</a> {{ post.excerpt }} {% endfor %}
{% endraw %}