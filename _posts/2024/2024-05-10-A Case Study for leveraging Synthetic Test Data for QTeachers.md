---
title: How to Consume Synthetic Data from Developer Portal
author: jeny-amatya-qed
categories: [Public]
tags: [datahub]
date: 2024-05-10 05:43:35 
updatedBy: jeny-amatya-qed
updated: 2024-05-13 01:01:13 
likes: 0
---

## Introduction
In an effort to provide test data for third-party applications such as QTeachers, Developer Portal team conducted a review of various synthetic data solutions. The objective was to find a solution that seamlessly integrates with our Datahub API specs and is as model agnostic as possible.

## Journey
We explored several solutions:
1. **Faker Library**: This required hardcoding business rules for generating test data, thus not being model agnostic.
2. **Mockaroo**: While it offered a web-based tool for generating realistic test data, it lacked support for complex data structures.
3. **Custom GPT Models**: However, due to immaturity of GPT models and unpredictable results, this option was not viable.

## Solution
The chosen solution involves using the Faker library to generate synthetic data and storing it in Cosmos DB. This approach allows endpoints to consistently return the same data based on the provided parameters, creating persistent yet artificially generated datasets. This method combines the capabilities of the Faker library with the persistence of a backend.

Sample data was generated for the following scenario: four schools, each with seven subject classes, fifty students, and ten staff members. Enrolment IDs for students and staff IDs for staff were kept consistent across all endpoints.

**School Centre Codes**: 7570, 1740, 6517, 0942

API requests should include the following mandatory headers:

| Key | Value |
| --- | --- |
|X-Api-Key  |API KEY saved earlier  |
|GenerationService  |StoredResponseGenerationService  |

Endpoints for accessing data:
- `/qt_student/school-api/schools/{centreCode}/students`
- `/qt_student/school-api/schools/{centreCode}/photos`
- `/qt_student/school-api/schools/{centreCode}/flags`
- `/qt_student/school-api/schools/{centreCode}/addresses`
- `/qt_student/school-api/schools/{centreCode}/parents`
- `/qt_student/school-api/schools/{centreCode}/emergency-contacts`
- `/qt_student/school-api/schools/{centreCode}/enrolment-history`
- `/qt_staff/school-api/schools/{centreCode}/staff`
- `/qt_staff/school-api/schools/{centreCode}/photos`

Pagination options:
- `navigationPage`: Page number (e.g., 1 for the first page, 2 for the second)
- `navigationPageSize`: Number of records per page (e.g., 10)

Example API call for the second page of 10 students for centreCode 1690:
[https://dp-mockaco.azurewebsites.net/qt_student/school-api/schools/1690/students?navigationPage=1&navigationPageSize=5](https://dp-mockaco.azurewebsites.net/qt_student/school-api/schools/1690/students?navigationPage=1&navigationPageSize=5)


## What Do I Need to Use This Data?
1. Log in to the Developer Portal.
2. Navigate to APIs -> My Applications.
3. Create an API key and save it for future use. This key must be added to the header of API calls.
4. Utilize any of the provided endpoints to execute the APIs and receive synthetic data in the response.

## Result
Developer Portal is currently collaborating with the QTeachers team to facilitate the execution of these endpoints and consumption of the generated data.
