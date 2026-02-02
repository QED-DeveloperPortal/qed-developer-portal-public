---
title: "How our API catalogue works"
slug: "how-our-application-catalogue-works-0737f7"
author: andrew
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:15:59 
updatedBy: joyclyn
updated: 2025-09-16 00:49:50 
likes: 0
publishedOn: 2025-09-16 00:49:50
---

## What is the API catalogue?

Our **API catalogue** is your one-stop shop for discovering and using our APIs. 
It allows you to:

- **Explore** available APIs and relevant documentation
- **Download** OpenAPI specifications
- **Test** APIs directly in the Developer Portal sandbox or with tools like Postman
- **Integrate** APIs into your own applications

> **Good to know** 💡
> Our API catalogue is designed for developers at all levels — whether you're just getting started or already experienced. 
 

## Where did the API catalogue come from?

**Data Hub** is our internal service responsible for securely exposing APIs. These APIs enable both internal systems and external vendor applications to interact with our data and services.

Our API catalogue is simply the developer-friendly view of these APIs. They are *non-production* versions of our APIs, designed to help you quickly develop, test, and integrate your applications with department systems.

* **While testing** APIs that we surface through API catalogue, use the base URL: 
```http
https://dp-mockaco.azurewebsites.net
```
* **When going live**, all production APIs use a consistent base URL: 

```http
http://api.qed.gov.au
```

> Tip 🔑 
> Once your application is approved by the department, you can apply for security credentials to access production APIs. Until then, the Developer Portal provides everything you need to get ready. If you think we're missing something, [send us some feedback](https://developer.qed.qld.gov.au/contact-us/) to let us know how we can improve.

## Why the API Catalogue matters
Using our API catalogue saves you time and reduces guesswork. 
It ensures you are:

- **working with trusted, up-to-date information**, so your apps stay compatible with department systems
-  **testing safely**, with a dedicated test environment before going live
-  **building secure integration**, by following our approved process for credentials and API access
- **scaling easily**, as more APIs are added, your applications can expand their capabilities without major rework.

Our API catalogue helps you build better, more reliable applications faster. 

## Next steps
- **Visit the portal interface**: Browse our [API catalogue](https://developer.qed.qld.gov.au/apis/) and review the available API groups.
- **Download the API specifications**: Use the OpenAPI spec to understand endpoints, parameters, and request/response formats.
- **Try an API call**: Execute the API endpoint in our API sandbox or import the spec into Postman.
- **Experiment in the test environment** by sending a request to: 
```http
   https://dp-mockaco.azurewebsites.net 
```