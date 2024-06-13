---
title: How to add a tag in DevPortal
author: jeny-amatya-qed
categories: [Public]
tags: [getting started]
date: 2023-05-15 05:32:50 
updatedBy: jeny-amatya-qed
updated: 2024-06-13 00:41:23 
likes: 1
---

There are two types of tags in the Developer Portal site.

* Pre-defined tags
* User defined tags

1.  **Pre-defined tags**
    * These tags need to be specified in the tags.yml file. For example, a tag named 'accessibility' has been defined in this yml file shown as below.

        ```
            accessibility:
              name: Accessibility
              css-class: tag-red 
        ```
    * There needs to be a corresponding md file in the \_tag folder.

        ```
        ---
        layout: tag
        tag: accesssiblity
        permalink: "tag/accessibility"       
        ---         
        ```
        * Clicking on these tags will redirect you to the page that lists all the tagged post.
        
2. **User defined tags**
    * You can add one or multiple tags when creating a new post via inline editor. The multiple tags need to be separated by a comma.
    * Clicking on these tags will redirect you to the Tags Archive page that lists all the tagged posts, grouped by tag.