# Agent0 Codex Patch

![Agent0 Codex Patch banner](./banner.png)

Native Codex proxy integration for stable Agent0, packaged as a lightweight installer patch.

It adds a local OpenAI-compatible proxy inside Agent0, a Settings -> External Services -> Codex Proxy panel, OAuth device login plus `~/.codex/auth.json` import, and auto-wiring for chat, utility, and browser models.

This repo is meant for people who want the Codex provider workflow on a fresh stable Agent0 checkout without depending on the newer dev-branch plugin system.

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

If you want to use the installer script, run it from the root of a clean Agent0 checkout:

```bash
curl -fsSL https://raw.githubusercontent.com/Nunezchef/agent0-codex-patch/main/install.sh | bash
```

## Recommended Install Method

Use these manual steps from the root of the real Agent0 checkout.

Do not clone this patch repo into `usr/workdir` and run `install.sh` there. The patch must be applied from the root of Agent0 itself, where files like `run_ui.py`, `python/`, and `webui/` already exist.

### 1. Get Agent0 at the pinned commit

```bash
git clone https://github.com/Nunezchef/agent-zero.git
cd agent-zero
git checkout fa65fa3ddc12b46efed05bd7884a5aa64209901e
```

### 2. Download the patch

```bash
curl -fsSL https://raw.githubusercontent.com/Nunezchef/agent0-codex-patch/main/agent0-codex.patch -o /tmp/agent0-codex.patch
```

### 3. Apply the patch from the Agent0 root

```bash
git apply --check /tmp/agent0-codex.patch
git apply /tmp/agent0-codex.patch
```

### 4. Build the local image

```bash
docker build -f DockerfileLocal -t agent-zero-local --build-arg CACHE_DATE=$(date +%Y-%m-%d:%H:%M:%S) .
```

### 5. Run Agent0 and configure Codex

1. Start the image or update your compose stack to use `agent-zero-local:latest`
2. Open Settings -> External Services -> Codex Proxy
3. Sign in with OpenAI or import `~/.codex/auth.json`
4. Apply the Codex models to Agent0

## Agent Instructions

If you are asking another coding agent to install this patch, give it these instructions:

```text
You are patching an existing Agent0 checkout.

Important:
- Do not clone the patch repo into usr/workdir and run install.sh there.
- Work only from the root of the actual Agent0 repository.
- Verify the checkout is at commit fa65fa3ddc12b46efed05bd7884a5aa64209901e.
- Download https://raw.githubusercontent.com/Nunezchef/agent0-codex-patch/main/agent0-codex.patch to a temp path.
- Run git apply --check on the patch first.
- Then run git apply.
- After patching, build Docker with DockerfileLocal.
```

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
