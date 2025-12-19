---
title: "Code examples of connecting your app"
slug: "code-examples-of-connecting-your-app-661a99"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [getting-started,api]
date: 2025-09-10 23:10:34 
updatedBy: Joyclyn
updated: 2025-09-16 22:41:53 
likes: 0
publishedOn: 2025-09-16 22:41:53
---

# Overview  
This guide shows you how to connect to the API sandbox using your **application key**. It includes examples in **cURL**, **Node.js**, **Python**, and **C#** so you can make your first API call quickly and confidently.


### Authentication 🔑
All API requests must include your **application key** for authentication.
- Add it to the request **headers** using the format: 

```http
X-API-KEY: YOUR_APP_KEY
```
 > **Tip** 💡
>  Replace YOUR_APP_KEY with your actual Application Key before running the examples below.

### Example: cURL 📌
```bash
curl -X GET "https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245" \
      -H "X-API-KEY: YOUR_APP_KEY"

```

### Example: node.js 📌
```javascript
const axios = require("axios");

axios.get("https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245", {
  headers: { "X-API-KEY": "YOUR_APP_KEY" }
})
.then(res => console.log(res.data))
.catch(err => console.error(err));
```

### Example: Python 📌
```python
import requests

url = "https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245"
headers = {
    "X-API-KEY": "YOUR_APP_KEY"
}

response = requests.get(url, headers=headers)
print(response.json())
```

### Example: C# 📌
```csharp
using System.Net.Http;

var client = new HttpClient();
client.DefaultRequestHeaders.Add("X-API-KEY", "YOUR_APP_KEY");

var response = await client.GetStringAsync("https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245");
Console.WriteLine(response);
```

### Next steps
Run one of these examples to confirm your application key is working and that you can retrieve data from the sandbox environment safely.