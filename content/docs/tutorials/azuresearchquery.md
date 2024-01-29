---
title: Azure Search Query
---

_This tutorial provides step-by-step instructions on how to rotate an Azure Search Query Key._

---

## Generate a new Azure Search Query Key

### Step 1 - Navigate to the Azure Search Keys page

#### 1a. Navigate to `Azure AI`

Navigate to the `AI search` under `Azure AI services` page and click on the relevant `Azure Search service`.
![](/images/azuresearchquery/1.png)

#### 1b. Navigate to `Keys` page

Under `Settings`, click on `Keys`.

![](/images/azuresearchquery/2.png)

### Step 2 - Generate a new key

#### 2a. Create a new key

Under `Manage query keys`, click `Add` buttton and provide name of the new query key.

![](/images/azuresearchquery/3.png)

#### 2b. Copy the new token

![](/images/azuresearchquery/4.png)

---

## Replace the Leaked Azure Search Query Key

Replace the leaked Azure Search Query Key with the new one in all impacted applications and services.

---

## Revoke the Leaked Azure Search Query Key

Hover and mark check the leaked key to enable the `Delete` button. Ensure you're deleting the correct leaked key.
![](/images/azuresearchquery/5.png)

Confirm the key deletion action by clicking `Yes`.

> Note: Clicking `Yes` will revoke the existing key.

## Resources

- [Azure Search Query Keys Documentation](https://learn.microsoft.com/en-us/rest/api/searchservice/index-preview)
