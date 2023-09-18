---
title: Twilio
---

*This tutorial provides step-by-step instructions on how to rotate a Twilio API key.*

---

## Promote a new Twilio API key

### Step 1 - Navigate to the API key page
Navigate to `Account` > `API keys and tokens`.

![](/images/twilio/2.png)

### Step 2 - Promote a new API key
#### 2a. Request a Secondary Token
Scroll to the bottom of the page and click the ` Request a Secondary Token` button.
#### 2b. Promote the new token to Primary
Click the `Promote to Primary` button next to the new token.
#### 2c. Confirm promotion

> **Note:** This will delete and revoke the old token.

![](/images/twilio/twilio_key_rotation.gif)


---

## Replace the Leaked Twilio API key
Replace the leaked Twilio API key with the new one in all impacted applications and services.


---

## Resources
- [Twilio API key Documentation](https://www.twilio.com/blog/better-twilio-authentication-csharp-twilio-api-keys)