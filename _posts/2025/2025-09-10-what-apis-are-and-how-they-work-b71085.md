---
title: "API basics: What they are and how they work"
slug: "what-apis-are-and-how-they-work-b71085"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:15:08 
updatedBy: Joyclyn
updated: 2025-09-15 04:50:27 
likes: 0
---

### What is an API?
An **API** (Application Programming Interface) is a **standard way for two software systems to communicate with each other** in a safe, consistent and controlled manner. You can think of it as a bridge between your application and another system, or like a waiter in a restaurant.

The waiter takes your order (or request), communicates it to the kitchen (the system providing the service) and finally, delivers the food (or response from the system) back to your table. 

 ![Restaurant analogy](https://sadevportal3.blob.core.windows.net/root/post/API-kitchen-analogy.png)

An API acts as a **messenger** that:  
- receives a request from your application
- passes that request to the appropriate system  
- returns the response back to your application.  

![API workflow](https://sadevportal3.blob.core.windows.net/root/post/what-is-an-api.png)

### How do APIs work?
The process can be summarised in three steps:
1. **Send a request**
Your application sends a request to a specific API requesting the data or action required. 

2. **Process the request**
The API validates your request (using your application key), then retrieves the relevant data or performs the requested action.

3. **Receive the response**
The API returns the result in a standard format (typically JSON) that your application can use.

---
### Examples
**Mobile weather app**
1. Send a request: To `local weather API`: Give me the local weather forecast for [location].
2. Process the request: The `local weather API` validates the request and sends back the requested data.
3. Receive the response: The mobile weather app receives the data from `local weather API` and displays the data for the user.

**Class attendance roll**
1. Send a request: To `attendance API`: Give me a list of all the students who are present in year 4 today.
2. Process the request: The `attendance API` validates the request and sends back the requested data.
3. Receive the response: Your app receives data from the `attendance API` which lists all the students in year 4 who are present today.

---
### Why use APIs?
APIs make it easy to:
- access up-to-date, accurate data
- save time because there's no manual data entry needed
- build apps and dashboards that update automatically.

---
### Next steps
- [Learn how to authenticate using your application key](/public/setting-up-and-managing-your-application-key-57837c/)
- [See code examples for Node.js, Python, C# and curl](/public/code-examples-of-connecting-your-app-661a99/)
- Test your first call in our API sandbox - a safe place to experiment