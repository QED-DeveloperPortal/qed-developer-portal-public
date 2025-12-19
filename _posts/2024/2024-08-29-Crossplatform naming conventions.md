---
title: "Cross-platform naming conventions"
author: g-morton
categories: [Public]
classification: Public
tags: [standards]
date: 2024-08-29 02:13:37 
updatedBy: 
likes: 0
publishedOn: 2024-08-29 02:13:37
---

### Introduction

The following naming conventions are designed with C#.NET in mind, particularly within the context of Model-View-Controller (MVC) architectures. However, these standards are versatile and can be adapted to support other programming languages and frameworks. The core principles—such as using PascalCase for areas and controllers, camelCase for JavaScript and CSS files, and maintaining consistency in naming conventions—are universal best practices that enhance code readability, maintainability, and scalability across various programming environments.

While the examples provided are specific to C#.NET, developers can easily modify these conventions to fit other languages such as Java, Python, Ruby, or JavaScript frameworks. For instance:

- In Java, you might adapt the controller naming convention to follow typical Java class naming practices.
- In Python, PascalCase can be used for class names, and snake_case is preferred for function and variable names.
- In JavaScript or TypeScript, you can use the same conventions for naming components, services, or modules within a framework like Angular or React.

Ultimately, these guidelines serve as a foundation for maintaining a clean, consistent codebase, regardless of the specific technology stack in use.


### Naming conventions

#### Areas
Each functional area should have its own area name. The area name should be in PascalCase.

**Example:**
```plaintext
Dashboard
```

#### Controllers
Controller names should be in PascalCase and should end with `Controller`.

**Example:**
```plaintext
StudentController
```
An intermediate base controller can be created, but it must be named in the format `Base<AreaName>Controller`.

#### Actions
Action names should be in PascalCase and should indicate the operation being performed on the controller. Avoid repeating the context of the controller in the action name.

**Example:**
```plaintext
StudentController.Get() 
/* Not recommended */
StudentController.GetStudent()
```

#### Views
View names should match the action names using PascalCase wherever possible. Partial views should be prefixed with an underscore `_`.

**Example:**
```plaintext
_Edit.cshtml
```
If a partial view is associated with the main view to cater for Read-only or Edit mode, the name should be the same as the main view but with an underscore `_` prefix. The Read-only file should be placed under the `DisplayPartial` folder, and the Edit file should be under the `EditorPartial` folder.

**Example:**
```plaintext
Staff.cshtml (Main view)
_Staff.cshtml (Partial view)
```
For partial views associated with an “Item” model, name the partial view to correspond with the model.

**Example:**
```plaintext
If the model name is `StaffCentreRoleItem`, the corresponding partial view would be `_StaffCentreRoleItem.cshtml` and saved under the folder `DisplayPartial` or `EditorPartial`.
```

#### View models
The view model name should consist of the name of the primary entity plus one of the following suffixes:

- `ViewModel` – Used for the main view model

**Example:**
```plaintext
StaffViewModel
```
- `Item` – Used for displaying a list or as a model in a partial view

**Example:**
```plaintext
StaffCentreRoleItem
```
Models should be located directly in the `Models` folder of the area to which they belong.

#### Folder names
Folder names should be in PascalCase without spaces. Avoid creating new folders at the root level.

#### JavaScript file names
JavaScript file names should be in camelCase with a system code prefix.

**Example:**
```plaintext
oslp.js
```
JavaScript files should be stored and delivered as `.js` files.

**Function-specific**
Prefix the name with `<systemCode>.mvc.` followed by a function description.

**Example:**
```plaintext
oslp.mvc.attachment.js
```

**Area-specific**
The format should be `<systemCode>.<areaName>.js`.

**Example:**
```plaintext
oslp.schoolPlan.js
```

**Controller-specific**
The format should be `<systemCode>.<areaName>.<controllerName>.js`.

**Example:**
```plaintext
oslp.schoolPlan.school.js
```

#### CSS file names
CSS file names should be in camelCase with a system code prefix.

**Example:**
```plaintext
oslp.css
```

**Function-specific**
Prefix the name with `<systemCode>.mvc.` followed by a function description.

**Example:**
```plaintext
oslp.mvc.attachment.css
```

**Area-specific**
The format should be `<systemCode>.<areaName>.css`.

**Example:**
```plaintext
oslp.schoolPlan.css
```

**Controller-specific**
The format should be `<systemCode>.<areaName>.<controllerName>.css`.

**Example:**
```plaintext
oslp.schoolPlan.school.css
```
