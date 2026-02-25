---
title: "Code examples of connecting your app"
slug: "code-examples-of-connecting-your-app-661a99"
author: jeny-amatya-qed
categories: public
tags: [getting-started,api]
date: 2025-09-10 23:10:34 
updatedBy: jeny-amatya-qed
updated: 2025-09-10 23:17:48 
likes: 0
publishedOn: 2025-09-10 23:17:48
---

# Overview  
This guide shows you how to connect to the API sandbox using your **Application Key**.  
It includes examples in **cURL**, **Node.js**, **Python**, and **C#** to help you get started quickly.  

---

##  Authentication  🔑
Every request must include your **Application Key**:  
- Add it to the **headers** as `X-API-KEY: <key>`  

Example header:  

```http
X-API-KEY: YOUR_APP_KEY
```

### Example: cURL
```bash
curl -X GET "https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245" \
      -H "X-API-KEY: YOUR_APP_KEY"

```

### Example: node.js
```javascript
const axios = require("axios");

axios.get("https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245", {
  headers: { "X-API-KEY": "YOUR_APP_KEY" }
})
.then(res => console.log(res.data))
.catch(err => console.error(err));
```

### Example: Python
```python
import requests

url = "https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245"
headers = {
    "X-API-KEY": "YOUR_APP_KEY"
}

response = requests.get(url, headers=headers)
print(response.json())
```


### Example: C#
```csharp
using System.Net.Http;

var client = new HttpClient();
client.DefaultRequestHeaders.Add("X-API-KEY", "YOUR_APP_KEY");

var response = await client.GetStringAsync("https://dp-mockaco.azurewebsites.net/QT_staff/school-api/schools/111/staff?centreCode =1245");
Console.WriteLine(response);
```

✅ Tip: Replace YOUR_APP_KEY with your actual Application Key before running these requests.
This will allow you to test endpoints in the sandbox environment safely.