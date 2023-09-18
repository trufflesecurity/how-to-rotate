---
title: Atlassian
---

*This tutorial provides step-by-step instructions on how to rotate an Atlassian API Token.*

---

## Generate a new Atlassian API Token 

### Step 1 - Navigate to the API Token page
The API token page is located at: https://id.atlassian.com/manage-profile/security/api-tokens.
![](/images/atlassian/1.png)

### Step 2 - Generate a new API Token
#### 2a. Click on `Create API token`
![](/images/atlassian/2.png)
#### 2b. Provide a `Label` and click on `Create`
![](/images/atlassian/3.png)
#### 2c. The new token will generated
![](/images/atlassian/4.png)

---

## Replace the Leaked Atlassian Token
Replace the leaked Atlassian key with the new one in all impacted applications and services.

---

## Revoke the Leaked Atlassian Token
### Step 1 - Navigate to the API Token page
The API token page is located at: https://id.atlassian.com/manage-profile/security/api-tokens.
![](/images/atlassian/1.png)

### Step 2 - Revoke the Token
Click on the `Revoke` button next to the API key you want to delete. Then click `Revoke` again in the pop up.
![](/images/atlassian/6.png)

---

## Resources
- Learn more about [Automatic API Key Rotation in Atlassian](https://support.atlassian.com/organization-administration/docs/set-up-automatic-key-rotation/), if you're using an application tunnel.