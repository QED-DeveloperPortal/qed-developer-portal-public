---
title: "GET, POST, PUT, DELETE Examples"
slug: "get-post-put-delete-examples-e4d761"
author: andrew
tags: [api,getting-started]
date: 2025-09-16 04:23:44 
updatedBy: andrew
updated: 2025-09-16 22:32:29 
publishedOn: 2025-09-16 22:32:29
categories: public
post-type: standard
status: published
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

PUT
===

For PUT we demonstrated the API **/parent-api/schools/{zoneId}/parentpersonals/{eqId}/parents/{parentId}/addresses** add an address for a parent of a student:

In Postman we choose PUT from the dropdown as the type of request and then place something akin to the following in the address bar:

```
https://dp-mockaco.azurewebsites.net/STUDENT/parent-api/schools/443523/parentpersonals/1253674/parents/7694/addresses
```

As always, we set the x-api-key to a value created via the My Applications section of DevPortal.

In the Body tab, choose **raw** as the data type and past in the following entry:

```
{
  "LocalId": "172917",
  "PersonInfo": {
    "AddressList": [
      {
        "Street": {
          "Line1": "750907 Miles Platting Road",
          "Line2": ""
        },
        "City": "Eight Mile Plains",
        "StateProvince": "QLD",
        "Country": "1101",
        "PostalCode": "4113",
        "Type": "0765"
      }
    ]
  },
  "SIF_Metadata": {
    "LifeCycle": {
      "ETag": "ew0KICAicGFyZW50LXBlcnNvbmFscyI6ICJlVGFnVmFsdWUxIg0KfQ=="
    }
  }
}
```

Then click Send and after a short time a result similar to what follows with an accompanying response code of **200 OK** will appear:

```
{
    "response": {
        "Description": "Success",
        "Headers": {
            "Content-Type": {
                "UnresolvedReference": false,
                "Description": "Describes the format of the response: application/xml or application/json",
                "Required": true,
                "Deprecated": false,
                "AllowEmptyValue": false,
                "Explode": false,
                "AllowReserved": false,
                "Schema": {
                    "Type": "string",
                    "ReadOnly": false,
                    "WriteOnly": false,
                    "AllOf": [],
                    "OneOf": [],
                    "AnyOf": [],
                    "Required": [],
                    "Properties": {},
                    "AdditionalPropertiesAllowed": true,
                    "Enum": [],
                    "Nullable": false,
                    "Deprecated": false,
                    "Extensions": {},
                    "UnresolvedReference": false
                },
                "Examples": {},
                "Content": {},
                "Extensions": {}
            },
            "messageId": {
                "UnresolvedReference": false,
                "Description": "Unique identifier of the message. If provided in the request, then it is the same value as supplied in the request header.",
                "Required": true,
                "Deprecated": false,
                "AllowEmptyValue": false,
                "Explode": false,
                "AllowReserved": false,
                "Schema": {
                    "Type": "string",
                    "ReadOnly": false,
                    "WriteOnly": false,
                    "AllOf": [],
                    "OneOf": [],
                    "AnyOf": [],
                    "Required": [],
                    "Properties": {},
                    "AdditionalPropertiesAllowed": true,
                    "Enum": [],
                    "Nullable": false,
                    "Deprecated": false,
                    "Extensions": {},
                    "UnresolvedReference": false
                },
                "Examples": {},
                "Content": {},
                "Extensions": {}
            },
            "messageType": {
                "UnresolvedReference": false,
                "Description": "The message type. Will be RESPONSE for a successful response.",
                "Required": true,
                "Deprecated": false,
                "AllowEmptyValue": false,
                "Explode": false,
                "AllowReserved": false,
                "Schema": {
                    "Type": "string",
                    "ReadOnly": false,
                    "WriteOnly": false,
                    "AllOf": [],
                    "OneOf": [],
                    "AnyOf": [],
                    "Required": [],
                    "Properties": {},
                    "AdditionalPropertiesAllowed": true,
                    "Enum": [
                        {
                            "PrimitiveType": "string",
                            "AnyType": "primitive",
                            "Value": "RESPONSE"
                        }
                    ],
                    "Nullable": false,
                    "Deprecated": false,
                    "Extensions": {},
                    "UnresolvedReference": false
                },
                "Examples": {},
                "Content": {},
                "Extensions": {}
            },
            "responseAction": {
                "UnresolvedReference": false,
                "Description": "The response action. Will be UPDATE for this action.",
                "Required": true,
                "Deprecated": false,
                "AllowEmptyValue": false,
                "Explode": false,
                "AllowReserved": false,
                "Schema": {
                    "Type": "string",
                    "ReadOnly": false,
                    "WriteOnly": false,
                    "AllOf": [],
                    "OneOf": [],
                    "AnyOf": [],
                    "Required": [],
                    "Properties": {},
                    "AdditionalPropertiesAllowed": true,
                    "Enum": [
                        {
                            "PrimitiveType": "string",
                            "AnyType": "primitive",
                            "Value": "UPDATE"
                        }
                    ],
                    "Nullable": false,
                    "Deprecated": false,
                    "Extensions": {},
                    "UnresolvedReference": false
                },
                "Examples": {},
                "Content": {},
                "Extensions": {}
            }
        },
        "Content": {},
        "Links": {},
        "Extensions": {},
        "UnresolvedReference": false
    }
}
```

