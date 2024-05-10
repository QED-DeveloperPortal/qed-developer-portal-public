---
title: A Case Study for leveraging Synthetic Test Data for QTeachers
author: jeny-amatya-qed
categories: [Public]
tags: [datahub]
date: 2024-05-10 05:43:35 
likes: 0
---

# Introduction:
In the era of data-driven decision-making, quality assurance (QA) processes are indispensable, especially in systems dealing with sensitive information such as educational data. This case study explores the utilization of synthetic test data to ensure the robustness and reliability of the **QTeachers** data hub sandbox. The challenge was to create a flexible solution capable of seamlessly integrating with various data hub models while being agnostic to changes in data structures.

# Problem Statement:
The **QTeachers** project required a reliable method to generate synthetic test data for its data hub sandbox. This data needed to mimic real-world scenarios, be scalable, and easily adaptable to accommodate potential changes in the data hub models. Traditional methods such as manual data entry or extracting data from production environments were impractical due to time and privacy constraints.

# Approaches Investigated:

### Faker Library: 
An open-source Python library designed to generate fake data for various purposes. While versatile, it lacked customization options specific to the QTeachers' requirements.

### Mockaroo: 
A web-based tool for generating realistic test data. Despite its ease of use, it did not offer the level of control needed for complex data structures.

### Custom GPT Models:
Leveraging custom-trained GPT models to generate synthetic data. While promising, it required significant investment in model development and training.

### Live, JIT, or Pre-generated Data:
Considering live data feeds, Just-In-Time (JIT) generation, or pre-generated datasets. While effective, these methods lacked scalability and were not suitable for dynamic testing environments.

# Proposed Solution:
The proposed solution aimed to address the QTeachers' need for flexible, scalable, and customizable synthetic test data. By simulating a real-world scenario, a service was implemented to generate synthetic data for a set of related API endpoints.

## Use Case:
The use case involved simulating data for four schools, each with seven subject classes, fifty students, and ten staff members. Sample data included consistent enrolment IDs for students and staff IDs for staff across all endpoints.

## Implementation:

### School Generation:
Schools were generated with unique school codes (e.g., 4650, 1690, 9743, 0220) to simulate diversity within the dataset.

### API Endpoints:
A series of API endpoints were defined to retrieve synthetic data for various entities such as students, photos, addresses, parents, emergency contacts, and enrolment history.
/qt_student/school-api/schools/{centreCode}/students
/qt_student/school-api/schools/{centreCode}/photos
/qt_student/school-api/schools/{centreCode}/flags
/qt_student/school-api/schools/{centreCode}/addresses
/qt_student/school-api/schools/{centreCode}/parents
/qt_student/school-api/schools/{centreCode}/emergency-contacts
/qt_student/school-api/schools/{centreCode}/enrolment-history
/qt_staff/school-api/schools/{centreCode}/staff
/qt_staff/school-api/schools/{centreCode}/photos

### Pagination Support:
Each API call supported pagination, enabling retrieval of specific subsets of data based on navigation page and page size parameters. For example, to return the 2nd page of 10 students for centreCode 1690:
/qt_student/school-api/schools/1690/students?navigationPage=1&navigationPageSize=5

# Conclusion:
In conclusion, the implementation of synthetic test data for the QTeachers project provided an effective solution for ensuring the reliability and robustness of the data hub sandbox. By leveraging a simulated real-world scenario, the solution offered flexibility, scalability, and adaptability to changing data models. Through this case study, it becomes evident that synthetic test data generation is a valuable tool in the arsenal of QA processes, especially in complex and dynamic environments such as educational data systems.