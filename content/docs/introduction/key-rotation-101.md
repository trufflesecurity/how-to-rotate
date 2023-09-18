---
title: Key Rotation 101
weight: 2
---

***

## What is a leaked secret/key?
A non-public password or credential accessible to an unauthorized entity. 

### How often does this happen?
Very, very often. We recently launched [Forager](https://forager.trufflesecurity.com), a public secret scanning tool, which monitors event feeds from NPM and GitHub to identify leaked keys. We found **0.1%** of ALL pushes to GitHub contain a valid leaked secret. [Our research into the Alexa Top 1 Million sites](https://trufflesecurity.com/blog/4500-of-the-top-1-million-websites-leaked-source-code-secrets/) revealed a similarly unexpected discovery. Hundreds of valid API keys, including root AWS keys and admin GitHub tokens, were freely accessible on the internet’s most visited websites.  

### What are the security implications of a leaked secret?
Depending on the permissions and third-party services involved, a leaked key could provide attackers with the means to orchestrate sophisticated social engineering campaigns or gain control over your entire online infrastructure. 

Remediating leaked API keys and tokens requires a systematic and efficient approach. The most secure way to remediate a leaked secret is key rotation.

---

## What is Key Rotation?
Key rotation refers to the process of (1) generating a new API key, (2) rendering the compromised key obsolete, and (3) updating the associated systems with the new key (like your CI/CD pipeline). This practice helps minimize the impact of an exposed API key or password.

> **Important:** Before you rotate an API key, it's important to ensure you don't disrupt any applications/services using that API key. Review which applications/services use the affected API, and make sure you have the appropriate permissions to change the API key once rotated.

### Can I just delete the code exposing the key?

No. We wrote [an entire article](https://trufflesecurity.com/blog/remediate-leaked-api-keys-with-key-rotation/) explaining why this approach is insufficient.

### What about editing Git history?

Again, this approach is insufficient. First, an attacker might already have your key. Removing it from Git history doesn't fix that. Second, some mirrors might already have a copy of your vulnerable code and editing the git history won't force them to edit their version. Third, if you work on a development team with more than a few developers, ask them what they think about force pushing changes to Git history. They'll most likely roll their eyes, since it can cause all types of conflicts and issues.
