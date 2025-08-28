---
title: "Mobile application standards"
slug: "mobile-application-standards-ca6843"
author: g-morton
categories: Public
classification: Public
tags: [standards,mobile]
date: 2023-07-03 13:20:33 
updatedBy: jeny-amatya-qed
updated: 2025-08-28 04:06:22 
likes: 2
---

# Mobile application standards
Version 0.1

## Audience 
Department-wide, third-party partners, vendors under-contract

## Purpose 
This policy provides the Department of Education's approach to determining what considerations should be given to the delivery of software applications for use via smartphones and tablets. It includes when applications should be designed to support use via these devices and when a native mobile application should be developed either wholly, or to complement a device agnostic application.

## Policy statement 
1. The department is committed to providing safe, secure mobility options when using its software systems.

2. The department is committed to enabling staff, students and parents to choose the device the best suits the situation, when delivering a software solution.

3. The department is committed to utilising features on devices to prevent/minimise data loss, corruption or theft.


## Native, hybrid or responsive website
Mobile devices such as smart phones, tablets and ‘phablets' can render applications using a number of different technology approaches. From a ‘mobile aware’ website that intelligently renders content according to the device’s size, to natively leveraging the device at the operating system and hardware layer.
There are three main reasons to consider building a native mobile application:
1. **Performance**: Native apps are optimised for specific platforms, offering fast and responsive user experiences by leveraging the device's hardware and software capabilities.

2. **Platform-specific features**: They can access device-specific APIs and features, delivering a user experience that aligns with platform expectations.

3. **Reliability and security**: Native apps are typically more secure and reliable by using the inherent security features of the operating system and often have fewer bugs due to the absence of cross-compatibility layers.

While there are certainly arguments to be made for other types of mobile applications, such as web or hybrid apps, native apps can provide the best performance, security, and user experience, which could make them the preferred choice for developers depending on the project's needs and requirements.

> **Case study: OneSchool Me**
> The Department observed a need for teachers to require a mobile app. A determining factor for a mobile app over a responsive web site was the need for teacher access to information ‘in the field’ where internet connectivity was not consistent.


> **Departmental recommendation**
> **A native mobile application**
> Native mobile solutions should be considered when it is required to provide data storage while offline, this is, using the local device, not the Internet for data storage. Currently only native solutions featuring encrypted storage options are deemed fit-for-purpose for housing official-to-sensitive data.
>
> **Hybrid/web-view JS app**
> Adequate if sufficient accessibility measures are implemented, and local storage is not required to house official-to-sensitive data.
>
> **Responsive website**
> Adequate for online-only content delivery to the general public.


## Connectivity
Mobile Applications have three main patterns of connectivity:
1. **Online**: These applications require constant internet connectivity, processing and storing data on a remote server.

2. **Offline**: These applications operate without internet, storing and processing data locally.

3. **Offline-first**: A hybrid approach where applications function fully without internet by prioritising local operations, but also ‘synchronise’ with a server when connectivity is available. Synchronisation is when the device regains internet connectivity and the application securely transfers the locally stored data back to the remote server or service.


## Architecture and frameworks

The choice of architecture and framework is a crucial decision that can impact many aspects of the mobile application.
1. **Performance**: The chosen framework can significantly impact app performance.

2. **Development speed and cost**: Some frameworks allow for faster, more cost-effective cross-platform development.

3. **Access to native features**: The framework can affect the app’s ability to use native device features.

4. **Community and support**: The size of a framework's community and the quality of its support can aid problem-solving during development.

5. **Maintenance and scalability**: The choice of framework impacts the ease of app updates, debugging, and scaling.

The vendor and/or community’s support for the framework is also crucial, consider:
1. **Longevity and support**: Reputable vendors are more likely to offer long-term support and regular updates.

2. **Quality and reliability**: A good vendor reputation often indicates higher framework quality and reliability.

3. **Community and ecosystem**: Established vendors usually have larger developer communities and richer tool ecosystems.

4. **Documentation and learning resources**: Reputable vendors typically provide comprehensive, well-maintained resources.

5. **Security**: Strong vendor reputation usually correlates with more robust security measures in their framework.

6. **Extensibility**: Reputable vendors and strong community support ensure the framework is open, adaptable and extendable.


> **Case study: OneSchool ME to QTeachers**
> The Department created a mobile app for teachers called ‘OneSchool ME’ using Angular and PWA technology. Whilst the app’s features were successful, the architecture was deemed too insecure for an Enterprise app. Microsoft’s Xamarin framework using .Net was subsequently selected. The new app was rebranded as ‘QTeachers’.


> **Departmental recommendation**
> **Microsoft Xamarin / MAUI & .Net frameworks**
> For cross platform native UI and hardware access, and source-code longevity (i.e.  non-proprietary vendor lock in).
>
> **Support and/or component libraries**
> Third-party libraries should offer commercial SLA based support channels.


### Usability and user interface
Designing a successful interface for mobile applications has special considerations. While there's some overlap, designing for mobile and web are different processes that require understanding and addressing the specific characteristics and constraints of each platform.
1. **Screen size**: Mobile designs must prioritise content and functionality due to smaller screens.

2. **Interaction**: Mobile interfaces are touch-based, requiring different interactive element designs compared to mouse-and-keyboard web interfaces.

3. **Context of use**: Mobile designs need to account for usage in various contexts, like on-the-go and in different lighting conditions.

4. **Capabilities**: Mobile devices have unique features like storage, GPS and camera that can be leveraged in the design.

5. **Design guidelines**: Each platform has its own design guidelines or best practices to follow.

6. **Performance**: Mobile designs need to consider the potentially lower processing power and memory of devices.

That is to say, successful mobile application design must be fit-for-purpose both for the user and the device. 

Consider:
**User-centric design**: Put the needs and preferences of your target users at the forefront of your design process. Consider the core principles of user experience – useful, usable, findable, credible, accessible and desirable.
**Simplicity and clarity**: Keep the interface simple, spacious and uncluttered. Avoid unnecessary elements and distractions and prioritse the most important features and content within each view.


**Consistency**: Maintain consistency throughout the interface in terms of visual elements, layout, navigation, and interactions. Consistency assists in the navigation, learnability and memorability of the product.


> **Case study: QTeachers**
> The QTeachers product worked closely with active teachers to ensure the product suited their specific needs including preferred device orientation, peek usage times, most common activities and page layout. A common icon and colour pallets was also employed to ensure consistency across the products functions and to reduce adoption and training friction.
> QTeachers continued leveraging teacher feedback through workshops and UAT sessions to further refine its user experience.


### Accessibility
It is a government requirement that all software products are WCAG 2.x AA compliant. In addition to standard accessibility considerations, additional special considerations should be given to mobile app accessibility including:
1. **Font size and spacing**: Text should be easily readable, and clickable elements should be large enough and spaced apart enough to be easily tapped without error. Text should also support the scaling accessibility settings of the device.

2. **Keyboard navigation**: Ensure that your application can be navigated using only a keyboard, which can be essential for people with motor disabilities.

3. **Ease of use**: Try to minimise the complexity of navigation and interaction, which can benefit people with cognitive impairments.

4. **Compatibility with assistive technologies**: The app should be compatible with assistive technologies like screen readers, magnifiers, or switch devices.

Remember, accessibility is not just a checklist—it's a perspective that should permeate the entire design process, from the earliest sketches to the final product, aiming to create an inclusive experience for all users.


> **Case study: QTeachers vs R4Q**
> QTeachers and R4Q share many common UI elements. However, R4Q was specifically designed for use on a tablet to suit the equipment issued to Regulatory Officers. QTeachers was designed to suit all form factors across Apple and Android given the diversity of the audience. Additionally, special efforts were made to ensure QTeachers could support teachers with special needs including supporting on-device accessibility tools and third-party screen-reading aids.


> **Departmental recommendation**
> **Accessibility**
> WCAG 2.x AA compliance is a government requirement.
> Quality assurance should be conducted on the physical device to ensure touch and gesture usability. On-device accessibility tools such as *Large Fonts* and *High Contrast Mode* should be supported.


### Data storage
Storing sensitive data on a mobile device comes with a number of risks and challenges. It's often best to avoid storing sensitive data locally whenever possible.
1. **Encryption**: Any sensitive data stored on a mobile device should be encrypted. This means converting the data into a code to prevent unauthorised access.

2. **Secure elements**: Use secure hardware-based containers, such as iOS's Keychain or Android's Keystore, to store cryptographic keys securely.

3. **Data minimisation**: Store only the data you absolutely need. The less data you store, the less there is to be compromised.

4. **Access controls**: Implement strong user authentication before granting access to sensitive data. Biometric authentication or multi-factor authentication can provide additional layers of security.

5. **Secure transfers**: If data must be transmitted, use secure connections like HTTPS or TLS, to protect the data while in transit.

6. **User data privacy:**  Clearly communicate your app's data privacy practices to users and obtain their informed consent.


> **Departmental recommendation**
> Locally stored data should be encrypted, example - **Zetetic SQLCipher, Commercial edition f**or Microsoft endorsed on-device storage encryption.


### Security
The security of a digital system can generally be divided into three key areas: hardware security, application security, and connectivity security.
1. **Hardware security**: Relates to physical device protections such as biometric systems and secure elements for storing encryption keys to prevent unauthorised physical access.

2. **Application security**: Involves ensuring applications don't have vulnerabilities that could be exploited, through measures like secure coding, proper data handling, local and remote user authentication mechanisms, and regular updates. Ensure that the APIs used by the app to communicate with the server are secure and update in lines with OS requirements.

3. **Connectivity security**: Pertains to securing network connections to prevent unauthorised access or eavesdropping during data transmission, using methods like secure protocols (HTTPS), VPNs, and encryption.

4. **Penetration testing and security audits:**  Conduct regular security assessments, penetration testing, and code reviews to identify and address any security vulnerabilities in your mobile app.


> **Case study: QTeachers and R4Q**
> Teachers and Regulatory officers deal with highly sensitive data, so it was clear these apps needed strong ‘security-by-design' patterns, even while offline.
> *Hardware security* – both apps run a check at the operating system level to ensure the hardware has been sufficiently secured. If the app has detected the hosting device has a no or low unlock security configured, the app will not open.
> *Application security* – regardless of whether the app is used online or offline, the app will raise a sign-in challenge by way of PIN or biometric. All locally saved data is strongly encrypted, and the app will self-lock after a short period of inactivity.
> *Connectivity security* – User claims and data-access are all controlled server-side, while enterprise issued OAuth tokens control access, ID and refresh states over SSL.


> **Departmental recommendation**
> **Hardware**
> PIN, passcode or biometrics should be enforced. Pattern or swipe unlocks are not sufficient.
>
> **Application**
> The App must offer an independent unlock challenge from the device if personal, confidential or sensitive information is stored.
>
> **Connectivity**
> Server-side claims management. 
> Authentication should be OAuth compliant.
> All data transfers should be encrypted and logged.


### Privacy
Considerations:
* Understanding personal privacy
* Understanding information
* Readiness for GDPR



### Distribution
When it comes to distributing your mobile app, there are several options available to reach your target audience. Selecting the correct distribution method and determining MDM compatibility requirements can assist with security, updating, coverage and delivery.

#### App store distribution
**Apple store**
**Public:** Publicly available on the App Store in the locations you selected and available to anyone for volume purchase through Apple Business Manager or Apple School Manager via a school MDM.
**Private:** The app will be available only on Apple Business Manager or Apple School Manager to specific businesses and organisations that you specify in App Store Connect via a school MDM.
**Unlisted:** Apps that aren’t suited for public distribution on the App Store, discoverable only with a direct link. Unlisted apps don’t appear in any App Store categories, recommendations, charts, search results, or other listings. In addition, they can be accessed through Apple Business Manager and Apple School Manager via a school MDM.
**Proprietary in-house apps:** Proprietary in-house apps are distributed to devices, not users. They require self-hosting and management of provisioning profiles and distribution certificates.

**Google Play store**
**Public:**  publicly available on the App Store in the locations you selected and available to anyone via a school MDM.
**Private:**  apps are similar to any other app on **Google Play** with the exception of them being restricted in distribution to the target enterprise(s via a school MDM.)

#### AppCentre
App Center Distribute is a tool for developers to release builds to end user devices. Distribute supports Android, iOS, macOS, UWP, WPF and WinForms apps, allowing you to manage app distribution across multiple platforms all in one place as a MDM.

MDM support
The table below provides a high level comparison of the MDMs that have been approved for use within the department’s environment for the purpose of managing Apple iOS devices.

Android devices are currently not supported within the department.


|                      | Jamf Pro | Jamf School | Lightspeed | Meraki | Mosyle | Intune |
| -------------------- | -------- | ----------- | ---------- | ------ | ------ | ------ |
| iPads and iPhones    | Y        | Y           | Y          | Y      | Y      | Y      |
| Mac and Macbooks     | Y        | Y           | Y          | Y      | Y      | Y      |
| Apple Tvs            | Y        | Y           | Y          |        | Y      |        |
| Windows              |          |             | Y          | Y      |        | Y      |
| Apple School Manager | Y        | Y           | Y          | Y      | Y      | Y      |




> **Case study: QTeachers**
> QTeachers was first established with an AppCentre distribution method, to allow for highly controlled and managed delivery, while in pilot phase. Once QTeachers updates became more regular and the addition of more schools, this distribution method was not fit for purpose, due to the complexity of updates at a school level, access, and visibility.  QTeachers then moved to an Unlisted Application distribution method via Apple Store to allow for streamlined and automatic updates, controlled delivery and store analytics to support the customer needs.


### Maintenance
Considerations:
* Ease of app support
* Operating system and hardware patching commitments
* Responding to bugs and vulnerabilities