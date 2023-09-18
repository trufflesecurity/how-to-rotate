---
title: Slack Webhook
---

*This tutorial provides step-by-step instructions on how to rotate a Slack Webhook.*

---

## Generate a new Slack Webhook

### Step 1 - Navigate to the Webhook page
Log into your Slack workspace and navigate to https://api.slack.com/apps/
![](/images/slack-webhook/1.png)

### Step 2 - Generate a new Slack App with Webhook
#### 2a. Click `Create New App`
Click on the `Create New App` button and choose either `From Scratch` or `From an app manifest`. 
![](/images/slack-webhook/2.png)

#### 2b. Select the Workspace
![](/images/slack-webhook/3.png)

#### 2c. Review the Configuration and Create the App
Review all of the Application configuration options by clicking through the `Next` buttons. On the last step, click `Create` to create the app.
![](/images/slack-webhook/4.png)
![](/images/slack-webhook/5.png)

#### 2d. Select Incoming Webhooks
Select the `Incoming Webhooks` tile from the `Add features and functionality` dropdown. 
![](/images/slack-webhook/6.png)

#### 2e. Activate the Incoming Webhook
![](/images/slack-webhook/7.png)

#### 2f. Add a New Webhook to the Workspace
Click on `Add New Webhook to Workspace`.
![](/images/slack-webhook/8.png)

#### 2g. Select the Channel
Select the channel that the webhook should post to. Click `Allow` to grant the required permissions to that channel.
![](/images/slack-webhook/9.png)

#### 2h. Verify the Webhook
Copy the webhook URL and then verify the webhook works by sending a test message to the channel.

![](/images/slack-webhook/10.png)

`curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' <WEBHOOK_URL>`

![](/images/slack-webhook/11.png)

---

## Replace the Leaked Slack Webhook
Replace the leaked Slack Webhook with the new one in all impacted applications and services.

---

## Revoke the Leaked Slack Webhook

### Step 1 - Navigate to the Webhook page
Log into your Slack workspace and navigate to https://api.slack.com/apps/
![](/images/slack-webhook/1.png)

### Step 2 - Revoke the Webhook
#### 2a. Select your target app
Select your target app and click on `Incoming Webhooks`.
![](/images/slack-webhook/12.png)

#### 2b. Consider disabling webhooks
If you no longer need webhooks for this application, you can disable them. However, the existing ones will still be accessible.
![](/images/slack-webhook/13.png)

#### 2c. Delete the Webhook URL
Delete the `Webhook URL` by clicking on the `Delete` icon next to the Webhook URL. Confirm deletion by clicking the `Remove` button in the pop-up.
![](/images/slack-webhook/14.png)

---

## Best Practices

### A Webhook is a Password
Treat your Slack Webhook like you would any other password. 

---

## Resources
- [Slack Webhook Documentation](https://api.slack.com/messaging/webhooks)