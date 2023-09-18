---
title: Slack
---

*This tutorial provides step-by-step instructions on how to rotate a Slack Configuration Token.*

---

## Generate a new Slack Configuration Token

### Step 1 - Navigate to the Configuration Token page
Log into your Slack workspace admin account and navigate to https://api.slack.com/apps/.
![](/images/slack/1.png)

### Step 2 - Generate a new Configuration Token
#### 2a. Click `Generate Token`
![](/images/slack/6.png)
#### 2b. Select a workspace & click `Generate`
![](/images/slack/2.png)
#### 2c. Copy the tokens
You can copy the `Access Token` and `Refresh Token` by clicking on the relevant `Copy` button.
![](/images/slack/3.png)

---

## Replace the Leaked Slack Configuration Token
Replace the leaked Slack Configuration Token with the new one in all impacted applications and services.

---

## Revoke the Leaked Slack Configuration Token

### Step 1 - Navigate to the Configuration Token page
Log into your Slack workspace admin account and navigate to https://api.slack.com/apps/.
![](/images/slack/1.png)

### Step 2 - Revoke the Configuration Token
#### 2a. Click the delete button
Click the delete trashcan icon button in the row corresponding to the configuration token you want to delete.
![](/images/slack/4.png)

#### 2b. Confirm revocation
Click the `Revoke Token` button.
![](/images/slack/5.png)

---

## Resources
- [Slack Configuration Token Documentation](https://api.slack.com/authentication/config-tokens)