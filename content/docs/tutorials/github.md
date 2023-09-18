---
title: GitHub
---

*This tutorial provides step-by-step instructions on how to rotate a GitHub Personal Access Token (PAT).*

---

## Generate a new GitHub PAT

### Step 1 - Navigate to the Access Token page
Navigate to the Access Token page: https://github.com/settings/tokens. 

To navigate to this link manually, click on your avatar in the top-right corner, then click `Settings`. Scroll all the way down and then click on the left-hand navbar tab named `Developer Settings`.
![](/images/github/1.png)

### Step 2 - Generate a new PAT
#### 2a. Click on `Generate new token`
You can either select the "Beta" or "Classic" version depending on your requirements. 
![](/images/github/2.png)
#### 2b. Name your token
Provide a name for your PAT in the "Note" field.
![](/images/github/3.png)
#### 2c. Configure token expiration
Set an expiration date for your token. The default is `30 Days`.
#### 2d. Configure token scopes
Select the required scopes.
#### 2e. Create the token
Click on `Generate token`.
![](/images/github/4.png)
Copy the token and save it to a secure place. It will not be displayed again.


---

## Replace the Leaked GitHub PAT
Replace the leaked GitHub Personal Access Token with the new one in all impacted applications and services.

---

## Revoke the Leaked GitHub PAT

### Step 1 - Navigate to the Access Token page
Navigate to the Access Token page: https://github.com/settings/tokens. 

To navigate to this link manually, click on your avatar in the top-right corner, then click `Settings`. Scroll all the way down and then click on the left-hand navbar tab named `Developer Settings`.
![](/images/github/1.png)

### Step 2 - Revoke the Access Token
#### 2a. Click `Delete` next to the relevant token
![](/images/github/6.png)
#### 2b. Click `I understand, delete this token`
![](/images/github/7.png)

---

## Best Practices

##### Fine-Grained PATs
Consider implementing a [fine-grained personal access token](https://github.blog/2022-10-18-introducing-fine-grained-personal-access-tokens-for-github/) to restrict token access and limit exposure in the event of a leaked PAT. 

##### Review Token Scopes
For all existing and new PATs, review the permissions (scopes) provided to each token. Consider limiting scopes to the least privilege required to conduct the relevant actions. To understand the permissions assigned to each scope, review [GitHub's scopes documentation](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps).

---

## Resources
- [GitHub Personal Access Token Documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)