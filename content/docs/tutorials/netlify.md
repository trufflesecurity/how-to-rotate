---
title: Netlify
---

*This tutorial provides step-by-step instructions on how to rotate a Netlify Personal Access Token.*

---

## Generate a new Netlify Personal Access Token

### Step 1 - Navigate to the Personal Access Token page
Navigate to [https://app.netlify.com/user/applications#personal-access-tokens](https://app.netlify.com/user/applications#personal-access-tokens)
![](/images/netlify/2.png)

### Step 2 - Generate a new Personal Access Token
#### 2a. Click `New Access Token`
![](/images/netlify/1.png)
#### 2b. Configure the new token
Provide a description for the token.
#### 2c. Click `Generate Token`
![](/images/netlify/3.png)

---

## Replace the Leaked Netlify Personal Access Token
Replace the leaked Netlify Personal Access Token with the new one in all impacted applications and services.

---

## Revoke the Leaked Netlify Personal Access Token

### Step 1 - Navigate to the Personal Access Token page
Navigate to [https://app.netlify.com/user/applications#personal-access-tokens](https://app.netlify.com/user/applications#personal-access-tokens)
![](/images/netlify/2.png)

### Step 2 - Revoke the Personal Access Token
#### 2a. Delete the token
Click on `Options` then `Delete personal token` next to the token that you want to delete.
![](/images/netlify/4.png)
#### 2b. Confirm deletion
Click `Delete` to confirm deletion.
![](/images/netlify/5.png)

---

## Resources
- [Netlify Personal Access Token Documentation](https://docs.netlify.com/cli/get-started/#authentication)
