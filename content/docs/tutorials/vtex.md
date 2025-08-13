---
title: VTEX
---

*This tutorial provides step-by-step instructions on how to rotate a VTEX API Key.*

---

## Generate a new VTEX API Key

### Step 1 - Navigate to the API Keys page
Log into your VTEX admin account and navigate to `https://{accountName}.myvtex.com/admin/api-keys`.
![](/images/vtex/1.gif)

### Step 2 - Generate a new API Key
#### 2a. Click `Generate Key`
![](/images/vtex/2.png)
#### 2b. Provide `Key identification`, add roles and click `Generate`
![](/images/vtex/3.gif)
#### 2c. Copy the token unique access link
![](/images/vtex/4.png)
#### 2d. Navigate to the token unique access link
Go to the link generated in the previous step, in the format `https://share.vtex.com/credentials/{token}`, where `token` is a random identifier generated when the key is created.
![](/images/vtex/5.png)
#### 2e. Copy the `Key` and the `New token` and store it somewhere safe
![](/images/vtex/6.gif)

---

## Replace the Leaked VTEX API Key
Replace the leaked VTEX API Key with the new one in all impacted applications and services.

---

## Revoke the Leaked VTEX API Key

### Step 1 - Navigate to the API Keys page
Log into your VTEX admin account and navigate to `https://{accountName}.myvtex.com/admin/api-keys`.
![](/images/vtex/1.gif)

### Step 2 - Revoke the VTEX API Key
#### 2a. Click `Delete Key`
Find the row of the API Key you want to delete and click the ellipsis menu `⋮`, then click the `Delete Key` menu option.
![](/images/vtex/7.png)
#### 2b. Confirm deletion
Check `I understand that this action cannot be undone` and click `Delete` to confirm.
![](/images/vtex/8.png)

---

## Resources
- [VTEX API Key Documentation](https://help.vtex.com/en/tutorial/api-keys--4bFEmcHXgpNksoePchZyy6)
- [VTEX API Key Best Practices](https://help.vtex.com/en/tutorial/best-practices-api-keys--7b6nD1VMHa49aI5brlOvJm)