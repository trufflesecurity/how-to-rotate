---
title: Azure Search Admin
---

_This tutorial provides step-by-step instructions on how to rotate an Azure Search Admin Key._

---

## Regenerate an Azure Search Admin Key

### Step 1 - Navigate to the Azure Search Keys page

#### 1a. Navigate to `Azure AI`

Navigate to the `AI search` under `Azure AI services` page and click on the relevant `Azure Search service`.
![](/images/azuresearchadmin/1.png)

#### 1b. Navigate to `Keys` page

Under `Settings`, click on `Keys`.

![](/images/azuresearchadmin/2.png)

### Step 2 - Regenerate the Azure Search Admin Key

Click the copy icon and paste it in your editor to check the key. Ensure you're rotating the correct key.
![](/images/azuresearchadmin/3.png)

Confirm the key regeneration action by clicking `Regenerate`.

![](/images/azuresearchadmin/4.png)

You'll see a message at the top-right indicating that you "Successfully regenerated the primary or secondary admin key".

![](/images/azuresearchadmin/5.png)

> Note: Clicking `Yes` will revoke the existing key in addition to creating a new one.

---

## Replace the Leaked Azure Search Admin Key

Replace the leaked Azure Search Admin Key with the new one in all impacted applications and services.

---

## Resources

- [Azure Search Admin Keys Documentation](https://learn.microsoft.com/en-us/rest/api/searchservice/index-preview)
