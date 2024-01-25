---
title: Azure Storage
---

_This tutorial provides step-by-step instructions on how to rotate an Azure Storage Account Access Key._

---

## Regenerate an Azure Storage Account Access Key

### Step 1 - Navigate to the Access keys page

#### 1a. Navigate to `Storage Accounts`

Navigate to the `Storage Accounts` page and click on the relevant `Storage Account`.
![](/images/azure/1.png)

#### 1b. Navigate to `Access Keys`

Under `Security + networking`, click on `Access Keys`.

![](/images/azure/2.png)

### Step 2 - Regenerate the Access key

Click on the `Rotate key`. If you have multiple keys, clicking `Show` next to the `Key` or `Connection String` fields will reveal that key's information. Ensure you're rotating the correct key.
![](/images/azure/4.png)
Confirm the key rotation action by clicking `Yes`.
![](/images/azure/5.png)
You'll see a message at the top indicating that you "Successfully regenerated access key".
![](/images/azure/6.png)

> Note: Clicking `Rotate key` will revoke the existing key in addition to creating a new one.

---

## Replace the Leaked Azure Storage Account Access Key

Replace the leaked Azure Storage Account Access Key with the new one in all impacted applications and services.

---

## Resources

- [Azure Storage Account Access Keys Documentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal)
