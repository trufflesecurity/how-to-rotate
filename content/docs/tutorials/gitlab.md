---
title: GitLab
---

*This tutorial provides step-by-step instructions on how to rotate a GitLab Personal Access Token.*

---

## Generate a new GitLab Personal Access Token

### Step 1 - Navigate to the Personal Access Token page
Navigate to https://gitlab.com/-/profile/personal_access_tokens.
![](/images/gitlab/2.png)

### Step 2 - Generate a new Personal Access Token
#### 2a. Configure the access token
Provide a `Token Name`, set an `Expiration Date` and select token `scopes` (permissions).
#### 2b. Click on `Create personal access token`.
#### 2c. View/Copy the new token
![](/images/gitlab/3.png)

---

## Replace the Leaked GitLab Personal Access Token
Replace the leaked GitLab Personal Access Token with the new one in all impacted applications and services.

---

## Revoke the Leaked GitLab Personal Access Token

### Step 1 - Navigate to the Personal Access Token page
Navigate to https://gitlab.com/-/profile/personal_access_tokens.
![](/images/gitlab/2.png)


### Step 2 - Revoke the Personal Access Token
#### 2a. Delete the leaked token
Click on the delete icon under the "Action" column in the row corresponding to the token that you want to delete. 
![](/images/gitlab/4.png)
#### 2b. Confirm deletion
Click `Revoke` to confirm deletion.
![](/images/gitlab/5.png)

A message will appear indicating the token was deleted.
![](/images/gitlab/6.png)

---

## Resources
- [GitLab Personal Access Token Documentation](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)