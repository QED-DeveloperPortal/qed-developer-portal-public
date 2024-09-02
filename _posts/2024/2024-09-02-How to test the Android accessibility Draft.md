---
title: How to test the Android accessibility Draft
author: sushma-hazari-qed
categories: [Public]
classification: Opinion
tags: [mobiles,opinion]
date: 2024-09-02 05:00:31 
updatedBy: 
likes: 0
---

**Android's Accessibility Features**


***TalkBack***

TalkBack is Android's built-in screen reader. When TalkBack is on, users can interact with their Android device without seeing the screen. This is great for those who suffer from vision impairments that make it difficult to navigate applications or websites.

*What to test for?*

1. Are all the elements properly labeled allowing TalkBack to read them to the user?
2. Do notifications or popup windows read to the user?
3. Can users swipe through a page to navigate and explore every element on the page?
4. Are users able to use the double-tap feature to randomly explore the application or pick specific elements to explore?

[How to Test Accessibility with Android TalkBack](https://accessibility.huit.harvard.edu/test-android-talkback)

***Switch Access***

Switch Access lets users interact with Android devices using a switch instead of the touch screen. There are several kinds of switches but a simple example is the volume down button and the volume up button.

*What to test for?*

1. Are users able to navigate through the application easily?
2.  If there are text or other inputs, can you add and edit content easily?
3. Are items highlighted only if you can perform an action with them?
4. Are all functionality available through selectable controls or custom actions within Switch Access?
5. Does the spoken feedback for each element convey its content or purpose appropriately?

***BrailleBack (Extra Accessibility Feature)***

Google's BrailleBack is an actual mobile application that enables users to type text using a Braille display on Android devices via Bluetooth. This service works directly with TalkBack to offer users both speech and Braille supports.

*What to test for?*

1. Is the name of the application or website correctly displayed using the connected Braille device?
2. Can the user or tester properly navigate the site or application using the connected Braille device?
3. Are any text or prompts on the application or site correctly displayed on the connected Braille device?

Other important ways to test application or mobile website include checking to see that the application is completely compatible with a screen magnifier as well as increased font sizes. Testing color schemes is also recommended to ensure the color pattern on a webpage or application does not act as a barrier to people who are color blind. 

***
Further reading :
* Developer android (n.a), [ Google Developers Training team](https://developer.android.com/codelabs/basic-android-kotlin-compose-test-accessibility#0), accessed September 2 2024
* DigitalA11y(n.a), [Android accessibility checklist]( https://www.digitala11y.com/android-accessibility-testing-checklist/), accessed September 2 2024
* Developer android(n.a), [Test your accessibility](https://developer.android.com/guide/topics/ui/accessibility/testing), accessed September 2 2024



