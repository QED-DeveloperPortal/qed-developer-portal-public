---
title: How to test the iOS accessibility
author: sushma-hazari
categories: [Public]
classification: Opinion
tags: [mobiles,opinion]
date: 2024-08-29 01:58:13 
updatedBy: sushma-hazari
updated: 2024-08-30 06:01:38 
likes: 0
---

Testing accessibility on iOS is essential for creating apps that are inclusive and user-friendly for everyone, including those with disabilities. This process involves evaluating how well an app integrates with iOS’s accessibility features, such as VoiceOver, AssistiveTouch, and color contrast adjustments. By thoroughly testing these aspects, developers can identify and address potential barriers that might prevent users with visual, auditory, or motor impairments from fully engaging with the app. Ensuring strong accessibility not only helps meet legal requirements but also improves the app’s usability and expands its reach to a broader audience.

**Voice Over**: the screen reader for all Apple devices (iPhone, iPad, MacOS). It allows you to vocalize all the (useful) information present on the screen. It's an essential tool for blind and visually impaired people.

**Switch control**: this option allows the control of the phone with an external contactor, head movements, or even sounds. This tool is mainly used by people with motor disabilities who can't perform touchscreen gestures.

**Keyboard navigation**: enable this feature to use your phone with an external keyboard (usually via Bluetooth). It's useful for people who have difficulties using the touch screen due, for example, to motor impairment.

**Voice control**: option to control a phone only with the voice. It's essential for people who cannot physically interact with the device or an external contactor.

**Larger Text size**: increase text size, only useful with applications that manage this option.

***
#### **Getting started with accessibility options #**

**VoiceOver #**

Navigating with the screen reader is not always easy when you are starting, but a few simple basic gestures allow you to navigate within an application.

A detailed description of these actions is available on the following page: [Guide to Testing iOS Accessibility with VoiceOver](https://a11y-guidelines.orange.com/en/mobile/ios/voiceover/.)

By using VoiceOver, you can verify that all the essential information for understanding and navigation is rendered by the screen reader, including:

1. Interactive elements (buttons, links, checkboxes, etc.),
2. The status of the elements (checked or not, selected or not, unfolded or not, etc.),
3. The page titles must be read to allow users to be informed of a screen change and understand the context,
4. Content changes or temporary messages must also be read (alerts, errors, messages, etc.),
5. The consistency between VoiceOver reading order and the visual order of information presentation.

**Switch Control #**

Using the Switch Control allows you to mainly check: the focus order and the accessibility of interactive elements.

1. Enable Switch Control.
3. The focus is then displayed and begins to move from one container to another (for example: the header, the main view, the navigation bar, etc.).
5. To make the focus move on the different interactive elements inside a container, simply tap once when the focus comes to that container.
7. Then an additional tap will bring up the possible interaction options with each element having the focus (tap, scroll up/down, drag, etc.).

**Keyboard navigation #**

It is possible to use your phone only with an external keyboard.

1. Connect a keyboard to the phone.
3. Enable "Full Keyboard Access" option.
5. Now, all features available by touch gestures should also be operable with the keyboard. Navigating is similar to a desktop keyboard, **TAB** key to move forward, **SHIFT+TAB** to go back, **SPACE** to activate an element. 
7. Keyboard navigation also allows you to check that the navigation order is consistent.
8. If the focus is not visible enough, it is possible to increase its contrast in the option settings.

**Voice control #**

When "Voice Control" is enabled, you can say commands like:

1. "Return to home screen"
2. "Touch **item name**"
3. "Open **app name**"
4. "Turn up the volume"
By default, element names are superimposed. Also, for an application to be controllable in this way, the interactive components must have a simple and consistent accessible name (in particular in the case of a link image or button image without a visible label).

**Larger text #**

1. Increase the text size using the shortcut configured above.
2. One can increase text up to 310%, but accessibility recommendations require a correct display up to 235%.
3. If the application has been designed to support enlargement (Dynamic Type), then the texts will be correctly rendered, readable, and without loss of information (no truncated text or superposition)

**Dark mode #**
  As the dark mode is used more and more, so it's strongly recommended to test your    application by activating “dark mode”.

1. Go to Settings > Display & Brightness (or directly from Control Centre).
2. Check that all texts and components are visible and meet the expected contrast levels.


***

**How to Test Accessibility with an iPhone #**

***Turn on VoiceOver #***

Go to Settings > Accessibility > VoiceOver

There is a toggle to turn VoiceOver on/off at the top of the VoiceOver menu. When you turn VoiceOver on the gestures that you use to navigate your iPhone will change.
**

**Orient to VoiceOver #**

***Change How Fast VoiceOver Talks***

Go to Settings > Accessibility > VoiceOver > Speaking Rate 

Choosing a slower speaking rate can help with comprehension as you listen during testing.

**Try VoiceOver Practice #**

iPhones have a practice mode where you can practice using the different gestures needed to use VoiceOver. Turn on VoiceOver. Tap VoiceOver Practice, then double-tap to start. Follow the instruction provided in the practice mode.

***Basic Testing Gestures #***

* Use swipe gestures to move forward or backward through all page elements.
* Screen reader should announce each element and relevant text on the page.
* Double tap to activate links or buttons

Left to move backward, Right to move forward

**Now, Let's Test!**

1. Is all the text accessible to the screen reader and read aloud?
2.  Are elements read in a logical order that follows the visible page structure?**
4. Do the names of items that you hear match the visual text? 
6.  Can interactive elements (like links and forms) be activated and used?
8.  Is any content being skipped that should be read?
11. Is any content being read that is visually hidden?


**Use the Rotor to test specific elements**
***Open the Rotor #***

1. Turn on VoiceOver 
1. Rotate two fingers on your screen as if you are turning a dial 
2. If you prefer to use one finger on each hand then simultaneously drag up with one finger and down with another 
3. Select the rotor option (headings, buttons, landmarks) you would like to test from the rotor menu. 
4. If you don’t see the element type you want you may need to set the rotor options (see "Set the Rotor Options") 

**Set Rotor Options #**

Go to Settings > Accessibility > VoiceOver > Rotor

Select “Rotor” to show a list of elements that may be included in the rotor menu. Make sure the elements you plan to test are all selected. We recommend selecting: “Headings”, “Links”, “Landmarks” and “Form Controls”.

**Gestures to navigate by element**

1. Use swipe gestures to move forward or backward through your chosen page element.
2. The screen reader should announce each element and relevant text on the page.
3. Double tap to activate links or buttons
Up to move to previous instance, Down to move to next instance

**Test with gestures #**

2. Choose the element type.
3. Use up or down swipe gestures to move forward and backward through that particular element type. 
4. Double tap to activate links or buttons.
The screen reader should announce all the elements of the selected type present on the page and their relevant text


***

Further reading: 

* Developer Apple (n.d), [Testing system accessibility features in your app](https://developer.apple.com/documentation/accessibility/testing-system-accessibility-features-in-your-app), accessed 30 August 2024
* TEDx Talks (n.d), [Accessible tech makes better tech for everyone](https://www.google.com/search?q=ted+talk+accessibilty+for+mobile+app&sca_esv=77634acc5d5dc9b4&sca_upv=1&rlz=1C1GCEB_enAU1040AU1040&biw=1366&bih=641&sxsrf=ADLYWIIjAmVJn5uo4Kyy5x82c4f-RFCNBg%3A1724992131175&ei=g0rRZti6Cuje2roPy6-bgAQ&ved=0ahUKEwiYiOC58JuIAxVor1YBHcvXBkA4ChDh1QMIEA&uact=5&oq=ted+talk+accessibilty+for+mobile+app&gs_lp=Egxnd3Mtd2l6LXNlcnAiJHRlZCB0YWxrIGFjY2Vzc2liaWx0eSBmb3IgbW9iaWxlIGFwcDIHECEYoAEYCjIHECEYoAEYCjIHECEYoAEYCjIHECEYoAEYCkiUalCUC1ihZXACeAGQAQCYAYUDoAHGTKoBBjItMjguOLgBA8gBAPgBAZgCJaAC_EuoAhHCAgoQABiwAxjWBBhHwgIHECMYJxjqAsICFBAAGIAEGOMEGLQCGOkEGOoC2AEBwgIKECMYgAQYJxiKBcICBBAjGCfCAgsQABiABBiRAhiKBcICEBAAGIAEGLEDGEMYgwEYigXCAgsQABiABBixAxiDAcICERAuGIAEGLEDGNEDGIMBGMcBwgIKEAAYgAQYQxiKBcICEBAuGIAEGLEDGEMYgwEYigXCAg0QLhiABBixAxhDGIoFwgIKEC4YgAQYQxiKBcICExAuGIAEGLEDGEMYgwEY1AIYigXCAggQLhiABBixA8ICHxAuGIAEGLEDGEMYgwEYigUYlwUY3AQY3gQY4ATYAQLCAg0QABiABBixAxhDGIoFwgIEEC4YA8ICBRAAGIAEwgIKEAAYgAQYFBiHAsICBxAAGIAEGArCAgYQABgWGB7CAggQABgWGB4YD8ICCxAAGIAEGIYDGIoFwgIHEAAYgAQYDcICBhAhGBUYCsICCBAhGBUYChgNwgIEECEYCpgDB4gGAZAGCLoGBggBEAEYAboGBggCEAEYFJIHCDIuMC4yNi45oAew_gE&sclient=gws-wiz-serp#fpstate=ive&vld=cid:f616d24e,vid:2115c0GL4a8,st:0), accessed 30 August 2024
* Appt (n.d), [ Automated accessibility testing of Android and iOS apps](https://appt.org/en/articles/automated-accessibility-testing-android-ios-apps), accessed 30 August 2024