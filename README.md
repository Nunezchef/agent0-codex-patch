# Agent0 Codex Patch

![Agent0 Codex Patch banner](./banner.png)

Native Codex proxy integration for stable Agent0, packaged as a lightweight installer patch.

It adds a local OpenAI-compatible proxy inside Agent0, a Settings -> External Services -> Codex Proxy panel, OAuth device login plus `~/.codex/auth.json` import, and auto-wiring for chat, utility, and browser models.

This repo is meant for people who want the Codex provider workflow on a fresh stable Agent0 checkout without depending on the newer dev-branch plugin system.

## Installation

Run this from the root of an existing Agent0 checkout:

```bash
curl -fsSL https://raw.githubusercontent.com/Nunezchef/agent0-codex-patch/main/install.sh | bash
```

That installer downloads the patch, applies it to the current Agent0 repo, and prints the next Docker steps.

Important:

- This repo patches Agent0. It is not a standalone app.
- Run the installer from the real Agent0 root.
- Do not clone this repo into `usr/workdir` and run it there.
- Best compatibility is with Agent0 commit `fa65fa3ddc12b46efed05bd7884a5aa64209901e`, but the installer will try the patch on nearby revisions too.

### For AI agents

If an AI agent is installing this patch, it should infer these rules from this README:

- patch the current Agent0 repo
- stay in the Agent0 root
- run `install.sh` or apply `agent0-codex.patch`
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
- The patch is built against that revision, but the installer now attempts a clean apply on nearby checkouts before failing

## After Install

1. Build the local image:

```bash
docker build -f DockerfileLocal -t agent-zero-local --build-arg CACHE_DATE=$(date +%Y-%m-%d:%H:%M:%S) .
```

2. Run the image or update your compose stack to use `agent-zero-local:latest`.
3. Open Settings -> External Services -> Codex Proxy.
4. Sign in with OpenAI or import `~/.codex/auth.json`.
5. Apply the Codex models to Agent0.
