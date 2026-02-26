---
title: "Mobile application and operating systems standard"
author: joyclyn
tags: [standards]
date: 2024-04-08 01:25:35 
publishedOn: 2024-04-08 01:25:35
categories: public
post-type: standard
status: published
---

# Mobile application and operating systems standard
CM: 19/227306
Implementation date: 1 July 2019
Version: 2.0

## Audience
* Department-wide, including but not limited to including schools, divisions, units, offices and business units.
* Technical and business professionals, and service partners who participate in the design, development, maintenance and support of IT solutions. 
* Project managers, business analysts or anyone involved during portfolio and project planning, conducting impact assessments or requirements analysis activities.

## Purpose
This document details the Department of Education mobile application development and mobile operating system standard. Support mobile operating systems and versions are declared along with mobile application development standards, which ensures that the department develops applications that are secure by design and industry supported secure mobile operating systems.

## 1. Scope
The following items are within the scope of this standard: 
* Resources consumed by the department to support, maintain or update mobile applications as a result of: 
    * procurement of ICT services
    * ICT development projects
* External developers or vendors developing mobile applications for, or on behalf of, the department.

Out of scope: Software-as-a-service based mobile applications developed by vendors or government agencies whom will fully support and maintain the application.

## 2. Exemptions handling
* Any exemption to this standard could be subject to CIO approval.
* All exemptions require approval by the Domain Architecture and Standards Group.

## 3. Standard exceptions
### Microsoft Windows Mobile
The department has stopped further development efforts for Microsoft Windows Mobile and is retiring this platform. Existing departmental applications must be supported until the application is removed from the Windows Store.

## 4. Mobile operating systems
### 4.1 Apple iOS

Apple iOS must be supported for the current and previous three `MAJOR `versions.
Determining the supported version is calculated as follows `N `minus `3 `version support where `N` is the `MAJOR `version number.

### 4.2 Google Android
Google Android must be supported for the current and previous five `MAJOR `versions. 
Determining the supported version is calculated as follows `N `minus `5 `version support where `N `is the `MAJOR `version number.

## 5. Early support withdrawal 
Early withdrawal of support is where the department should immediately stop support and development for mobile operating systems where the developer of vendor has withdrawn support due to security or compatibility reasons. 

## 6. Mobile application development
### 6.1 Security 
Mobile application developers must follow security or development best practices in the following order of priority: 
1. Latest Information Management and Information Security standards and processes specified by the department.
2. Latest departmental application development best practices and standards. 
3. Latest mobile operating system development, security guidelines and best practices available; for example: 
    * NIST 800-163 Vetting the Security of Mobile Applications.
    * OWASP Mobile Security Testing Guide.  

### 6.2 Version numbering
Development of mobile applications must adhere to `MAJOR.MINOR.PATCH` semantic versioning. 

#### 6.2.1 Versioning guidance
The first version of a mobile application must always start with a `MAJOR `version of 1 and should use the following guidelines when incrementing version numbers:
*  `MAJOR `version when you make incompatible or breaking changes
* `MINOR `version when you add functionality in a backwards-compatible manner
* `PATCH `version when you make backwards-compatible bug fixes.

## Legislation
Nil

## Related policies
Nil

## Related procedures
Nil

## Related standards
* Semantic versioning
* NIST 800-163 Vetting the Security of Mobile Applications

## Guidelines
Nil

## Supporting information/websites
* OWASP Mobile Security Testing Guide
* ACSC - Update on processor vulnerabilities (Meltdown/Spectre)
