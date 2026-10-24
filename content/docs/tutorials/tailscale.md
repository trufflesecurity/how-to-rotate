---
title: Tailscale
---

*This tutorial provides step-by-step instructions on how to rotate Tailscale Auth Keys and API Access Tokens.*

---

## Generate a new Tailscale Auth Key or API Access Token

### Step 1 - Navigate to the Keys page
Keys page found at <https://login.tailscale.com/admin/settings/keys>

As an administrator, click on "Settings" under the top navbar. Then click "Keys" under "Personal Settings" on the left-hand navbar.

![](/images/tailscale/1.png)

### Step 2 - Generate a new Auth Key or API Access Token
#### Step 2a - Click "Generate..."
Click on the "Generate..." button under the "Auth Keys" or "API Access Tokens" section.
#### Step 2b - Configure the Key
The API Access Token provides users with two settings: `description` and `expiration`. Fill out those values and then click `Generate access token`.

![](/images/tailscale/2.png)

The Auth Key provides users with four settings: `description`, `reusability`, `expiration`, and `device settings`. Fill those out and then click `Generate key`.

![](/images/tailscale/3.png)

#### Step 2c - Copy the Key

![](/images/tailscale/4.png)

---

## Replace the Leaked Tailscale Auth Keys and API Access Tokens
Replace the leaked Tailscale Auth Key or API Access Token with the new one in all impacted applications and services.

---

## Revoke the Leaked Tailscale Auth Keys and API Access Tokens

### Step 1 - Navigate to the Keys page
Keys page found at <https://login.tailscale.com/admin/settings/keys>Keys page found at <https://login.tailscale.com/admin/settings/keys>

As an administrator, click on "Settings" under the top navbar. Then click "Keys" under "Personal Settings" on the left-hand navbar.

![](/images/tailscale/1.png)

### Step 2 - Revoke the Auth Keys and API Access Tokens
Click the `Revoke` button next to the leaked Auth Key or API Access Token.

![](/images/tailscale/5.png)

---

## Best Practices

##### Delegate Fine-grained Control with OAuth Clients
As an alternative to an access token that has full permission to the Tailscale API, use OAuth clients to provide delegated fine-grained control to the Tailscale API.

---

## Resources
- [Tailscale Auth Keys Documentation](https://tailscale.com/kb/1085/auth-keys/)
- [Tailscale API Keys Documentation](https://tailscale.com/kb/1101/api/)
- [Learn about Key Management in the Tailscale Control Protocol](https://tailscale.com/blog/tailscale-key-management/)
