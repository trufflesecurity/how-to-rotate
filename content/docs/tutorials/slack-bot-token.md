---
title: Slack Bot Token
---

*This tutorial provides step-by-step instructions on how to rotate a Slack Bot Token.*

---

## Generate a new Slack Bot Token

Slack bot tokens are issued when a Slack app is installed in a workspace. A long-lived bot token starts with `xoxb-`. If Slack token rotation is enabled for the app, the active bot access token starts with `xoxe.xoxb-` and is paired with a refresh token that starts with `xoxe-`.

### Step 1 - Navigate to the Slack App page
Log into your Slack workspace admin account and navigate to https://api.slack.com/apps/.
![](/images/slack/1.png)

### Step 2 - Confirm the token type
Select the affected Slack app and open `OAuth & Permissions`. In `OAuth Tokens for Your Workspace`, identify whether the leaked token is a long-lived `xoxb-` bot token or an expiring `xoxe.xoxb-` bot access token.

### Step 3 - Generate a replacement token

#### 3a. Rotate an app that already uses token rotation
If the app already stores a refresh token, call `oauth.v2.access` with `grant_type=refresh_token`. Use the app's `client_id` and `client_secret` from `Basic Information`. Store both the returned `access_token` and the returned `refresh_token`.

```sh
curl -X POST https://slack.com/api/oauth.v2.access \
  -u "<CLIENT_ID>:<CLIENT_SECRET>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "grant_type=refresh_token" \
  --data-urlencode "refresh_token=<REFRESH_TOKEN>"
```

The returned `access_token` expires after the number of seconds shown in `expires_in`. The refresh token used in the request is single-use, so update your secret store with the new refresh token from the response.

#### 3b. Migrate a long-lived bot token to token rotation
If the app still uses a long-lived `xoxb-` token, first make sure the app can refresh tokens before they expire. In the app's `OAuth & Permissions` settings, enable token rotation. Slack does not allow token rotation to be turned off after it is enabled.

Then call `oauth.v2.exchange` with the existing long-lived bot token, plus the app's `client_id` and `client_secret`. The client credentials are available in the app's `Basic Information` settings.

```sh
curl -X POST https://slack.com/api/oauth.v2.exchange \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "client_id=<CLIENT_ID>" \
  --data-urlencode "client_secret=<CLIENT_SECRET>" \
  --data-urlencode "token=<OLD_SLACK_BOT_TOKEN>"
```

Copy the returned `access_token` and `refresh_token`. The new access token will start with `xoxe.xoxb-`. Immediately perform the first refresh using the returned refresh token and the `oauth.v2.access` request shown above, then store the second response's `access_token` and `refresh_token`. Slack expires the original long-lived access token after the short-lived credentials are refreshed for the first time.

#### 3c. Reinstall if token rotation is not an option
If the app cannot support Slack token rotation yet, there is no no-downtime bot token replacement path. You must revoke the app's existing OAuth tokens before Slack will issue a new long-lived bot token.

In the app's `OAuth & Permissions` settings, use `Revoke All OAuth Tokens`, then reinstall the app to the workspace to obtain a new `xoxb-` bot token. This invalidates the current bot token before the replacement exists, so workflows and automations that depend on the bot token will break until the app is reinstalled and the new token is deployed everywhere.

Plan this path as an outage. Slack API calls, message posting, event handling, slash commands, workflow steps, and any other integration using the revoked token may fail during the rotation window. Reinstalling may also remove the bot user's channel memberships, so plan to invite the bot back to required channels after reinstalling.

---

## Replace the Leaked Slack Bot Token
Replace the leaked Slack Bot Token with the new token in all impacted applications and services.

If the app uses Slack token rotation, update the stored refresh token at the same time. Schedule token refreshes before the current `expires_in` window ends so the app does not continue using an expired bot access token.

---

## Revoke the Leaked Slack Bot Token

### Step 1 - Verify the old token
Use `auth.test` to confirm whether the old token still works.

```sh
curl -X POST https://slack.com/api/auth.test \
  -H "Authorization: Bearer <OLD_SLACK_BOT_TOKEN>"
```

If Slack returns `ok: false`, the token is no longer valid.

### Step 2 - Revoke the token if it is still active
If the leaked token is still active and the app uses Slack token rotation, call `auth.revoke`.

```sh
curl -X POST https://slack.com/api/auth.revoke \
  -H "Authorization: Bearer <LEAKED_SLACK_BOT_TOKEN>"
```

If the leaked token is a non-rotatable long-lived `xoxb-` bot token, revoke it from the app's `OAuth & Permissions` settings with `Revoke All OAuth Tokens`. This revokes the active OAuth tokens for the app installation before Slack issues a new bot token, so it will interrupt workflows until the app is reinstalled and the new token is deployed.

If you migrated a long-lived `xoxb-` token with `oauth.v2.exchange`, do not revoke the original token with `auth.revoke` unless you are prepared to reauthorize the app. Use `auth.test` to verify that the original token has stopped working.

---

## Best Practices

##### Enable Slack token rotation where possible
Slack token rotation replaces long-lived bot tokens with short-lived access tokens and single-use refresh tokens. Test the refresh flow in a development app before enabling token rotation in production.

##### Store the refresh token like a password
A refresh token can mint new bot access tokens. Store it in a secret manager, not in source code or local configuration files.

##### Limit bot token scopes
Review the app's `Bot Token Scopes` before reinstalling or exchanging tokens. Remove permissions that the app no longer needs.

---

## Resources
- [Slack Tokens Documentation](https://docs.slack.dev/authentication/tokens/)
- [Slack Token Rotation Documentation](https://docs.slack.dev/authentication/using-token-rotation/)
- [Slack oauth.v2.access Documentation](https://docs.slack.dev/reference/methods/oauth.v2.access/)
- [Slack oauth.v2.exchange Documentation](https://docs.slack.dev/reference/methods/oauth.v2.exchange/)
- [Slack auth.revoke Documentation](https://docs.slack.dev/reference/methods/auth.revoke/)
- [Slack auth.test Documentation](https://docs.slack.dev/reference/methods/auth.test/)
