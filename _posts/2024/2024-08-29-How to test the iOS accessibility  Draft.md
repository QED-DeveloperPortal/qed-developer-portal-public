---
title: How to test the iOS accessibility  Draft
author: sushma-hazari
categories: [Public]
classification: Opinion
tags: [mobiles,opinion]
date: 2024-08-29 01:58:13 
updatedBy: sushma-hazari
updated: 2024-08-30 01:10:57 
likes: 0
---

**Presentation of the main options #**

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