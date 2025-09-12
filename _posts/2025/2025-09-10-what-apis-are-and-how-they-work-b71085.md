---
title: "What are APIs and how they work"
slug: "what-apis-are-and-how-they-work-b71085"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:15:08 
updatedBy: jeny-amatya-qed
updated: 2025-09-12 02:38:06 
likes: 0
---

### Overview
This post is the perfect place to start if you are new to APIs. 

---

### What is an API?
An **API** (Application Programming Interface) is a **standard way for two software systems to communicate with each other**. You can think of it as a bridge between your application and another system.
It allows one software system to request information or trigger an action in another application in a safe, consistent and controlled manner.

In simpler terms, an API acts as a **messenger**:  
- It receives a request from your application  
- Passes that request to the appropriate system  
- Returns the response back to your application  

![API workflow](https://sadevportal3.blob.core.windows.net/root/post/what-is-an-api.jpg)

For example:
- A mobile weather app sends our location to an API and request the local weather forecast, which is returned back to our phones.
- APIs are like waiters in a restaurant; they take our order (or request), communicate it to the kitchen (the system providing the service) and finally, deliver the food (or response from the system) back to our table. 

 ![Restarant analogy](https://sadevportal3.blob.core.windows.net/root/post/api-analogy-1.jpg)

---
### A Department of Education analogy
- **School office reception (Staff directory)**
The staff API is like the school reception desk. Your app can ask *"Who are the teachers in Year 4?"* and receive the just the relevant staff details, and not every HR record.

- **Class attendance roll (Attendance API )**
An attendance API records student presence or absence and shares it with other authorised systems like QParents.

---
### How APIs work - The basics
The process can be summarised in three steps:
1. **Send a request**
Your application sends a request to the API specifying the data or action required. For example, "Give me a list of staff at school Brisbane State High School".

2. **Process the request**
The API validates your request (using your application key), then retrieves the relevant data or performs the requested action.

3. **Receive a response**
The API returns the result in a standard format (typically JSON) that your application can use.

---
### Why you should care
APIs make it easy to
- access up-to-date, accurate data
- save time - no manual data entry
- build apps and dashboards that update automatically

---
### Next Step
- [Learn how to authenticate using your application key](/public/setting-up-and-managing-your-application-key-57837c/)
- [See code examples for Node.js, Python, C# and curl](/public/code-examples-of-connecting-your-app-661a99/)
- Test your first call in our API sandbox - a safe place to experiment