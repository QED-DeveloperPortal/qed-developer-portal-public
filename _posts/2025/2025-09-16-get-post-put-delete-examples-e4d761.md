---
title: "GET, POST, PUT, DELETE Examples"
slug: "get-post-put-delete-examples-e4d761"
author: andrew
categories: Public
classification: Public
tags: [api,getting-started]
date: 2025-09-16 04:23:44 
updatedBy: andrew
updated: 2025-09-16 05:54:38 
likes: 0
---

Here are  examples of using POST, PUT and DELETE requests from the API Catalogue.

For POST we demonstrate using the /visaentitlement-api/studyentitlement:check api that is available in the VisaEntitlement-API section of Student Management inside API Catalogue.

For Request Body Content we can use the following JSON:

```
{
  "StudentPersonal": [
    {
      "PersonInfo": {
        "Name": {
          "FamilyName": "FamilyName1",
          "GivenName": "GivenName1"
        },
        "Demographics": {
          "BirthDate": "2011-03-22T0:00:00+10:00",
          "PassportNumber": "123456789",
          "PassportCountryCode": "AUS"
        }
      }
    },
    {
      "PersonInfo": {
        "Name": {
          "FamilyName": "FamilyName2",
          "GivenName": "GivenName2"
        },
        "Demographics": {
          "BirthDate": "2006-03-22T0:00:00+10:00",
          "PassportNumber": "987654321",
          "PassportCountryCode": "AUS"
        }
      }
    }
  ]
}
```

When we run this API we get the following Response back:

```
{
  "Description": "Accepted"
}
```