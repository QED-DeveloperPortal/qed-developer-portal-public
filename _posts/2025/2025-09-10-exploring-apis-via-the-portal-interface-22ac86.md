---
title: "Exploring APIs via the Portal interface"
slug: "exploring-apis-via-the-portal-interface-22ac86"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:16:41 
updatedBy: jeny-amatya-qed
updated: 2025-09-10 23:28:30 
likes: 0
---

# Draft 
The Portal interface is like a practice exam – a safe space to try before you go live.
[add screenshot]

1. Go to the API catalogue
2. Select an API product within the catalogue (e.g., QTeachers catalogue - >Staff)
3. Select the API endpoint.
4. Enter parameters (like centreCode = 12345)
5.  Click on Execute button and see the JSON response
```json
[
  {
    "staffCentreId": "90087",
    "staffId": "84748",
    "title": "Mr.",
    "familyName": "Reynolds",
    "givenNames": "Layla",
    "timetableCode": "HOMEMI",
    "staffType": {
      "code": "D",
      "description": "Departmental"
    },
    "staffStatus": {
      "code": "A",
      "description": "Active"
    },
    "gender": {
      "code": "F",
      "description": "Female"
    }
  },...
```
