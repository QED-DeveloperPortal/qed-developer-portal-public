---
title: "DevSecOps from CM1"
author: jeny-amatya-qed
categories: [public]
tags: [auto-import, contentmanager]
date: 2024-07-23 22:25:18
likes: 0
imported: True 
import-source: "ContentManager"
import-reference: "1234"
---

# DevSecOps
 
## A Culture of Workflow Cyber Security
 
### Executive Summary
 
In today's digital landscape, software security is not just a necessity but a cornerstone for safeguarding critical systems and sensitive data against malicious threats. It plays a vital role in maintaining the integrity, availability, and confidentiality of information, which are crucial for the trust and safety of individuals and organisations alike.
 
Embracing a proactive approach, DevSecOps (Development, Security, and Operations) stands out as a pivotal strategy for the swift delivery of secure, high-quality digital services. This approach, which integrates security practices from the very beginning of the development and operations lifecycle, is instrumental in facilitating early threat detection. Such early integration significantly reduces risks and costs associated with cybersecurity threats. Moreover, the inherent automation within DevSecOps accelerates development processes while ensuring robust security through continuous monitoring.
 
This document encompasses a thorough market scan, comparing various solutions to tailor DevSecOps to the department’s specific needs. The aim is to craft a practical and cost-effective approach to cybersecurity, adapting to the unique challenges and requirements faced in today's rapidly evolving cyber landscape.
 
### Introduction to DevSecOps
 
In the dynamic world of software development, the intersection of speed, innovation, and security is where DevSecOps finds its significance. DevSecOps, an abbreviation for Development, Security, and Operations, represents a paradigm shift in how organisations approach software development and cybersecurity.
 
Traditionally, security has often been a siloed aspect of the development process, typically addressed at the end of the software development lifecycle (SDLC). This approach, while structured, tends to delay product releases and may overlook evolving security threats that arise during the development process. DevSecOps disrupts this model by embedding security at every stage of the SDLC, starting from initial design to deployment and operations.
 
This integration is not merely about tooling; it's a cultural shift. DevSecOps fosters a 'Security as Code' culture, where security is treated as an integral part of the development process, not as an afterthought. It encourages continuous collaboration between development, security, and operations teams. This collaborative approach ensures that security considerations are not just tacked on but are an intrinsic part of the development process.
 
One of the key tenets of DevSecOps is the 'shift left' principle. It emphasises the need to address security early in the development cycle. By shifting left, security testing and compliance monitoring happen in tandem with coding, significantly reducing the likelihood of security issues in the released product.
 
The benefits of DevSecOps are multifaceted. It enables organisations to rapidly deploy secure and compliant software, reduces the cost and time involved in addressing security issues, and enhances overall software quality. Perhaps most critically, it helps in managing and mitigating the risks in a landscape where cybersecurity threats are increasingly sophisticated and pervasive.
 
In summary, DevSecOps represents a strategic and necessary evolution in the approach to software development. By integrating security practices into every phase of the SDLC, it allows organisations to balance the need for speed and innovation in software development with the imperative of maintaining robust cybersecurity measures.
 
### Current State Analysis
 
The current security landscape in software development is marked by rapidly evolving risks and technologies. This dynamic environment demands a security approach that is both robust and proactive. Our existing security framework, however, shows several shortcomings:
 
- High-level architectural reviews: These abstract reviews often miss crucial details. They lack depth in analysing the inner workings of software, which can lead to undetected vulnerabilities lurking beneath the surface.
- Use of open-source libraries: While open-source libraries nested within closed-source components offer numerous benefits, they also pose significant security risks. These risks are often overlooked, and ironically, attempts to secure these libraries by ‘freezing’ versions can lead to further vulnerabilities due to lack of continual patching.
- Peer code reviews: Although peer reviews are essential for collaboration and knowledge sharing, they frequently fall short in identifying complex security issues. This is often due to a lack of specialised security expertise among peers.
- Annual penetration tests: These often expensive and time-consuming tests do not cover the entire spectrum of code vulnerabilities. In a fast-paced development world, a year is a long time, and software can become exposed to new risks between these annual checks. Moreover, many of the existing security tools were developed before the emergence of current technological trends.

Given these challenges, there is an urgent need to upgrade the tools and methodologies used by developers. This upgrade is essential for ensuring the safety and security of software in an environment where threats are continuously evolving and increasing in complexity.
 
### DevSecOps vs Traditional Cyber Security
 
#### Keys for a Holistic DevSecOps Approach

- Security in infrastructure as code: Ensuring secure infrastructure configurations from the start.
- Secret management: Securely manage and store secrets and credentials.
- Pre-commit hooks: Enforce code quality and security standards before code is committed to the repository.
- Source composition analysis: Scan and manage open-source dependencies for vulnerabilities.
- Static application security testing (SAST): Analyse the source code for security vulnerabilities.
- Dynamic application security testing (DAST): Test applications in runtime for security issues.
- Web application firewall (WAF): An additional layer of protection for web applications by filtering malicious traffic.
- Container security: Scan container images for vulnerabilities.
- Continuous integration/continuous deployment (CI/CD) security: Integration of security checks within the CI/CD pipeline.
- Threat modelling: Practices and tools for identifying and addressing security threats in the design phase.
- Security orchestration, automation, and response (SOAR): Automating incident response and remediation.
- Security information and event management (SIEM): Real-time monitoring and threat detection.
- Identity and access management (IAM): Managing user access and permissions securely.
- Runtime application self-protection (RASP): Protection against runtime attacks.
- Secure code review tools: In-depth code review and vulnerability detection.

### Strategic Pivot to DevSecOps
 
Transitioning to a DevSecOps model requires a strategic pivot that encompasses not just the adoption of new tools and technologies but also a shift in organisational culture and processes. This strategic pivot should be executed through several key steps:

1. **Assessment and planning:** Begin by conducting a thorough assessment of the current security practices and infrastructure. This should include identifying the gaps in the existing system and understanding the specific needs of the organisation. Based on this assessment, develop a detailed plan that outlines the objectives, timeline, and key milestones for the transition to DevSecOps.
2. **Cultural shift and training:** DevSecOps demands a cultural shift where security is integrated into every aspect of development and operations. This involves training and sensitising the development, operations, and security teams about the importance of security in the development lifecycle. It's crucial to promote a culture of collaboration and shared responsibility for security.
3. **Integration of security into the SDLC:** Security practices should be 'shifted left', meaning they are introduced earlier in the software development lifecycle. This includes integrating security tools and practices into the Continuous Integration/Continuous Deployment (CI/CD) pipelines and ensuring that security checks are a part of the regular development process.
4. **Automation and continuous monitoring:** Implement automation tools for security testing, monitoring, and compliance. Automation is key in DevSecOps to ensure continuous security without slowing down the development process. Continuous monitoring of the infrastructure and applications for any security threats should be established.
5. **Feedback loops and continuous improvement:** Establish feedback mechanisms for continuous learning and improvement. Security is an evolving field, and the DevSecOps approach should be flexible and adaptable to accommodate changes in the security landscape.