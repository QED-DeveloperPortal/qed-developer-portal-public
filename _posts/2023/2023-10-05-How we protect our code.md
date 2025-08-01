---
title: "Exploring DevSecOps security with GitHub"
slug: "exploring-devsecops-security-with-github-0da1f1"
author: Joyclyn
categories: Public
classification: Public
tags: [security]
date: 2023-10-05 01:46:39 
updatedBy: Joyclyn
updated: 2025-08-01 00:36:44 
likes: 0
---

'Secure code' isn't a single thing but a complex blend of factors. Two major factors that influence our Developer Portal set up are:
1. the practice of 'DevSecOps' 
2. security features provided by the GitHub Enterprise platform. 

### What is DevSecOps?
DevSecOps is a set of practices and principles that aim to integrate security (Sec) into the DevOps (Development and Operations) process. It's an approach to software development and IT operations that places a strong emphasis on security throughout the entire software development lifecycle. DevSecOps aims to strike a balance between agility, speed, and security in the software development process. 

It acknowledges that security should not be a barrier to rapid development and deployment but should be an integral part of the process that enhances the overall security of applications and systems.

Some practical examples include:
* Incorporating security needs into user stories and acceptance criteria.
* Building moderation workflows in GitHub to trigger content review before code is pushed.

Incorporating DevSecOps practices fosters a proactive approach to security throughout the software development lifecycle.

### What security features does GitHub Enterprise offer?

* **Access control**: We can define and enforce access control policies, including specifying who can access repositories, branches, and other resources.
* **Code scanning**: GitHub Enterprise integrates with security scanning tools to detect vulnerabilities and security issues in code, including dependency scanning and secret scanning. It automatically analyses code for potential threats and provides alerts to our developers.
* **Dependency analysis**: GitHub has a built-in tool—*Dependabot*—that proactively identifies and mitigates security risks related to outdated or vulnerable libraries or packages in our code. 
    * Dependabot automatically checks our code, shows us exactly where in the code we’re vulnerable and creates pull requests to update dependencies to their latest, secure versions. This automation ensures that we can quickly apply security patches without manual intervention. 
    * We can customise Dependabot's update policies to align with our security and compliance requirements and we can specify which updates can be automatically applied and which require manual approval.
* **Audit logging**: GitHub Enterprise maintains comprehensive audit logs, which record all user and system activity. This would help us track changes and investigate in the unlikely event of suspicious or unauthorised activities.
* **Private instances**: GitHub Enterprise allows us to host our own private GitHub instance, which gives us greater control over data, security and configurations. 
* **Enterprise-grade support**: A GitHub Enterprise account comes with priority support and service level agreements. This means we can get quicker responses and support for security-related issues.
* **Private network deployment**: We can deploy within our private network or on a cloud platform of our choice. This allows us more control over network security and data isolation.
* **Custom integrations**: We have more flexibility to integrate GitHub Enterprise with our security tools and processes. This includes customising security workflows and integrations with existing security information and event management systems.
* **High availability**: GitHub Enterprise offers options for high availability and redundancy, reducing the risk of downtime due to infrastructure failures.

### Are there any gaps?
Of course there are potential gaps, nothing is entirely without risk. 
Although GitHub Enterprise offers robust security features, we still consider: 

* **Configuration errors**: Misconfiguration can still occur, leading to security vulnerabilities. This can be mitigated by regular audits and monitoring.
* **Human error**: Users with certain privileges can inadvertently cause security issues. Training and access controls can help to mitigate this risk.
* **Zero-day vulnerabilities**: GitHub Enterprise may not always protect against newly discovered vulnerabilities until updates or patches are released.

A comprehensive security strategy that includes best practices in configuration management, employee training, and monitoring for emerging threats will help to address potential gaps and maintain a secure environment.

### So how safe is our Developer Portal code?
It’s difficult, and perhaps even foolish, to try to assign a security rating or number to the security of our code. But with the layers of protection we have in our practices (DevSecOps) and our infrastructure (GitHub Enterprise), our code is well protected.