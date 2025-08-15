---
title: "JA GH OAI authentication doc in text"
slug: "ja-gh-oai-authentication-doc-in-text-b2e3a1"
author: jeny-amatya-qed
owner: jeny-amatya-qed
categories: Public
classification: Public
tags: [auto-import, about]
date: 2025-08-15 04:46:47
likes: 0
imported: True 
import-source: "github"
import-reference: ""
import-config-id: "61355e30-9bf7-4d48-ba80-cb08bb580a99"
---


# Action authentication

Actions offer different authentication schemas to accommodate various use cases. To specify the authentication schema for your action, use the GPT editor and select "None", "API Key", or "OAuth".

By default, the authentication method for all actions is set to "None", but you can change this and allow different actions to have different authentication methods.

## No authentication

We support flows without authentication for applications where users can send requests directly to your API without needing an API key or signing in with OAuth.

Consider using no authentication for initial user interactions as you might experience a user drop off if they are forced to sign into an application. You can create a "signed out" experience and then move users to a "signed in" experience by enabling a separate action.

## API key authentication

Just like how a user might already be using your API, we allow API key authentication through the GPT editor UI. We encrypt the secret key when we store it in our database to keep your API key secure.

This approach is useful if you have an API that takes slightly more consequential actions than the no authentication flow but does not require an individual user to sign in. Adding API key authentication can protect your API and give you more fine-grained access controls along with visibility into where requests are coming from.

## OAuth

Actions allow OAuth sign in for each user. This is the best way to provide personalized experiences and make the most powerful actions available to users. A simple example of the OAuth flow with actions will look like the following:

-   To start, select "Authentication" in the GPT editor UI, and select "OAuth".
-   You will be prompted to enter the OAuth client ID, client secret, authorization URL, token URL, and scope.
    -   The client ID and secret can be simple text strings but should [follow OAuth best practices](https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/).
    -   We store an encrypted version of the client secret, while the client ID is available to end users.
-   OAuth requests will include the following information: `request={'grant_type': 'authorization_code', 'client_id': 'YOUR_CLIENT_ID', 'client_secret': 'YOUR_CLIENT_SECRET', 'code': 'abc123', 'redirect_uri': 'https://chatgpt.com/aip/g-some_gpt_id/oauth/callback'}`
-   In order for someone to use an action with OAuth, they will need to send a message that invokes the action and then the user will be presented with a "Sign in to [domain]" button in the ChatGPT UI.
-   The `authorization_url` endpoint should return a response that looks like:
    `{ "access_token": "example_token", "token_type": "bearer", "refresh_token": "example_token", "expires_in": 59 }`
-   During the user sign in process, ChatGPT makes a request to your `authorization_url` using the specified `authorization_content_type`, we expect to get back an access token and optionally a [refresh token](https://auth0.com/learn/refresh-tokens) which we use to periodically fetch a new access token.
-   Each time a user makes a request to the action, the user’s token will be passed in the Authorization header: (“Authorization”: “[Bearer/Basic] [user’s token]”).
-   We require that OAuth applications make use of the [state parameter](https://auth0.com/docs/secure/attack-protection/state-parameters#set-and-compare-state-parameter-values) for security reasons.
