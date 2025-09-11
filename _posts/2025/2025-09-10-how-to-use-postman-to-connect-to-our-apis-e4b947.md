---
title: "How to use Postman to connect to our APIs"
slug: "how-to-use-postman-to-connect-to-our-apis-e4b947"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:42:15 
updatedBy: andrew
updated: 2025-09-11 09:25:03 
likes: 0
---

**What is Postman?**


**Why use Postman?**


**Installing Postman**

Postman can be downloaded from [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

**Quick start**

Let's quickly get setup in Postman to test a DevPortal provided API.

1. Open Postman
2. Click the New button that is next to the column My Workspace 
3. Choose HTTP from the list of available options
4. You will then see that GET is current HTTP option selected. For this first operation we will use a GET call.
5. Set the URL to https://dp-mockaco.azurewebsites.net/BOOK/staff-api/schools/434972/staffpersonals
This is for the API call /staff-api/schools/{zoneId}/staffpersonals within the category Booking System.
6. Within the Header tab add a value name x-api-key with the value from your "My Applications" value.
7. Next click Execute to send the request you have constructed to the server and after some seconds you should see some JSON returned from the server as a response.



