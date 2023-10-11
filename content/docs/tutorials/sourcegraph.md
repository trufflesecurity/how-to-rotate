---
title: Sourcegraph
---

*This tutorial provides step-by-step instructions on how to rotate a Sourcegraph Access Token.*

---

## Generate a New Sourcegraph Access Token

### Step 1 - Navigate to the Access Token page
Navigate to the url [https://sourcegraph.com/users/{username}/settings/tokens](https://sourcegraph.com/users/{sourcegraph_username}/settings/tokens). Replace `{username}` with your Sourcegraph username. If this token is from different Sourcegraph instance, replace the url with the instance url example: https://sourcegraph.example.com/users/{username}/settings/tokens.

![](/images/sourcegraph/1.png)

### Step 2 - Revoke the Access Token
#### 2a. Revoke the existing Access Token
Go through the list of Access Tokens and revoke the existing one by clicking the `Delete` button.
#### 2b. Confirm
Click the `OK` button to confirm the operation.
![](/images/sourcegraph/2.png)

### Step 3 - Regenerate the Access Token
#### 3a. Navigate to the Access Tokens page
Navigate to the url [https://sourcegraph.com/users/{username}/settings/tokens/new](https://sourcegraph.com/users/{username}/settings/tokens/new). Replace `{username}` with your Sourcegraph username. If this token is from different Sourcegraph instance, replace the url with the instance url example: https://sourcegraph.example.com/users/{username}/settings/tokens/new.
#### 3b. Regenerate Access Token
Type in a new description for the Access Token.
#### 3c. Confirm
Click the `Generate Token` button to confirm the operation.
![](/images/sourcegraph/3.png)

> **Note:** For security reasons, Sourcegraph Access Tokens are masked after creation. If you lose the key, you will need to generate a new one. 


---

## Replace the Leaked Sourcegraph Access Token
Replace the leaked Sourcegraph Access Token with the new one in all impacted applications and services.

---

## Resources
- [Sourcegraph API Documentation](https://docs.sourcegraph.com/api/graphql)