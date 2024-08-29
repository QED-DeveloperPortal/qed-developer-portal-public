---
title: Testing mobile apps for accessibility
author: sushma-hazari-qed
categories: [Public]
classification: Official
tags: [mobiles,opinion]
date: 2024-08-28 01:58:50 
updatedBy: sushma-hazari
updated: 2024-08-29 05:30:29 
likes: 0
---

Mobile accessibility testing ensures that mobile apps are accessible to users of all abilities. With the rise of mobile usage, it's crucial for apps to be designed with inclusivity in mind, allowing everyone to interact seamlessly. Accessibility testing focuses on identifying barriers that might prevent users with visual, auditory, motor, or cognitive impairments from fully using the app. By following established guidelines, such as the Web Content Accessibility Guidelines (WCAG), developers can create apps that offer a satisfying user experience for everyone.

***
#### **Accessibility tools provided by Android/iOS :**

**For iOS:**

**Accessibility Inspector**: Integrated into Xcode, this tool provides detailed insights into your app's accessibility features. It allows you to review accessibility traits and labels, helping you identify areas that need improvement.

**Xcode accessibility features**: Xcode offers several features for testing accessibility, such as simulating different accessibility settings and viewing accessibility properties of UI elements. This helps ensure that your app performs well under various accessibility configurations.

**TestFlight**: Apple’s beta testing service enables you to distribute your app to real users, including those who rely on assistive technologies. Gathering feedback from these users can provide valuable insights into how accessible your app is in real-world scenarios.

**Voice Control**: This feature allows users to control their device using voice commands. Testing your app with Voice Control helps ensure that it supports voice-based interactions effectively.

**Switch Control**: Designed for users who interact with their device using adaptive hardware, Switch Control helps you test how well your app accommodates switch devices and other assistive technologies.

**For Android:**

**TalkBack**: Android’s built-in screen reader that reads out on-screen content. It helps you assess how well your app supports screen readers and ensures that visually impaired users can navigate your app effectively.

**Accessibility Scanner**: An Android app that provides actionable recommendations to improve accessibility. It identifies potential issues with your app’s UI and suggests ways to make it more accessible.

**Android Studio accessibility test framework**: Integrated into Android Studio, this tool allows you to run automated accessibility tests and review detailed reports on how your app performs against accessibility guidelines.

**Developer options accessibility settings**: Android’s developer options include various settings for simulating different accessibility features, such as magnification gestures and colour inversion. These settings help you test how your app behaves under various accessibility configurations.

**Google accessibility scanner**: A tool within Android Studio that analyses your app and provides suggestions for improving accessibility. It helps you identify areas where your app could be more inclusive.

**Voice Access**: An accessibility service that allows users to control their device using voice commands. Testing your app with Voice Access ensures that it supports voice-based interactions effectively.

**Switch Access**: Designed for users who interact with their device using switch devices, Switch Access helps you test how well your app accommodates adaptive hardware and other assistive technologies.


***
#### **Mobile accessibility testing checklist**

**Screen reader support**
* Ensure interactive elements are announced with appropriate labels.
* Check for proper reading order of content.

**Colour contrast**
* Ensure sufficient contrast between text and background colours.
* Verify that colour is not the only means of conveying information.

**Text size and scalability**
* Test text resizing to ensure readability when scaled up.
* Verify that text remains legible and does not overlap.

**Keyboard and focus navigation**
* Check that all interactive elements are reachable and focusable using a keyboard or external device.
* Ensure that the focus order is logical and intuitive.

**Touch target size**
* Verify that touch targets (buttons, links) are large enough to be easily tapped.
* Ensure adequate spacing between touch targets to avoid accidental selections.

**Voice control and commands**
* Test voice commands to ensure that all app functions can be accessed using voice control.
* Verify that voice feedback is clear and accurate.

**Alternative text for images**
* Ensure all images have descriptive alternative text.
* Verify that decorative images are correctly marked as such.

**Accessibility labels and hints**
* Check that all interactive elements have meaningful labels.
* Verify that hints and instructions are provided where needed.

**Error handling and notifications**
* Ensure that errors are announced clearly by screen readers.
* Verify that users receive accessible notifications and error messages.

**Switch access**
* Test how well the app supports switch devices and other adaptive hardware.
* Ensure that all functions are accessible using switch access.

**Custom controls and widgets**
* Verify that custom controls and widgets are accessible and provide appropriate feedback.
* Ensure they are compatible with screen readers and other assistive technologies.

**Gestures and multi-touch**
* Ensure that gesture-based interactions are accessible and can be performed using alternative methods if needed.
* Verify that multi-touch functionality is supported and intuitive.

**Language and localisation**
* Check that all text is properly localised and translated.
* Ensure that accessibility features are supported in all languages the app is available in.

**Testing with real users**
* Conduct testing with users who have disabilities to gather real-world feedback.
* Address any issues identified during user testing.

***

**Further reading:**

* Browser Stack, [Accessibility Testing for Mobile Apps Guide BrowserStack](https://www.browserstack.com/guide/accessibility-testing-for-mobile-apps), accessed 28 August 2024
* Testsigma, [Mobile Accessibility Testing Blog Testsigma](https://testsigma.com/blog/mobile-accessibility-testing/) accessed 28 August 2024
* DigitialA11Y, [Free Mobile Accessibility Testing Tools DigitalA11Y](https://www.digitala11y.com/free-mobile-accessibility-testing-tools), accessed 28 August 2024