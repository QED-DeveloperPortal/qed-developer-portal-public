---
title: "How the API Catalogue works"
slug: "how-our-application-catalogue-works-0737f7"
author: andrew
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:15:59 
updatedBy: jeny-amatya-qed
updated: 2025-09-15 02:13:14 
likes: 0
---

# What is the API Catalogue?

The **API Catalogue** is your one-stop shop for discovering and using the Department of Education's APIs. It allows you to:

- **Explore** available APIs and their documentation
- **Download** OpenAPI specification
- **Test** APIs directly in the Developer Portal sandbox or with tools like Postman
- **Integrate** APIs into your own applications

> 💡 **Good to know:** The API Catalogue is designed for developers at all levels — whether you're just getting started or already experienced.  
 
---
## API Groups
The API Catalogue currently includes the following groups of APIs:  

* Consent Management
* Attendance/Roll Marking
* Booking Systems
* DOE Test Clients
* Library Management Systems
* SMS/Text Messaging Providers
* Student Management
* Student Management Publisher

Additionally, there are three **QTeachers** groups:

* Rollmarking
* Staff
* Student

## Where did API Catalogue come from?

The **DataHub** is the Department of Education's internal service and team responsible for securely exposing APIs. These APIs enable both internal systems and external vendor applications to interact with the Department data and services.

The API Catalogue is simply the developer-friendly view of these APIs. 
It is designed to help you quickly develop, test, and integrate your applications with Department systems.

* **While testing** APIs that we surface through API catalogue, use the base URL: 
```http
https://dp-mockaco.azurewebsites.net.
```
* **When going live**, all production APIs use a consistent base URL: 

```http
http://api.qed.gov.au
```

> 🔑 Tip: Once your application is approved by the Department, you can apply for security credentials to access production APIs.

## Why the API Catalogue matters
Using the API Catalogue saves you time and reduces guesswork. It ensures you are:

- **Working with trusted, up-to-date information** - so your apps stay compatible with Department systems
-  **Testing safely** - with a dedicated test environment before going live
-  **Building secure integration** - by following the Department's approved process for credentials and API access
- **Scaling easily** - as more APIs are added, your applications can expand their capabilities without major rework

> The API Catalogue helps you build better, more reliable applications faster. 

## Next steps for getting started
- **Visit the Portal interface** - Browse the [API Catalogue](https://developer.qed.qld.gov.au/apis/) and review the available API groups
- **Download the API specifications** - Use the OpenAPI spec to understand endpoints, parameters, and request/response formats.
- **Try an API call** - Execute the API endpoint in Developer Portal's API sandbox or import the spec into Postman.
-. **Experiment in the test environment** - Send request to: 
```http
   https://dp-mockaco.azurewebsites.net 
```
- **Plan your integration** - Once your app is ready, request approval and security credentials to access the production environment.