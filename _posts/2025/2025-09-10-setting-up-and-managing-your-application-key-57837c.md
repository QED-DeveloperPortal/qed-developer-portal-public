---
title: "Setting up and managing your application key"
slug: "setting-up-and-managing-your-application-key-57837c"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:25:29 
likes: 0
---

# Overview 

Application keys are required to securely access our APIs. You must include your key in the request header `X-API-KEY` when making requests from Postman or other API clients.  

This guide walks you through creating, managing, and using application keys.  

---

## Step 1: Sign in to the Developer Portal  🔐

1. Log in to the Developer Portal using your credentials.  
2. Navigate to the **APIs** section from the main navigation menu.  
3. Go to **APIs → My Applications**. 
![](https://sadevportal3.blob.core.windows.net/root/post/1-api-key-page.png)

## Step 2: Create an application key  🆔

1. Click **Create an API Key**.  
2. Enter a descriptive name for your application (e.g., `QTeacher Integration App`).  
3. Copy the generated API key using the copy icon.  

> 💡 **Tip:** You can create multiple application keys to manage access for different environments or teams.  

You will use this API key to authenticate your requests in Postman or any third-party application.  

![Create API key](https://sadevportal3.blob.core.windows.net/root/post/2-api-key-create.png)

---

## Step 3: Delete an application key  🗑

If an application key is no longer required:  

1. Select the key from your list of applications.  
2. Click **Delete** to remove it.  

> 🔒 **Best practice:** Delete unused keys to keep your API access secure.  

---

## Step 4: View API activity 📊 

1. View API usage by clicking on the **Activity** button next to your application.  
2. Download the usage history in CSV format for reporting or auditing. 
![View API usage](https://sadevportal3.blob.core.windows.net/root/post/3-api-key-activity.png) 

---

## Why the API key is important 🚀

The application key uniquely identifies your application and authorizes it to access the API.  
Without a valid API key, your requests will be rejected.  

When testing in Postman:  

1. Open the **Headers** tab in your request.  
2. Add a new header with:  

   | Key        | Value             |
   |-----------|-----------------|
   | X-API-KEY | *your API key*  |  

3. Save the collection so you don’t need to re-enter the key for every request.  

![Add API Key in Postman](https://sadevportal3.blob.core.windows.net/root/post/4-import-add-api-key.png)  

---

## Next steps 🚀 

- [Import the API specifications into Postman](/public/importing-endpoints-via-openapi-download-d37897/)   

