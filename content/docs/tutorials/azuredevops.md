---
title: Azure DevOps
---

_This tutorial provides step-by-step instructions on how to rotate an Azure DevOps Personal Access Token._

---

## Regenerate an Azure DevOps Personal Access Token

### Step 1 - Navigate to the Azure DevOps Tokens page

#### 1a. Navigate to `Azure DevOps Organizations`

Navigate to the `Azure DevOps Organizations` page and click on the relevant `Azure DevOps Organizations Account`.
![](/images/azuredevops/1.png)

#### 1b. Navigate to `Personal Access Tokens`

Under `User Settings`, click on `Personal Access Tokens`.
![](/images/azuredevops/2.png)

### Step 2 - Regenerate the Personal Access Tokens

Click on the any token and the `Revoke`, `Edit`, and `Regenerate` actions will appear. If you click on `Edit` will reveal that tokens's information. Ensure you're rotating the correct token.
![](/images/azuredevops/3.png)
Confirm the token regeneration action by clicking `Regenerate`.

![](/images/azuredevops/4.png)

You'll see a message at the top indicating that you "Successfully added a new personal access token".

![](/images/azuredevops/5.png)

> Note: Clicking `Regenerate` will revoke the existing key in addition to creating a new one.

---

## Replace the Leaked Azure DevOps Personal Access Token

Replace the leaked Azure DevOps Personal Access Token with the new one in all impacted applications and services.

---

## Resources

- [Azure DevOps Personal Access Tokens Documentation](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)
