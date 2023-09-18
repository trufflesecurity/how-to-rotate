---
title: MongoDB
---

*This tutorial provides step-by-step instructions on how to rotate a MongoDB API key.*

---

## Generate a new MongoDB API key

### Step 1 - Navigate to the API key page
After logging in, click the `Access Manager` tab on the left-hand navbar and then the `API Keys` tab.
![](/images/mongo/2.png)

### Step 2 - Generate a new API key
#### 2a. Click `Create API Key`
#### 2b. Configure the API key
Provide a `Description`, select the `Organization Permissions` and then click `Next`.
![](/images/mongo/3.png)
#### 2c. Copy the `Private Key`
![](/images/mongo/4.png)

---

## Replace the Leaked MongoDB API key
Replace the leaked MongoDB API key with the new one in all impacted applications and services.

---

## Revoke the Leaked MongoDB API key

### Step 1 - Navigate to the API key page
After logging in, click the `Access Manager` tab on the left-hand navbar and then the `API Keys` tab.
![](/images/mongo/2.png)

### Step 2 - Revoke the API key
#### 2a. Delete the key
Click the delete icon next to the API key you want to delete.
![](/images/mongo/6.png)
#### 2b. Confirm deletion
Click the `Delete` button to confirm deletion.
![](/images/mongo/7.png)

---

## Resources
- [MongoDB API key Documentation](https://www.mongodb.com/docs/atlas/app-services/authentication/api-key/)