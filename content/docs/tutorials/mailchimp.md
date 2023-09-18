---
title: Mailchimp
---
<!-- 
![](/images/mailchimp/header.png) -->

*This tutorial provides step-by-step instructions on how to rotate a Mailchimp API Key.*

---

## Generate a New Mailchimp API key
### Step 1 - Navigate to the API keys page
After logging in, navigate to https://us12.admin.mailchimp.com/account/api/.

> **Note:** Based on your location, the API keys page URL will differ. Mailchimp substitutes \<your_region\> into the URL https://\<your_region\>.admin.mailchimp.com/account/api. Similalrly, API key formats may differ by region as well. 

### Step 2 - Generate a new key
#### 1. Click on "Create New Key" 
![](/images/mailchimp/2.png)

#### 2. Provide an "API Key Name" and click on "Generate Key"
![](/images/mailchimp/3.png)

### Step 3 - Copy the new key
Copy the new key manually or by selecting the "Copy to Clipboard" button. Then, click "Done".

> **Note:** For security reasons, Mailchimp API keys are masked after creation. If you lose the key, you will need to generate a new one. 

---

## Replace the Leaked Mailchimp Key
Replace the leaked Mailchimp API key with the new one in all impacted applications and services.

---

## Revoke the Leaked Mailchimp API key
### Step 1 - Navigate to the API keys page
After logging in, navigate to https://us12.admin.mailchimp.com/account/api/.

> **Note:** Based on your location, the API keys page URL will differ. Mailchimp substitutes \<your_region\> into the URL https://\<your_region\>.admin.mailchimp.com/account/api. Similalrly, API key formats may differ by region as well. 

![](/images/mailchimp/4.png)

### Step 2 - Click "Revoke" on the relevant Key
Find the API key you want to revoke and click "Revoke".
![](/images/mailchimp/5.png)

### Step 3 - Confirm the key
Type "REVOKE" in the input prompt and click on "Revoke".
![](/images/mailchimp/6.png)

### Step 4 - Observe the Key is revoked
Mailchimp will place a strike through the API key, so that you know it's revoked.
![](/images/mailchimp/7.png)

---

## Notes & Best Practices

#### Separate keys by integration
Mailchimp recommends using a separate API key for each integration. Establishing separate keys helps when responding to a security incident, so that you only need to rotate the specific compromised key and not disrupt other services.

#### No client-side implementations
Mailchimp does not support any client-side implementations. As a result, API keys should never be in front-end or mobile application source code.

---

## Resources

- [https://mailchimp.com/help/about-api-keys](https://mailchimp.com/help/about-api-keys)