---
title: "How to use Postman to connect to our APIs"
slug: "how-to-use-postman-to-connect-to-our-apis-e4b947"
author: andrew
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:42:15 
updatedBy: andrew
updated: 2025-09-14 23:28:42 
likes: 0
---

**What is Postman?**

Postman is a powerful and user-friendly tool that takes a lot of the complexity out of testing APIs.

It is an API platform for developers to design build, test and collaborate on APIs (Application Programming Interfaces).

**Why use Postman?**

We can use Postman to quickly test APIs via a graphical user interface rather than having to write code or use the command line.

**Installing Postman**

Install Postman after downloading it from [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

**Quick start**

Let's quickly setup and use Postman to test a DevPortal provided API.

1. Open Postman
2. Click the New button that is next to the column My Workspace  ![postman_new.png](https://sadevportal3.blob.core.windows.net/root/postman_new.png)
4. Choose HTTP from the list of available options
![postman_choose_http.png](https://sadevportal3.blob.core.windows.net/root/postman_choose_http.png)
6. You will then see that GET is current HTTP option selected. For this first operation we will use a GET call. Other HTTP types include POST, PUT and DELETE.
7. Set the URL to https://dp-mockaco.azurewebsites.net/BOOK/staff-api/schools/434972/staffpersonals
This is for the API call /staff-api/schools/{zoneId}/staffpersonals within the category Booking System.
8. Within the Header tab add a value name x-api-key with the value from your "My Applications" value. ![postman_choose_http.png](https://sadevportal3.blob.core.windows.net/root/postman_set_header.png)
10. Next click Execute to send the request you have constructed to the server and after some seconds you should see some JSON returned from the server as a response as per the following image.
 ![postman_choose_http.png](https://sadevportal3.blob.core.windows.net/root/postman_200_response.png)