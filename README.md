# Agent0 Codex Patch

Native Codex proxy integration for stable Agent0, packaged as a lightweight installer patch.

It adds a local OpenAI-compatible proxy inside Agent0, a Settings -> External Services -> Codex Proxy panel, OAuth device login plus `~/.codex/auth.json` import, and auto-wiring for chat, utility, and browser models.

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

## One-Line Install

Run this from the root of a clean Agent0 checkout:

```bash
curl -fsSL https://raw.githubusercontent.com/Nunezchef/agent0-codex-patch/main/install.sh | bash
```

## What It Adds

- Native runtime config at `usr/codex_provider.json`
- OAuth device flow and `auth.json` token import
- Local Codex proxy on `127.0.0.1:8400`
- Native backend endpoints for auth, status, and apply/disconnect
- Settings -> External Services -> Codex Proxy UI
- Auto-start proxy on each conversation
- Chat, utility, and browser model wiring through the proxy

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
