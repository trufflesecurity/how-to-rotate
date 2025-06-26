---
title: GCP
---

*This tutorial provides step-by-step instructions on how to rotate a Google Cloud Platform (GCP) Service Account key.*

---
## Generate a new GCP Service Account Key

### Step 1 - Navigate to the relevant Service Account page
#### 1a. Navigate to the impacted GCP project
#### 1b. Click on the `IAM & Admin` tab
On the left-hand menu, click on the `IAM & Admin` tab.

![](/images/gcp/1.png)

#### 1c. Navigate to the relevant `Service Account`
In the `IAM & Admin` tab dropdown, click on `Service Accounts` to view your existing service accounts.

![](/images/gcp/2.png)

Click on the service account you want to create the Service Account key for.

![](/images/gcp/3.png)


### Step 2 - Generate a new GCP Service Account key

#### 2a. Create a new key
Click on the `Keys` tab. Click on the `Add Key` button and then select `Create new key`.
![](/images/gcp/4.png)
#### 2b. Choose the key type and click `Create`
Choose the key type (`JSON` or `P12`) and click `Create`.
![](/images/gcp/5.png)
#### 2c. New key automatically downloads to your computer
The new Service Account key will be downloaded to your computer. Make sure to store it in a secure location.
![](/images/gcp/6.png)

---
## Replace the Leaked GCP Service Account Key

Replace the leaked GCP Service Account Key with the new one in all impacted applications and services.

---
## Revoke the Leaked GCP Service Account Key

#### *Note: deleting the project that contains the key, does not ensure swift deactivation of that key. GCP services and traffic can remain active up to 30 days after scheduling a project for deletion*

### Step 1 - Navigate to the relevant Service Account page
#### 1a. Navigate to the impacted GCP project
#### 1b. Click on the `IAM & Admin` tab
On the left-hand menu, click on the `IAM & Admin` tab.

![](/images/gcp/1.png)

#### 1c. Navigate to the relevant `Service Account`
In the `IAM & Admin` tab dropdown, click on `Service Accounts` to view your existing service accounts.

![](/images/gcp/2.png)

Click on the service account you want to revoke the Service Account key for.

![](/images/gcp/3.png)



### Step 2 - Revoke the leaked GCP Service Account key

#### 2a. Delete the relevant key
Click on the `Keys` tab. Click on the `Delete` icon at the end of the row of the key you want to delete. 
![](/images/gcp/7.png)
#### 2b. Confirm deletion.
Click on the `Delete` button.
![](/images/gcp/8.png)
A message will pop up informing you that the key has been deleted.
![](/images/gcp/9.png)

---
## Resources
- [GCP Service Account Key Documentation](https://cloud.google.com/iam/docs/keys-create-delete)
