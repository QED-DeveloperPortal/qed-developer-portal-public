---
title: "Copy folder repo import"
slug: "copy-folder-repo-import-76fe96"
author: jeny-amatya-qed
owner: jeny-amatya-qed
categories: public
tags: [auto-import, technology]
date: 2026-02-09 22:02:27
likes: 0
publishedOn: 2026-02-09 22:02:27
imported: True 
import-source: "github"
import-reference: ""
import-url: "https://github.com/QED-DeveloperPortal/copy_folder_to_another_repo_action/blob/master/README.md"
source-published-on: 2020-08-24 19:25:59
source-updated-on: 2026-02-09 22:02:11
import-config-id: "2aaaadfc-8a13-4752-9c93-95d1c5194a3d"
---

# copy_folder_to_another_repo_action
This GitHub Action copies a folder from the current repository to a location in another repository.

## Example Workflow
```yaml
name: Push File

on: push 

jobs:
  copy-file:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v2

    - name: Pushes test folder
      uses: crykn/copy_folder_to_another_repo_action@v1.0.6
      env:
        API_TOKEN_GITHUB: ${{ secrets.API_TOKEN_GITHUB }}
      with:
        source_folder: 'test_files'
        destination_repo: 'dmnemec/release-test'
        destination_folder: 'test-dir'
        user_email: 'devin.nemec@gmail.com'
        user_name: 'dmnemec'
        commit_msg: '[GHA] Update the test files.'
```

## Variables
* **source_folder:** The folder to be moved.
* **destination_repo:** The repository to place the folder in.
* **destination_folder:** [optional] The folder in the destination repository to place the file in, if not the root directory.
* **user_email:** The GitHub user email associated with the API token secret.
* **user_name:** The GitHub username associated with the API token secret.
* **destination_branch:** [optional] The branch of the destination repo to base the changes on and push to (defaults to master).
* **destination_branch_create:** [optional] The branch the changes should be pushed to; defaults to committing to `destination_branch`; is useful for creating PRs.
* **commit_msg:** [optional] The commit message to use.

## Behavior Notes
The action will remove the destination folder before recreating it to place any copied files in it.

Updated on 10/02/206 8:02 AM