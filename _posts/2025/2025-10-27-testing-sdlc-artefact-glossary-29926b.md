---
title: "Testing SDLC Artefact Glossary"
slug: "testing-sdlc-artefact-glossary-29926b"
author: jeny-amatya-qed
categories: Public
classification: Public
tags: [about]
date: 2025-10-27 02:59:05 
likes: 0
---

---
index: true
---

# SDLC Artefact glossary

| **Artefact** | **Required for Type 1 Release** | **Required for Type 2 Release** | **Required for Type 3 Release** |
| --- | --- | --- | --- |
| SDLC Track Artefacts |     |     |     |
| Information Security Assessment | ✓   | ✓\* | ✓\* |
| Cloud Assessment Report <sup>[\[1\]](#footnote-1)</sup> | ✓   | ✓   | ✓   |
| Release Risks/Issue Register | ✓   | ✓   | ✓   |
| Needs Stage Artefacts |     |     |     |
| Idea Definition Document/Problem or Need Statement | ✓   |     |     |
| Concept Stage Artefacts |     |     |     |
| Operational Concept <sup>[\[2\]](#footnote-2)</sup> | ✓   |     |     |
| Terms of Reference for Project or Application Governance Board | ✓   |     |     |
| Project Brief | ✓   |     |     |
| Preliminary Business Requirements Specification (BRS) | ✓   |     |     |
| Requirements Stage Artefacts |     |     |     |
| System Requirements Specification Document (SRS) <sup>[\[3\]](#footnote-3)</sup> | ✓   | ✓   |     |
| Analysis And Design Stage Artefacts |     |     |     |
| Logical Solution Architecture<sup>[\[4\]](#footnote-4)</sup> | ✓   | ✓   | ✓   |
| Physical Solution Architecture | ✓   | ✓   | ✓   |
| Design Review Report <sup>[\[5\]](#footnote-5)</sup> | ✓   | ✓   | ✓   |
| Implementation Stage Artefacts |     |     |     |
| All codes and scripts fully finalized and checked into DET’s selected source control environment. | ✓   | ✓   | ✓   |
| Test Summary Report <sup>[\[6\]](#footnote-6)</sup> | ✓   | ✓   | ✓   |
| Code Review Report <sup>[\[7\]](#footnote-7)</sup> | ✓   | ✓   | ✓   |
| Deployment Plan | ✓   | ✓   | ✓   |
| Enterprise Integration Platform Engagement <sup>[\[8\]](#footnote-8)</sup> | ✓   | ✓   | ✓   |
| Accessibility Review Report <sup>[\[9\]](#footnote-9)</sup> | ✓   | ✓   | ✓   |
| Quality assurance certificate | ✓   | ✓   | ✓   |
| Test Stage Artefacts |     |     |     |
| Acceptance Test Summary Report | ✓   | ✓   | ✓   |
| Secondary Acceptance Test Summary Report (for releases with high levels of risk) <sup>[\[10\]](#footnote-10)</sup> | ✓   | ✓   | ✓   |
| Production Readiness Certificate<sup>[\[11\]](#footnote-11)</sup> | ✓   |     |     |
| Operational Support Plan | ✓   | ✓   | ✓   |
| Deployment Stage Artefacts |     |     |     |
| Vulnerability Test Report <sup>[\[12\]](#footnote-12)</sup> | ✓   | ✓   | ✓   |
| Load Test Report | ✓   |     |     |
| Release Completion Report <sup>[\[13\]](#footnote-13)</sup> | ✓   | ✓   | ✓   |
| Maintenance Stage Artefacts |     |     |     |
| System Release Schedule <sup>[\[14\]](#footnote-14)</sup> | ✓   | ✓   | ✓   |
| Retirement Stage Artefacts |     |     |     |
| Retirement Report | ✓   | ✓   | ✓   |

### Type 1 release
This track starts from the Needs stage and ends at the Maintenance stage and accordingly, such releases will require the artefacts and controls highlighted in all the included stages.

### Type 2 release
This track starts from the Requirements stage and ends at the Maintenance stage and accordingly, such releases will require the artefacts and controls highlighted in all the included stages.

### Type 3 release
This track starts from the Analysis and Design Stage and ends at the Maintenance stage and accordingly, such releases will require the artefacts and controls highlighted in all the included stages.

### Footnotes

*Optional depending on whether or not data models have changed during the development of the release.
  
1. Only applicable to releases with cloud-based components being used for the first time [↑](#footnote-ref-1)
2. Optional [↑](#footnote-ref-2)
3. For development activities delivering integration middleware, this artefact may be different from a System Requirements Specification (e.g. Enterprise Integration Platform (EIP) may use an Engagement artefact that wraps requirements) [↑](#footnote-ref-3)
4. Not applicable for Integration Middleware [↑](#footnote-ref-4)
5. The report can be extracted from application life cycle management tools, if used. [↑](#footnote-ref-5)
6. The report can be extracted from application life cycle management tools, if used. It should cover unit tests, integration tests, system tests and regression tests. [↑](#footnote-ref-6)
7. The report can be extracted from application life cycle management tools, if used. [↑](#footnote-ref-7)
8. Not applicable for development activities delivering Integration Middleware. Only applicable to solutions with system-to-system integration [↑](#footnote-ref-8)
9. Not applicable to Integration Middleware. Only applicable to solutions/releases with a user interface [↑](#footnote-ref-9)
10. Only applicable to releases with a high level of risk [↑](#footnote-ref-10)
11. A Production Readiness Certificate may be dependent on the results of Vulnerability and Load Tests that may be performed at later stages. [↑](#footnote-ref-11)
12. Only applicable to cases defined under "Vulnerability Testing Applicability Criteria" [↑](#footnote-ref-12)
13. This report may be extracted from application life cycle management or release management tools (e.g. Service Now) [↑](#footnote-ref-13)
14. This schedule may be managed and extracted from application life cycle management tools. [↑](#footnote-ref-14)
