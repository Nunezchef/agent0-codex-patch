# Agent0 Codex Patch

![Agent0 Codex Patch banner](./banner.png)

Native Codex proxy integration for stable Agent0, packaged as a lightweight installer patch.

It adds a local OpenAI-compatible proxy inside Agent0, a Settings -> External Services -> Codex Proxy panel, OAuth device login plus `~/.codex/auth.json` import, and auto-wiring for chat, utility, and browser models.

This repo is meant for people who want the Codex provider workflow on a fresh stable Agent0 checkout without depending on the newer dev-branch plugin system.

## Installation

This repository is a patch source for an existing Agent0 checkout.

It is not a standalone app.

Important:

- Work from the root of the real Agent0 repository
- Do not run this repo from `usr/workdir`
- Do not treat this repo as a replacement for Agent0 itself
- Apply `agent0-codex.patch` to Agent0

### Correct install flow

1. Get a clean Agent0 checkout.
2. Make sure the checkout is at the supported commit:
   - `fa65fa3ddc12b46efed05bd7884a5aa64209901e`
3. Download this repo or at minimum download `agent0-codex.patch`.
4. From the root of the Agent0 repo, apply the patch:

```bash
git apply --check /path/to/agent0-codex.patch
git apply /path/to/agent0-codex.patch
```

5. Build and run Agent0 normally.
6. Open `Settings -> External Services -> Codex Proxy`.
7. Sign in with OpenAI or import `~/.codex/auth.json`.
8. Apply the Codex models.

### One-line installer

If you want an automated install, run this from the root of the Agent0 checkout:

```bash
curl -fsSL https://raw.githubusercontent.com/Nunezchef/agent0-codex-patch/main/install.sh | bash
```

### For AI agents

If an AI agent is installing this patch, it should infer these rules from this README:

- patch the current Agent0 repo
- stay in the Agent0 root
- verify the expected commit
- use `agent0-codex.patch`
- avoid running the patch repo as a standalone project

## Supported Models

- `gpt-5.3-codex`
- `gpt-5.2-codex`
- `gpt-5.1-codex`
- `gpt-5.1-codex-mini`
- `gpt-5.2`
- `gpt-5.1`

Recommended defaults:

- Chat: `gpt-5.3-codex`
- Utility: `gpt-5.1-codex-mini`
- Browser: `gpt-5.1-codex-mini`

## What It Adds

- Native runtime config at `usr/codex_provider.json`
- OAuth device flow and `auth.json` token import
- Local Codex proxy on `127.0.0.1:8400`
- Native backend endpoints for auth, status, and apply/disconnect
- Settings -> External Services -> Codex Proxy UI
- Auto-start proxy on each conversation
- Chat, utility, and browser model wiring through the proxy

## Credits

- Original Codex provider plugin concept and implementation: [protolabs42/codex-provider](https://github.com/protolabs42/codex-provider)
- Agent0 upstream project: [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)

This patch ports the Codex provider idea into the stable Agent0 architecture, replacing the missing dev-branch plugin runtime with native settings, APIs, and extension hooks.

## Compatibility

- Pinned Agent0 commit: `fa65fa3ddc12b46efed05bd7884a5aa64209901e`
- The installer intentionally fails on other revisions

## Install Flow

1. Clone or download Agent0 at the pinned commit.
2. Run the one-line installer from the Agent0 root.
3. Build the local image:

```bash
docker build -f DockerfileLocal -t agent-zero-local --build-arg CACHE_DATE=$(date +%Y-%m-%d:%H:%M:%S) .
```

4. Run the image or update your compose stack to use `agent-zero-local:latest`.
5. Open Settings -> External Services -> Codex Proxy.
6. Sign in with OpenAI or import `~/.codex/auth.json`.
7. Apply the Codex models to Agent0.
