---
title: "Sample test post by tester"
author: Divya28237
categories: Public
classification: Public
tags: [opinion,about,faq,standards,technology,getting-started,accessibility,agile,myths,trending,tutorials,mobile,ai,api,privacy,uxui,web,quality-assurance,architecture,case-study,security,cloud,source-code,data-hub]
date: 2024-11-13 04:54:00 
likes: 0
---

There are two types of tags in the DevPortal site.

Pre-defined tags

Pre-defined tags

These tags need to be specified in the tags.yml file. For example, a tag named ‘accessibility’ has been defined in this yml file shown as below.

      accessibility:
        name: Accessibility
        css-class: tag-red 
There needs to be a corresponding md file in the _tag folder.

  ---
  layout: tag
  tag: accesssiblity
  permalink: "tag/accessibility"       
  ---         
 * Clicking on these tags will redirect you to the page that lists all the tagged post.
