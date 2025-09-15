---
title: "How to use Postman to connect to our APIs"
slug: "how-to-use-postman-to-connect-to-our-apis-e4b947"
author: andrew
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:42:15 
updatedBy: jeny-amatya-qed
updated: 2025-09-15 01:47:13 
likes: 0
---

## What is Postman?  

Postman is a powerful and user-friendly tool that simplifies API testing.  
It provides a **graphical interface** that lets you send requests, view responses, and debug APIs — without needing to write code or use the command line.  

Postman is more than just a testing tool. It’s a full API platform where developers can **design, build, test, and collaborate** on APIs.  


## Why use Postman?  

Using Postman makes it easy to:  

- Quickly test APIs with a simple point-and-click interface  
- Save and organize API requests into collections for reuse  
- Experiment with different parameters, headers, and request types  
- View structured responses (JSON, XML, etc.) instantly  

In short, Postman removes much of the complexity from API testing and speeds up development.  


## Installing Postman  

Download and install Postman from the official website:  

[https://www.postman.com/downloads/](https://www.postman.com/downloads/)  

Choose the version for your operating system (Windows, macOS, Linux) and follow the installation steps.  

## Quick Start: Testing a Developer Portal API  

Let’s walk through setting up and testing a Developer Portal API using Postman:  

1. **Open Postman**  

2. **Create a new request**  
   - Click the **New** button next to the “My Workspace” column.  
   ![postman_new.png](https://sadevportal3.blob.core.windows.net/root/postman_new.png)

3. **Choose HTTP**  
   - Select **HTTP** from the list of available options.  
   ![postman_choose_http.png](https://sadevportal3.blob.core.windows.net/root/postman_choose_http.png)

4. **Set the request type**  
   - You will see that **GET** is selected by default.  
   - For this first request, we’ll use `GET`.  
   - (Other common request types include `POST`, `PUT`, and `DELETE`.)

5. **Enter the request URL**  
   - Set the URL to:  
     ```
     https://dp-mockaco.azurewebsites.net/BOOK/staff-api/schools/434972/staffpersonals
     ```  
   - This calls the `/staff-api/schools/{zoneId}/staffpersonals` endpoint under the **Booking System** category.

6. **Add the API key header**  
   - Go to the **Headers** tab.  
   - Add a new header:  
     - **Key:** `x-api-key`  
     - **Value:** *(your API key from “My Applications” in the DevPortal)*  
   ![postman_set_header.png](https://sadevportal3.blob.core.windows.net/root/postman_set_header.png)

7. **Send the request**  
   - Click **Send** (or **Execute** depending on your version).  
   - After a few seconds, you should see a JSON response from the server.  
   ![postman_200_response.png](https://sadevportal3.blob.core.windows.net/root/postman_200_response.png)


## What’s next?  

Now that you have successfully sent a `GET` request, try experimenting with:  

- **Changing parameters** in the URL (e.g., using a different `zoneId`)  
- **Exploring other HTTP methods** such as `POST` or `PUT` (when available)  
- **Saving your request** into a Postman Collection for reuse later  

> 💡 **Tip:** You can also export and share your Postman collections with your team so everyone can test with the same setup.  

