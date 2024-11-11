---
title: "365375 - Issues when author slug doesn't match the moderator's gh account (New post) - Sensitive info - no tag selected"
author: DivyaTestUser
categories: Public
classification: Public
tags: [opinion]
date: 2024-11-11 03:29:05 
likes: 0
---

This ticket is to fix the issues that appear when the user's slug in authors'yml does not match the Github username for the same user. An example of this is an error that is detailed in the Repo Steps above. 

In order to verify this issue. I need to update the authors.yml for your user to meet the above condition for your moderator user. You can then test the following scenarios with that user.
Add/Edit posts
Subscribe/unsubscribe to tag
View pending posts in Profile Summary
View pending posts in Tag page
And also note any other anomalies in the site
These would mostly be covered in regression testing as well.