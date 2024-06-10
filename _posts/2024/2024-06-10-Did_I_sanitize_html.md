---
title: "Another Did I sanitize html "
author: "jeny-amatya-qed"
categories: [public]
tags: [auto-import, test,validate,sanitize]
date: 2024-06-10 11:57:34
likes: 0
imported: True 
import-source: "GitHub"
import-reference: "3333"
---

# Remove harmful tags from the content
 
Validation Service uses HTML Santizer which has been configured to remove the following harmful tags
 
- script
- iframe
- object
- embed

It can be further configured to

- allow specific tags and attributes and ignore the rest
- allow specific url schemes (http, https, mailto, tel) and ignore rest
- remove attributes that might be dangerous such as onclick, prevent inline js in links
- to custom handle specific tags etc.

The content includes a bunch of html code including script and iframe tags, which should be removed in the sanitized markdown file.  **Be careful of these tags!** 
   
*can you see these tags?*