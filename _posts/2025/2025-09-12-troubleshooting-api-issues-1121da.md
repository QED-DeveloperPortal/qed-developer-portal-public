---
title: "Troubleshooting API issues"
slug: "troubleshooting-api-issues-1121da"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-12 05:54:43 
updatedBy: joyclyn
updated: 2025-09-16 22:49:27 
likes: 0
publishedOn: 2025-09-16 22:49:27
---

# Overview

When calling API endpoints from Postman or your application, you may encounter issues related to authentication, headers, or request formatting.  
This guide lists common problems and their solutions so you can quickly diagnose and resolve them.  

## Authentication issues  🔑

**Symptom**:  
You receive an error such as:  
- `401 Unauthorized`  
- `403 Forbidden`  

**How to fix**:  
✔ Ensure you have created a valid application key in the Developer Portal.  
✔ Add the key to the request header:  

| Key        | Value             |
|-----------|-----------------|
| X-API-KEY | *your API key*  |  

✔ If you are using environment variables in Postman, for example `{{apiKey}}`, double-check that the variable is set and selected in the current environment.  
✔ If you deleted or rotated your key, generate a new one and update it everywhere it’s used.  

## Missing or incorrect headers 📝

**Symptom**:  
The request fails, or you receive an unexpected response (e.g., `400 Bad Request`).  

**How to fix**:  
✔ Confirm the `X-API-KEY` header is present.  
✔ Make sure there are no typos in the header name or value.  
✔ Check that the `Content-Type` header is set appropriately (e.g., `application/json` for JSON requests).  


##  Expired or invalid tokens (if applicable)  ⏳

**Symptom**: 
You receive `401 Unauthorized` even though your API key or token was working earlier.  

**How to fix**:  
✔ If the API requires short-lived tokens, refresh or regenerate them.  
✔ In Postman, re-run the authentication request (if applicable) to fetch a new token.  
✔ In your application, implement token refresh logic to avoid downtime.  


## Common HTTP errors and fixes ⚠️

| Error code | Meaning                | Possible Fix |
|-----------|----------------------|-------------|
| **400**   | Bad request           | Check query parameters, request body, and header formatting. |
| **401**   | Unauthorized          | Verify API key, tokens, and authentication headers. |
| **403**   | Forbidden             | Ensure your key has permission to access the endpoint. |
| **404**   | Not found             | Check that you are calling the correct endpoint and URL path. |
| **429**   | Too many requests     | You may have hit rate limits. Wait and try again later. |
| **500**   | Internal server error | Retry after a few seconds. If it persists, contact support. |


##  Common pitfalls  🧰

 **Using the wrong environment:**: 
✔ Make sure you are calling the correct environment (sandbox vs. production).  

**Forgetting to save headers**:  
✔ In Postman, save the header and parameter setup in a collection to avoid re-entering every time.  

**Incorrect base URL**: 
✔ Double-check that your `{{baseUrl}}` variable or endpoint URL is correct and has no trailing slashes or typos.  

**Calling endpoints without parameters**:  
✔ Some endpoints require query parameters (e.g., `centreCode`, `zoneId`). Missing parameters may return empty results.  

**Using an expired key**:  
✔ If you deleted or rotated the key, older requests will fail until updated.  


## Need help?  🆘

**If issues persist after troubleshooting**:  
✔ Refer to the [Quick start guides](/public/quick-start-using-the-api-portal-959619/).  
✔ Check the API activity log in the Developer Portal for clues (e.g., failed request counts).  
✔ Contact the support team with the error message, request details, and timestamp for faster resolution.