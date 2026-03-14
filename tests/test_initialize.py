from __future__ import annotations

import tempfile
import textwrap
import unittest
from pathlib import Path

import initialize


class InitializePatchTests(unittest.TestCase):
    def write_temp(self, content: str) -> Path:
        tmp = tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8")
        tmp.write(content)
        tmp.flush()
        tmp.close()
        return Path(tmp.name)

    def test_patch_external_settings_inserts_codex_section_once(self) -> None:
        path = self.write_temp(
            textwrap.dedent(
                """
                <html>
                  <body>
                    <nav>
                      <ul>
                        <li>
                          <a href="#section-api-keys">
                            <span>API Keys</span>
                          </a>
                        </li>
                        <li>
                          <a href="#section-tunnel">
                            <span>Flare Tunnel</span>
                          </a>
                        </li>
                      </ul>
                    </nav>
                    <div id="section-api-keys" class="section"></div>
                    <div id="section-tunnel" class="section"></div>
                  </body>
                </html>
                """
            ).strip()
        )

        initialize._patch_external_settings(path)
        initialize._patch_external_settings(path)

        text = path.read_text(encoding="utf-8")
        self.assertEqual(text.count("#section-codex"), 1)
        self.assertIn('path="settings/external/codex.html"', text)

    def test_patch_model_providers_adds_codex_proxy_once(self) -> None:
        path = self.write_temp(
            textwrap.dedent(
                """
                chat:
                  openai:
                    name: OpenAI
                    litellm_provider: openai

                embedding:
                  openai:
                    name: OpenAI
                    litellm_provider: openai
                """
            ).strip()
        )

        initialize._patch_model_providers(path)
        initialize._patch_model_providers(path)

        text = path.read_text(encoding="utf-8")
        self.assertEqual(text.count("codex_proxy:"), 1)
        self.assertIn("name: OpenAI Codex Proxy", text)

    def test_patch_missing_key_banner_treats_codex_proxy_as_local(self) -> None:
        path = self.write_temp(
            textwrap.dedent(
                """
                class MissingApiKeyCheck:
                    LOCAL_PROVIDERS = ["ollama", "lm_studio"]
                """
            ).strip()
        )

        initialize._patch_missing_key_banner(path)
        initialize._patch_missing_key_banner(path)

        text = path.read_text(encoding="utf-8")
        self.assertIn('"codex_proxy"', text)
        self.assertEqual(text.count('"codex_proxy"'), 1)

    def test_patch_settings_store_hides_codex_proxy_from_generic_keys(self) -> None:
        path = self.write_temp(
            textwrap.dedent(
                """
                const model = {
                  get apiKeyProviders() {
                    const key = prov.value.toLowerCase();
                    if (seen.has(key)) return;
                  },
                };
                """
            ).strip()
        )

        initialize._patch_settings_store(path)
        initialize._patch_settings_store(path)

        text = path.read_text(encoding="utf-8")
        self.assertIn('if (key === "codex_proxy") return;', text)
        self.assertEqual(text.count('if (key === "codex_proxy") return;'), 1)


if __name__ == "__main__":
    unittest.main()
