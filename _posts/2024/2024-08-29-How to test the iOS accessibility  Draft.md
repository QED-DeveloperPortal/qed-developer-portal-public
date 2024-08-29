---
title: How to test the iOS accessibility  Draft
author: sushma-hazari
categories: [Public]
classification: Opinion
tags: [mobiles,opinion]
date: 2024-08-29 01:58:13 
updatedBy: 
likes: 0
---

#### **Performing Accessibility Testing on iOS?**


Generally, an accessibility test can be executed in a number of ways, the first being through automated testing. 

**Automated Testing & Manual Testing**

Overall, automated testing is a great starting point when it comes to accessibility as it makes it possible to test hundreds of pages very quickly in order to get a general idea of the accessibility of a website or application. Automated accessibility testing is also well suited for evaluating features that do not require the critical eye of a tester like "alt" attribute. However, automated testing is limited in its ability to find every bug or anomaly that makes a website or application less accessible. 

The second way to execute accessibility testing is through the use of manual testers, which involves evaluating an application or a website on real devices paired with assistive technology software or hardware. Although slower than automated testing, manual testing goes beyond the surface level of accessibility features such as the appropriateness of "alt" tags. Overall, manual accessibility testing provides a greater human-driven accessibility assessment. 

**Test Coverage**

Like any QA test, accessibility tests for mobile websites and applications should account for the variety of screen sizes and operating systems used today. 

For the purposes of this article, we will focus on manual testing using accessibility tools or features built into Apple's iOS. 

**iOS Accessibility Features :**

**VoiceOver**

VoiceOver is a screen reader that interacts with objects in your applications so users can drive the interface even if they can’t see it. With VoiceOver, all the content on the screen can be read aloud to the user enabling them to use the application or website. 

When testing, the standard approach is to ensure that all content elements (text, links, form fields, tables, and more) are accessible or compatible with this feature. 

However, what makes VoiceOver important is its ability to provide a variety of visually impaired users with a comparable experience to non-visually impaired users. 

Here are additional questions to ask when testing:  

* In rotor mode, can users navigate the page based on the type of element, for example, links, headings, text fields, images, etc. 
* Are all the elements of the page labeled as “accessible”? 
* Are “accessibility labels” marked and do they provide a short description of the label? For example, “New playlist”. 
* Do accessibility labels begin with a capital letter and are not ended in a period? This is important for ensuring that accessibility labels are read by VoiceOver with the proper inflection. 
* Do accessibility hints provide a brief description of what the element does? Like accessibility labels, hints should begin with a capital letter, but they should end in a period. Also, they should avoid using the name or type of the control. For example, “Create will create a playlist” sounds less natural when read aloud. 
* Do accessibility traits provide meaningful information to the user to help them better understand the element?

**Zoom**

Zoom is a full-screen magnifier that scales content up to 200 percent to help visually impaired users. When paired with Magnification, the screen can be scaled up to 500 percent. Using Zoom, you can test your application to see how it appears while it is magnified. 

**Switch Control**

Switch Control gives users the ability to use their iPhones and navigate the different content and elements on a website or application with alternative controls. With Switch Control, users with limited mobility can navigate and make selections using by tapping the screen, moving their head in front of the selfie camera, or by pressing adaptive switches. Testing your application with this element will uncover bugs that can prevent users from navigating and using the application or mobile website.  

