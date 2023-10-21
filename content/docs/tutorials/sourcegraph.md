---
title: Sourcegraph
---

*This tutorial provides step-by-step instructions on how to rotate a Sourcegraph Access Token.*

---

## Generate a New Sourcegraph Access Token

#### Step 1a. Navigate to the Access Token page
Navigate to the url [https://sourcegraph.com/users/{username}/settings/tokens](https://sourcegraph.com/users/{sourcegraph_username}/settings/tokens). Replace `{username}` with your Sourcegraph username. If this token is from different Sourcegraph instance, replace the url with the instance url example: https://sourcegraph.example.com/users/{username}/settings/tokens.

![Access token page](/images/sourcegraph/1.png)

#### Step 1b. Generate Access Token
Type in a new description for the Access Token.

#### Step 1c. Confirm
Click the `Generate Token` button to confirm the operation.

![Regenerate access token](/images/sourcegraph/3.png)

## Replace the Leaked Sourcegraph Access token
Replace the leaked Sourcegraph access token with the new one in all impacted applications and services.

### Revoke the Access Token
#### Step 3a. Revoke the existing Access Token
Go through the list of Access Tokens and revoke the existing one by clicking the `Delete` button.
#### Step 3b. Confirm
Click the `OK` button to confirm the operation.

![Revoke access token](/images/sourcegraph/2.png)

> **Note:** For security reasons, Sourcegraph Access Tokens are masked after creation. If you lose the key, you will need to generate a new one. 


---

## Replace the Leaked Sourcegraph Access Token
Replace the leaked Sourcegraph Access Token with the new one in all impacted applications and services.

---

## Resources
- [Sourcegraph API Documentation](https://docs.sourcegraph.com/api/graphql)
