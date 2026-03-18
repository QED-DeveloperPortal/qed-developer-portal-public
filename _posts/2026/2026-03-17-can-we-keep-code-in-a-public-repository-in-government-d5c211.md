---
title: "Can we keep code in a public repository in government?"
slug: "can-we-keep-code-in-a-public-repository-in-government-d5c211"
author: joyclyn
categories: public
tags: [myths]
post-type: standard
status: published
date: 2026-03-17 00:41:46 
updatedBy: joyclyn
updated: 2026-03-18 05:02:07 
publishedOn: 2026-03-18 05:02:07 
---

This post is a follow-on to my previous post that asks, [Can we use open source software in government?](https://developer.qed.qld.gov.au/public/can-we-use-open-source-software-in-government-1bfe68/) and addresses the question about keeping code *we* create and manage in a public repository. 

So, can we create and manage code in a public repository in government? 
The short answer is **yes** we can. 

In fact, since January 2022, the Queensland Government Enterprise Architecture (QGEA) digital service standard has specified that *all new source code must be open by default*, recognising that open sources helps to: 
* reduce costs
* avoid lock-in
* stop duplication
* increase transparency
* add benefits, from improvements by other developers.

The QGEA also provides a guideline on OSS, giving Queensland agencies information and advice to consider when using and releasing OSS. The guideline acknowledges that, by making our in house software available as OSS we support the: 
* cultivation of trust with Queenslanders and our partners
* leveraging of our existing investments within government and industry.


| Myth or concern | Reality | 
| -- | -- |
| Publishing our code is a security risk. | Security depends on protecting credentials and infrastructure rather than hiding source code. Sensitive information should never be stored in a public repository.| 
| What if sensitive information is accidentally committed to a public repository? | Standard development practices and automated scanning tools help prevent credentials or confidential information from being published. But if they are, it’s quick and easy to roll changes back. |
| Having a public codebase means external parties can interfere with our code. | All suggested changes must be reviewed and approved by authorised maintainers before they become part of the code base. | 
| Having a public codebase opens the department up to criticism.  | Public visibility can attract feedback, but it can also improve quality and transparency by allowing issues to be identified and discussed openly. | 
| Exposing our codebase to the public will overload the department with suggestions and issues. | Public repositories can accept feedback without committing the organisation to implement or support every request or creating an obligation to provide ongoing support. The README file can be a good place to set boundaries for interaction. | 

***

Further reading: 
•	QGEA (Queensland Government Enterprise Architecture) (2025) [Open data, information sharing, access and use policy](https://www.forgov.qld.gov.au/information-technology/queensland-government-enterprise-architecture-qgea/qgea-directions-and-guidance/qgea-policies-standards-and-guidelines/open-data-information-sharing-access-and-use-policy), accessed 17 March 2026.