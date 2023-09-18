---
title: Stripe
---

*This tutorial provides step-by-step instructions on how to rotate a Stripe API key.*

---

## Generate a new Stripe API key

### Step 1 - Navigate to the API key page
Navigate to https://dashboard.stripe.com/apikeys.
![](/images/stripe/2.png)

### Step 2 - Generate a new API key
> **Note:** Stripe allows creating two type of Keys, secret and restricted keys. The process for creating and revoking them is same. 
#### 2a. Click `Create secret key`
Click the `Create secret key` button and complete the required verification. 
![](/images/stripe/3.png)
#### 2b. Provide the `Key name` and click `Create`.
![](/images/stripe/4.png)

---

## Replace the Leaked Stripe API key
Replace the leaked Stripe API key with the new one in all impacted applications and services.

---

## Revoke the Leaked Stripe API key

### Step 1 - Navigate to the API key page
Navigate to https://dashboard.stripe.com/apikeys.
![](/images/stripe/2.png)

### Step 2 - Revoke the API key
#### 2a. Delete the key
Click on the `...` button next to the key that you want to delete. 
![](/images/stripe/5.png)

Click `Delete key...` from the dropdown.

![](/images/stripe/6.png)

#### 2b. Confirm deletion
Re-authenticate in the pop-up and then click `Delete key`.
![](/images/stripe/7.png)

---

## Resources
- [Stripe API key Documentation](https://stripe.com/docs/keys)