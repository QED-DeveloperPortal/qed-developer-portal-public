---
title: "API Versioning"
slug: "api-versioning-8afe0b"
author: jeny-amatya-qed
tags: [api]
date: 2024-01-30 01:03:36 
publishedOn: 2024-01-30 01:03:36
categories: public
post-type: standard
status: archived
---

## What is API versioning?
API versioning is the process of managing and tracking changes to an API. It involves communicating those changes to the API's consumers.


## What are the benefits of API versioning?
API versioning enables the API producers to iterate in a way that minimizes breaking changes to the consumers and also provides a framework to communicate these changes effectively to consumers. This transparent strategy builds trust and then strengthens organization's reputation, hence boosting the API's adoption and retention rates.


## When should you version an API?
One should version the API whenever there is a "breaking change". A breaking change is the type of change that will require the consumers to modify their codebase in order to continue using the API. Some of these can involve changes to API's input and output data structures, success and error feedback and security mechanisms.
Some common examples of breaking changes are:
* Renaming a property or endpoint
* Turning an optional parameter into a required parameter
* Modifying a data format or type
* Modifying a property's characteristics


## What are some types of API versioning?
* URL versioning
    * The version number is included in the URL of the API endpoint.
    * Example: https://test-api.com/v1/items
* Query parameter versioning
    * The version number is included as a query parameter in the API request.
    * Example: https://test-api.com/items?version=v1
* Header versioning
    * The version number is passed as a header in the API request, which decouples the API version from the URL structure.
* Consumer-based versioning
    * The consumer chooses the appropriate version based on their needs. The version that exists at the time of the consumer's first call is stored with the consumer's information. Every future call is then executed against the same version, unless the consumer explicitly modifies the configuration.
    

## How do you version an API?
1. Choose a versioning strategy
2. Confirm if the new version is necessary
3. Update the API documentation
4. Gradually deploy the new version
5. Deprecate the old version 


## What are some best practices for API versioning?
* Design with extensibility in mind
* Know your consumers
* Include a versioning policy  in your terms of service
* Decouple implementation versioning and contract versioning
* Test thoroughly
* Plan for deprecation


### Reference
https://www.postman.com/api-platform/api-versioning/