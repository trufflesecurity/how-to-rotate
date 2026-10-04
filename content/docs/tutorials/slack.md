---
title: Slack
---

*This tutorial provides step-by-step instructions on how to rotate a Slack Configuration Token.*

---

## Identify the Slack Token Type

Slack uses different token prefixes for different token types. Use the prefix and the place where the token was issued to choose the correct rotation guide.

| Token prefix | Token type | Rotation guidance |
| --- | --- | --- |
| `xoxb-` | Bot token | Use the [Slack Bot Token](/docs/tutorials/slack-bot-token) guide. Consider adopting Slack token rotation so future bot access tokens expire and can be refreshed. If rotation is not possible, replacing the token requires `Revoke All OAuth Tokens` before reinstalling the app, which will break dependent workflows until the new token is deployed. |
| `xoxe.xoxb-` | Rotating bot access token | Use the [Slack Bot Token](/docs/tutorials/slack-bot-token) guide and rotate it with the paired `xoxe-` refresh token. |
| `xoxp-` | User token | Prefer migrating the app to Slack token rotation, then exchange the long-lived user token with `oauth.v2.exchange` and refresh it with `oauth.v2.access`. |
| `xoxe.xoxp-` | Rotating user access token or configuration access token | If this token came from an app OAuth flow, rotate it with the paired `xoxe-` refresh token. If it came from `Your App Configuration Tokens`, continue with this Slack Configuration Token guide. |
| `xoxe-` | Refresh token | Use the guide for the paired access token. For bot and user tokens, refresh with `oauth.v2.access`; for configuration tokens, generate a new token pair from `Your App Configuration Tokens`. |
| `xapp-` | App-level token | This repository does not yet have a dedicated app-level token guide. Review the app's `Basic Information` settings and Slack's token documentation. |
| `xwfp-` | Workflow token | These tokens are short-lived and automatically expire. Replace the exposed workflow run or secret storage path rather than trying to refresh the token. |
| Slack webhook URL | Incoming webhook | Use the [Slack Webhook](/docs/tutorials/slack-webhook) guide. |

For bot and user tokens, Slack token rotation is the recommended long-term remediation path. Token rotation replaces long-lived access tokens with short-lived access tokens and single-use refresh tokens, reducing the impact of future token exposure.

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
- [Slack Tokens Documentation](https://docs.slack.dev/authentication/tokens/)
- [Slack Token Rotation Documentation](https://docs.slack.dev/authentication/using-token-rotation/)
