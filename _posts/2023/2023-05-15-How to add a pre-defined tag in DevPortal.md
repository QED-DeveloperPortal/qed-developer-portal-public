---
title: How to add a tag in Developer Portal
author: jeny-amatya-qed
categories: [Public]
classification: Official (Everyone)
tags: [getting-started]
date: 2023-05-15 05:32:50 
updatedBy: jeny-amatya-qed
updated: 2024-06-13 01:56:52 
likes: 1
---

There are two types of tags in the Developer Portal.

* Pre-defined tags
* User-defined tags

1. **Pre-defined tags**
    * These tags need to be specified in the `tags.yml` file. For example, a tag named 'accessibility' is defined in this yml file as shown below:

        ```yml
        accessibility:
          name: Accessibility
          css-class: tag-red 
        ```
    * Clicking on the tag will take you to a page displaying all posts with that specific tag.
    * The following list shows the pre-defined tags as of now:
        * accessibility
        * api
        * architecture
        * cloud
        * getting-started
        * mobiles
        * security
        * technology
        * uxui
        

2. **User-defined tags**
    * You can add one or multiple tags when adding or updating content in the Developer Portal using either the inline editor or by updating the file in the GitHub repository. Multiple tags need to be separated by commas.
    * You can view the available tags on the [Tags](https://developer.qed.qld.gov.au/tags) page.
    
