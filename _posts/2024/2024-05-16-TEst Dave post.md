---
title: TEst Dave post
author: jeny-amatya-qed
categories: [Public]
tags: [test]
date: 2024-05-16 03:14:16 
likes: 0
---

This article outlines the software development practice framework to be followed by Department of Education for the development of software solutions to meet organizational objectives with respect to the development, maintenance and management of software products

***Principles:*** The following principles have been adapted from various resources

<dl>
  <dt>General</dt>
    <dd>- Focus on TCO rather than project costs</dd>
    <dd>- Build trust both within teams and with other stakeholders</dd>
  <dt>Solution Design</dt>
    <dd>- Simplicity</dd>
    <dd>- Modularity</dd>
    <dd>- Robustness</dd>
    <dd>- Scalability</dd>
    <dd>- Build in Security</dd>
    <dd>- Performance Optimisation</dd>
  <dt>Code Design</dt>
    <dd>- Avoid Repetition</dd>
    <dd>- Readability - Code for Humans</dd>
    <dd>- Don't over-engineer</dd>
    <dd>- Continuous Feedback & Iteration</dd>
    <dd>- Automate Testing</dd>
</dl>

***Objectives:*** To develop high-quality web applications efficiently by embracing Agile methodologies and leveraging Continuous Integration/Continuous Deployment pipelines.

More details and support can be found within the department’s Developer Portal

### Development Methodology
Software Development in the department leans towards two main methodologies:
* Scrum (for modules and simple products)
* SAFe (for complex Product Management) (Aspiring)

#### Scrum

Scrum is a highly rigorous software delivery methodology that focus on empirical data to support its outcomes. It focuses on continuous planning, using a pre-set cadence (usually 2 weeks), that allows it to adjust quickly to the ever changing and emerging software needs and reprioritisation that is part of every large complex organisation’s software environment. It does NOT follow a project mindset as projects tend to focus on large deliverables (months+) with preconceived ideas of scope, cost and schedules.
Scrum instead focusses on smaller improvements, that can be delivered quickly, but that can over time create large organisational change in an incremental fashion. It forces the organisation to focus on business need and priority to delivery business values and outcomes; and shifts the focus away from monolithic projects and funding. 

However, for Scrum to be successful it requires a couple of things to be in place as these underpin how Scrum operates. 

A scrum team should be stable and long lived. This means the team should be set up with the intent that it remains together for years allowing it to build business knowledge in the product area they are responsible for. In Scrum teams are not formed to service a project and then disbanded/reformed for the next project, the team remains in place and stable with work flowing into the team. The advantages are:
* Team cost is a known – a team of 10 costs the same sprint after sprint.
* Teams output can be assessed empirically based on their past performance, a long-lived team working at a sustainable pace will produce the same volume of work +/- 20% consistently sprint after sprint.
* Estimations become more accurate and can be more accurately assessed and planned. 
* Pricing an enhancement has greater accuracy and confidence. 

For Scrum to be efficient, a continuous Pipeline of work needs to be in place. This pipeline of work will contain new enhancement as identified by the business to provide new functionality (traditionally delivered via a project), defect resolution, and tech debt removal.

Note all IT work is considered to have business value and is in the same pipeline prioritised against each other. The reason for this is that if a piece of work has no business value it should not be performed. 

The Product Owner (PO) provides guidance regarding prioritisation and answer business requirement questions. The functions this role performs are critical to Scrum as the PO knows the product at a high level and can align the organisational priorities and strategic goals with the software changes required to support them. The PO also knows the product at a detailed level so they can accurately prioritize strategic enhancements against the need to resolve defects and tech debt. For a large complex platform, this role may be filled by multiple people, but they need to work closely together to remain functional. The PO is also the source of all requirements, once again for a complex product they are likely to be assisted here by BA and Tech Analysists who are across the nitty gritty of the product at a functional level. 

The Scrum Master helps drive improvement to the teams. They should be the expert on all things Scrum and help identify places for improvement to remove bottlenecks.

#### Aspiring to SAFe
SAFe (the Scaled Agile Framework) provides many of the controls large organisations are used to having in place which are not part of Scrum. But unlike ITIL Agile and Prince2 Agile, it is designed to complement agile delivery and Scrum specifically. It reintroduces Projects and Project Management, but instead of these being the foundations of the methodology, SAFe is based on Scrum and how it works. 

The SAFe framework then introduces process on how to manage multiple Scrum teams within a large organisation so they are working in a coordinated and collaborative fashion. It provides mechanisms to ensure priorities across teams all come from the same place, not isolated siloes chasing their own outcomes. These mechanisms provide support for how projects approach resources to complete their deliverables. No longer do projects decide what is important in isolation, but they need to do so in a collaborative fashion that considers the strategic needs of the organisation not the tactical need of each individual project. 

Projects need to approach teams to get their work completed providing better resource utilisation than the model of hoarding resources so they are available as and when you need them. For projects and project managers, how they deliver their work is very different, though they can continue to report in the old traditional ways. For the people doing the actual delivery work, regardless of the project, how they work using Scrum remains the same as the teams are stable. This approach is all about collaboration between teams, and is really useful for highlighting resourcing bottlenecks (e.g. solution architects, test automation) within an organisation.

### Processes and Best Practices

#### Planning and Estimation

*Detail the procedures for project planning, task estimation, and resource allocation. Include guidelines for creating project schedules, defining milestones, and managing dependencies.*

*The block below requires review, editing and formatting*

> Effective planning and estimation are crucial for successful software development projects. Firstly, it's essential to involve all stakeholders to gather comprehensive requirements and ensure alignment with project goals. Breaking down tasks into smaller, manageable units promotes clarity and accuracy in estimation. Utilizing historical data and leveraging the expertise of team members can enhance the accuracy of estimates. Additionally, employing agile methodologies allows for iterative planning and adjustment based on feedback, fostering adaptability in dynamic environments. Regularly revisiting and updating plans and estimates as the project progresses helps in maintaining alignment with evolving requirements and constraints. Continuous communication among team members and stakeholders is vital to address any discrepancies or changes promptly. Finally, fostering a culture of transparency and accountability cultivates trust and collaboration, leading to more reliable planning and estimation outcomes.
Several techniques can be employed to improve planning and estimation in software development:
Story Points: Utilize story points to estimate the relative effort required for completing user stories or tasks. This approach focuses on the complexity, uncertainty, and effort involved rather than specific time durations.
Planning Poker: Gather the development team to collectively estimate the effort required for each task using planning poker. This technique encourages discussion and consensus-building among team members, leading to more accurate estimates.
Three-Point Estimation: Use three-point estimation (optimistic, pessimistic, and most likely) to calculate a more realistic estimate by considering best-case, worst-case, and probable scenarios for task completion.
Historical Data Analysis: Analyze past project data to identify patterns and trends in task completion times and use this information to inform future estimates. This technique helps in making more informed decisions based on actual project experiences.
Expert Judgment: Leverage the expertise of team members and subject matter experts to provide insights and guidance during the estimation process. Experienced team members can offer valuable perspectives on the complexity and effort required for specific tasks.
Prototyping and Spike Solutions: Use prototyping or spike solutions to explore uncertainties and gather more information about complex or unfamiliar aspects of the project. This allows for better estimation by reducing ambiguity and identifying potential challenges early on.
By incorporating these techniques into the planning and estimation process, software development teams can enhance their ability to deliver projects on time and within budget while maintaining high-quality standards.


#### Development Environment(s)

*Specify the development tools, languages, and frameworks to be used. Outline the procedures for setting up a development environment, version control, and integration with continuous integration/continuous deployment (CI/CD) systems.*

#### Coding Standards

*Establish coding standards to ensure consistency and maintainability of code. Include guidelines for naming conventions, indentation, commenting, and code documentation.*

#### Code Review Process

*Define a code review process to catch errors early and promote collaboration. Specify the roles and responsibilities of reviewers, the frequency of reviews, and the tools used for code review.*

*Current state is a peer review, however there has in the past, and needs to be in the future a tool based code review to complement the peer reviews. This tool based review would look at key aspects of code quality, especially security*

#### Testing Practices

Because the department recognises that the landscape of software development is ever-evolving, we embrace both traditional and modern testing methodologies—from the meticulous precision of the V-Model to the dynamic adaptability of Agile and the efficiency of continuous integration/continuous deployment (CI/CD) pipelines.  

Regardless of the methodology, our quality-centric approach means that every piece of software we deliver meets the functional and performance expectations of our stakeholders.  

Details can be found in the Master Test Strategy (CM ref 10/14816)

#### Deployment & Release Management

*Describe the procedures for deploying software to different environments (development, testing, production). Specify the release management process, including versioning, rollback plans, and release notes.*

*Will probably feature things like
•	Establish a CD pipeline to automate the deployment process from staging to production environments.
•	Utilize containerization technologies like Docker for consistent deployment across different environments.
•	Implement blue-green or canary deployment strategies to minimize downtime and risk during deployments.*


More information is available in the Systems Development Lifecycle document (CM ref 16/180989)

#### Documentation

Documentation plays a pivotal role within any software development practice, serving as the backbone of knowledge sharing, transparency, and long-term sustainability. 

Comprehensive documentation acts as a guidebook, aiding developers in understanding the intricacies of the codebase, system architecture, and business logic. It serves as a vital communication tool, enabling seamless collaboration between team members, stakeholders, and future contributors. Moreover, documentation ensures continuity by preserving institutional knowledge, mitigating the risks associated with employee turnover or transitions between project phases. 

Clear and well-maintained documentation enhances the maintainability of software systems, facilitating troubleshooting, debugging, and future enhancements. 

The department utilises a blend of documentation methods and repositories, depending on the age and complexity of particular products. The goal is a transition of system documentation into Wikis within Azure DevOps. Each product may establish its own template/structure for Wiki’s to maximise knowledge sharing, retention and accessibility. 

#### Collaboration and Communication

A culture of collaboration and effective communication within the development teams, and their key stakeholders, is essential to success. 

Techniques such as pair programming and knowledge sharing is encouraged and all team members are encouraged to actively participate in Sprint ceremonies. 

Microsoft Teams and Azure DevOps are utilised to support collaboration, as is the Developer Portal

#### Continuous Improvement
 
*Aspirational: 
Encourage a culture of continuous improvement by regularly reviewing and updating the software development practice. Implement mechanisms for collecting feedback and learning from past projects.*

*Will likely contain some of the following:
•	Monitor application performance, usage metrics, and error logs in real-time.
•	Utilize tools like Prometheus, Grafana, or New Relic to gain insights into the application's health and performance.
•	Collect feedback from users, stakeholders, and team members to identify areas for improvement and prioritize future enhancements.*

#### Security Practices

*Integrate security practices into the development process. Define guidelines for secure coding, vulnerability assessments, and regular security audits.*

### Training and Skill Development

*Provide opportunities for ongoing training and skill development. Support team members in staying updated with the latest technologies and industry best practices.*
