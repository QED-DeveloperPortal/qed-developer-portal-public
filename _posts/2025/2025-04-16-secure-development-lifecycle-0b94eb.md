---
title: "Secure development lifecycle"
slug: "secure-development-lifecycle-0b94eb"
author: g-morton
categories: Public
classification: Public
tags: [standards,security]
date: 2025-04-16 05:05:41 
updatedBy: jeny-amatya-qed
updated: 2025-09-24 23:04:01 
likes: 0
publishedOn: 2025-09-24 23:04:01
---

**Overview**  
To ensure security is designed into software and systems from the beginning, development teams must adopt and apply secure development *standards, controls, and best practices* throughout the software development lifecycle (SDLC).

Security should not be a final checkbox—it must be baked into the everyday way we plan, build, test, deploy, and evolve digital solutions.

Our [development principles](https://developer.qed.qld.gov.au/public/software-development-practice-db6ab5/) describe how we aim to deliver secure, high-quality, and user-focused products in a modern, sustainable way.



### Secure development practices

| Area | Standard & best practices |
|------|---------------------------|
| **Planning & design** | Security, change-readiness, and prototyping must be considered early. While established patterns (e.g., separation of concerns, microservices) offer a solid foundation, they must evolve with the solution. Teams should enable fast, lightweight prototyping to validate designs rather than relying solely on documentation. Threat modelling and early risk identification should be part of initial planning activities. |
| **Code management** | Code must be managed using trusted systems (e.g., Azure DevOps, GitHub). Use **feature branching** to isolate changes and maintain stability. Code should be **modular, testable, and scannable**, supporting iterative delivery and continuous refactoring. Apply access controls, mandatory peer reviews, and **automated static analysis tools** (e.g., SonarQube) to surface technical debt and vulnerabilities early. |
| **Testing** | Testing must occur continuously during development—not just at the end. Use feature-level unit, integration, and security tests embedded in the CI/CD workflow. Security validation should be built into delivery pipelines (e.g., dependency scanning, code quality gates), not reliant on annual penetration tests. Synthetic or obfuscated data should always be used in non-production environments. |
| **Deployment** | Deployments should be **small, frequent, and automated** to reduce risk and support faster feedback. Avoid “big bang” releases. Use tools like **Azure Pipelines** or **GitHub Actions** to ensure consistent, repeatable deployment with built-in quality gates and environment-specific secrets management. Where appropriate, deploy changes to a **beta or trusted user group** first, using feature flags or staged rollouts to reduce risk. |
| **Stakeholder collaboration** | Engage stakeholders continuously throughout development—not just at delivery milestones. Co-design sessions, product reviews, and early user engagement (e.g., with beta testers) are essential to aligning security, usability, and business goals. Teams should regularly demonstrate working features and gather feedback to ensure the product remains fit-for-purpose. |
| **Risk management** | Post-deployment, maintain visibility over system health and security through logging, telemetry, and alerting. Audit trails, behavioural analytics, and regular review of access and data use should be part of the operational lifecycle. Maintain awareness of known vulnerabilities in dependencies via tools like **Dependabot** or **Snyk**. |



### Case study: The Developer Portal  
The **Developer Portal** exemplifies a modern and secure SDLC model, delivering high-value outcomes using lightweight, flexible controls:

- **Agile delivery** enables ongoing prioritisation and re-alignment of effort based on emerging needs.
- **Feature branching** and modular code in **GitHub** and **Azure DevOps** ensure flexibility and traceability.
- **DevSecOps pipeline** integrates security into the development lifecycle from day one.
- **Separation of concerns** between logic, data, and presentation allows targeted updates and clearer risk controls.
- **Soft launching via beta flags** enables real-time feedback from early adopters without compromising general stability.
- **Synthetic test data** ensures privacy and compliance while maintaining functional testing integrity.
- **Frequent feature-level reviews** promote team awareness, quality, and opportunities to pivot based on feedback.



### Sample secure controls in practice

| Control type | Example tools / techniques |
|--------------|-----------------------------|
| Version control & feature branching | Azure DevOps, GitHub, GitHub Flow |
| Security-aware CI/CD | Azure Pipelines, GitHub Actions with built-in quality and security gates |
| Static code analysis | SonarQube, GitHub Advanced Security, ESLint |
| Dependency vulnerability scanning | Dependabot, Snyk, WhiteSource |
| Secrets management | Azure Key Vault, GitHub Secrets |
| Testing | Jest, NUnit, Postman (with secure data), DAST tools |
| Feature flagging / Beta testing | LaunchDarkly, Azure App Configuration, GitHub Feature Flags |

---

### Continuous improvement

Security is not static. Teams should regularly:

- **review and iterate** on security practices as the product and context evolve
- **refactor** to reduce complexity and risk as systems grow
- **embed security champions** to promote awareness and challenge assumptions
- **promote learning**, not blame, when addressing defects or risks.