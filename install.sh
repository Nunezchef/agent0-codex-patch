#!/usr/bin/env bash
set -euo pipefail

EXPECTED_COMMIT="fa65fa3ddc12b46efed05bd7884a5aa64209901e"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PATCH_FILE="$SCRIPT_DIR/agent0-codex.patch"

fail() {
  echo "Error: $1" >&2
  exit 1
}

if [[ ! -d .git || ! -f run_ui.py || ! -d python || ! -d webui ]]; then
  fail "Run this from the root of a fresh Agent0 checkout."
fi

if [[ ! -f "$PATCH_FILE" ]]; then
  fail "Patch file not found at $PATCH_FILE."
fi

if [[ "$(git rev-parse HEAD)" != "$EXPECTED_COMMIT" ]]; then
  fail "This installer is pinned to Agent0 commit $EXPECTED_COMMIT."
fi

if ! git diff --quiet || ! git diff --cached --quiet || [[ -n "$(git ls-files --others --exclude-standard)" ]]; then
  fail "The Agent0 checkout must be clean before applying this patch."
fi

if git apply --reverse --check "$PATCH_FILE" >/dev/null 2>&1; then
  echo "Patch already applied. Nothing to do."
else
  git apply --check "$PATCH_FILE" || fail "Patch cannot be applied cleanly."
  git apply "$PATCH_FILE"
  echo "Patch applied successfully."
fi

cat <<'EOF'

Next steps:
1. docker build -f DockerfileLocal -t agent-zero-local --build-arg CACHE_DATE=$(date +%Y-%m-%d:%H:%M:%S) .
2. Run the local image or update your compose stack to use agent-zero-local:latest.
3. Open Settings -> External Services -> Codex Proxy.
4. Sign in with OpenAI or import ~/.codex/auth.json.
5. Apply the Codex models to Agent0.
EOF
