---
title: Azure Function
---

_This tutorial provides step-by-step instructions on how to rotate an Azure Function Key._

---

## Regenerate an Azure Function Key

### Step 1 - Navigate to the Azure Function App page

#### 1a. Navigate to `Azure Function App`

Navigate to the `Azure Function App` page and click on the relevant `Azure Function App`.
![](/images/azurefunction/1.png)

#### 1b. Navigate to `App keys` or `Function keys`

There are two types of keys:

1. `App keys` can access all the functions within the function app
2. `Function keys` can only access specific function within function app

For `App keys`, under `Functions`, click on `App keys`.
![](/images/azurefunction/2.png)

For `Function keys`, click the relevant function. Under `Developer` section, click `Function Keys`.
![](/images/azurefunction/5.png)

![](/images/azurefunction/6.png)

### Step 2 - Regenerate the App keys or Function keys

For `App keys`, see under `Host keys (all functions)`, click `Renew key value`. If you have multiple keys, clicking the `Show value` will reveal the key's information. Ensure that you are rotating the correct key.
![](/images/azurefunction/3.png)
Confirm the key renewal action by clicking `Renew and save`.

![](/images/azurefunction/4.png)

For `Function keys`, click `Renew key value`. If you have multiple keys, clicking the `Show value` will reveal the key's information. Ensure that you are rotating the correct key.
![](/images/azurefunction/7.png)
Confirm the key renewal action by clicking `Renew and save`.

![](/images/azurefunction/8.png)

> Note: Clicking `Renew and save` will revoke the existing key in addition to creating a new one.

---

## Replace the Leaked Azure Function Key

Replace the leaked Azure Function Key with the new one in all impacted applications and services.

---

## Resources

- [Azure Function Key Documentation](https://learn.microsoft.com/en-us/azure/azure-functions/)
