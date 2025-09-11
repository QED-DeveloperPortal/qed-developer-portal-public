---
title: "How to use Postman to connect to our APIs"
slug: "how-to-use-postman-to-connect-to-our-apis-e4b947"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:42:15 
updatedBy: andrew
updated: 2025-09-11 22:37:29 
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
`<img alt="postman_choose_http.png" src="https://sadevportal3.blob.core.windows.net/root/postman_choose_http.png">`
4. Choose HTTP from the list of available options
5. You will then see that GET is current HTTP option selected. For this first operation we will use a GET call.
6. Set the URL to https://dp-mockaco.azurewebsites.net/BOOK/staff-api/schools/434972/staffpersonals
This is for the API call /staff-api/schools/{zoneId}/staffpersonals within the category Booking System.
7. Within the Header tab add a value name x-api-key with the value from your "My Applications" value.
8. Next click Execute to send the request you have constructed to the server and after some seconds you should see some JSON returned from the server as a response.