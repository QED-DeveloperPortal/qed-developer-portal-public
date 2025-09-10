---
title: "Importing endpoints via OpenAPI download"
slug: "importing-endpoints-via-openapi-download-d37897"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,ai]
date: 2025-09-10 23:24:12 
likes: 0
---

# Draft
1. Download and install Postman.
2. Import endpoints
    1. From the API catalogue, download the OpenAPI specs
    2. In Postman, click Import -> upload the file
    3. You can see all the endpoints
3. Add application key
    1. In Postman, open the Headers tab.
    2. Add the entry for X-API-KEY.
    3. Paste the application key.
4. Run a request
    1. Pick an endpoint (e.g. https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff )
    2. Enter parameters (eg. centreCode=111)
    3. Click Send and you will get the results.
[add screenshot]
```json
Add results here
```
 Pro Tip: Save collections in Postman so you don’t have to re-enter every time.💡
[add screenshot]