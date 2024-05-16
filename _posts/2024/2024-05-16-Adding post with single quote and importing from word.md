---
title: Adding post with single quote and importing from word
author: sushma-hazari
categories: [Public]
tags: [test]
date: 2024-05-16 03:31:12 
updatedBy: Sushma Hazari
updated: 2024-05-16 03:41:29 
likes: 0
---

testing single quotes '

Testing the post for single quote

'

6

I am trying to write tests for one of our rich text components which was implemented with slate js editor in react js. So when writing tests, I am retrieveing the element div[contenteditable='true'], but not able to simulate events like change, blur, focus. The handlers attached to editor component are not getting called. I tried multiple combinations, but no luck. Can someone please help on this? Is it possible to simulate events for contenteditable element using testing library (contenteditable is implemented using slatejs)?

Like you've discovered, contenteditable isn't supported by JSDOM. React Testing Library (RTL) is built on top of JSDOM, so it's not possible to test the Slate editor properly with RTL until JSDOM implements support for contenteditable.