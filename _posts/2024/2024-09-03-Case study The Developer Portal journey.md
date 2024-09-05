---
title: Case study The Developer Portal journey
author: g-morton
categories: [Public]
classification: Official (Everyone)
tags: [architecture,case-study]
date: 2024-09-03 00:06:01 
updatedBy: g-morton
updated: 2024-09-03 05:19:53 
likes: 0
---

#### Who should read this case study?
This case study is intended for IT professionals, project managers, and government officials involved in digital transformation projects, particularly within the public sector. It will also be of interest to developers and vendors who want to understand how a developer portal can enhance collaboration, innovation, and compliance with government standards. Readers should gain insights into the project’s milestones, challenges, and successes, and learn practical lessons for implementing similar initiatives.

#### Introduction
The Developer Portal was conceived with the goal of creating a centralised platform that would streamline access to development tools, resources, and standards for both internal and external users. This initiative was aligned with the Department of Education’s digital strategy, focusing on fostering innovation, improving transparency, and promoting best practices in software development. The portal aimed to support a diverse range of stakeholders, including government staff, external vendors, and the broader developer community.

#### Context
Prior to the Developer Portal, the Department of Education faced challenges related to fragmented development processes, duplication of efforts, and inconsistent code quality. The absence of a unified platform for managing development activities led to inefficiencies and a lack of standardisation. The Developer Portal is designed to improve these issues by providing a "single source of truth" for all development-related activities, including API access, documentation, and collaboration tools. Additionally, the portal aims to securely facilitate information sharing between the department and its external partners, ensuring that all stakeholders had the resources needed to deliver high-quality digital services.

#### Approach
The development journey of the Developer Portal involved multiple phases, during which the team explored and adopted various technologies and platforms:

- **Initial exploration**: The team initially considered traditional CMS and custom-built solutions, but these were set aside due to scalability concerns. The need for a more modern, cloud-based architecture became apparent, leading to a shift towards cloud-native solutions.

- **Pivot to cloud-native architecture**: The team chose to leverage Azure services, including Azure Functions and Cosmos DB, for content management and storage. This decision was driven by the need for a solution that could handle high volumes of data and provide real-time content management capabilities. The adoption of GitHub for version control and feature management now plays a key role in the product’s success.

- **Microservices architecture**: The portal was built around a microservices architecture, allowing for greater flexibility and scalability. This approach was crucial in supporting diverse content types and user interactions, from API integrations to AI-driven content transformations.

**Software lifecycle management**: The portal's development process was managed using GitHub for storage and publication. Feature branches were employed to enable the rapid deployment of updates and improvements. The release pipeline followed a structured approach, progressing from internal development (Dev/Pre-alpha) to broader public testing (Beta), before moving towards general availability. The Developer Portal is currently labelled as **Beta**, inviting early adopters to explore and provide feedback while managing expectations that some features may still be evolving.

- **Security and safety**: To ensure the portal's security, all sandbox data is 100% simulated, with no connections to production databases. This approach ensures that the portal is safe for developers to interact with, minimising the risk of malicious exploitation.

#### Challenges
Several challenges emerged during the journey, particularly due to the department's initial limited adoption of cloud technologies and modern development practices. There was also resistance to embracing 'continuous improvement' methodologies, which supported our phased public release approach. This created some friction in the early stages of development. Additionally, the team faced the challenge of designing the portal to meet the diverse needs of various user groups—internal developers, external vendors, and third-party partners—while maintaining high standards of security and usability.

#### Results
The Developer Portal is improving development processes and raising awareness of modern software 'best practices' within the department. The portal is also enhancing collaboration between internal teams, leading the way for more consistent and higher-quality software products. User feedback is positive, with many praising the portal’s ease of use and the resources it provides.

#### Lessons learned
One of the key lessons learned from the initiative was the importance of being flexible and open to change during the development process. The early phased release approach allowed the team to build momentum and pivot quickly in response to emerging needs. By adopting a cloud-native, microservices architecture, the product gained the adaptability needed to evolve alongside these changes. The Beta site has been instrumental in this process, enabling us to rapidly, safely, and transparently adjust features to meet the needs of our members and stakeholders. This iterative approach has proven invaluable in refining the portal and ensuring its alignment with user expectations.

#### Conclusion
The Developer Portal initiative is supporting transformative change within the Department of Education, offering a centralised, secure platform that fosters innovation and collaboration. Through its adoption of modern software development practices and a culture of continuous improvement, the portal has not only enhanced efficiency and quality but is also laying a robust foundation for future digital initiatives. As the portal continues to evolve, it will play a pivotal role in advancing the department’s digital strategy and its commitment to delivering high-quality, user-centred digital services.

We are excited to extend the benefits of the Developer Portal to you.
Join us on this journey!