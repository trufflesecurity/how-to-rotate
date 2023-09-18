---
title: AWS
---

*This tutorial provides step-by-step instructions on how to rotate an AWS Access Key.*

---
## Generate a new AWS access key

### Step 1 - Navigate to the Access keys page
#### 1a. Navigate to `Security Credentials`
In the upper-right hand corner, click on your AWS account name. This will display a dropdown menu. Click on `Security Credentials`. 
![](/images/aws/11.png)

#### 1b. Scroll down to the `Access Keys` section
![](/images/aws/6.png)

### Step 2 - Generate a new Access key
#### 2a. Click on `Create access key`
![](/images/aws/3.png)

#### 2b. Copy the `Access key` and `Secret access key` values
You can download the new keys in a `.csv` file by clicking on `Download .csv file`.
![](/images/aws/5.png)

---
## Replace the Leaked AWS Key

Replace the leaked AWS key with the new one in all impacted applications and services.

---
## Revoke the Leaked AWS key
### Step 1 - Navigate to the Access keys page
#### 1a. Navigate to `Security Credentials`
In the upper-right hand corner, click on your AWS account name. This will display a dropdown menu. Click on `Security Credentials`. 
![](/images/aws/11.png)

#### 1b. Scroll down to the `Access Keys` section
![](/images/aws/6.png)

### Step 2 - Deactivate the key

#### 2a. Click `Actions` and then `Deactivate`
Click the checkbox next to the key you want to delete. Click on the `Actions` menu and then press `Deactivate`.
![](/images/aws/12.png)

#### 2b. Click `Deactivate`
![](/images/aws/10.png)

### Step 3 - Delete the key

#### 3a. Click `Actions` and then `Delete`
Once the key status is "inactive", you can delete the key. Click the checkbox next to the key you want to delete. Click on the `Actions` menu and then press `Delete`. 
![](/images/aws/7.png)

#### 3b. Type the key and Click `Delete`
Copy/paste the access key into the input field and then click `Delete`.
![](/images/aws/13.png)

---
## Resources
- [https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html](https://docs.aws.amazon.com/accounts/latest/reference/credentials-access-keys-best-practices.html)