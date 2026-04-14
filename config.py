import os
from pathlib import Path


def _load_local_env(env_path: Path) -> None:
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def get_settings() -> tuple[str, str]:
    _load_local_env(Path(__file__).with_name(".env"))

    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip() or "gpt-4o-mini"

    if not api_key or api_key == "put_your_openai_api_key_here":
        raise RuntimeError(
            "OPENAI_API_KEY missing. Add real key in .env file (OPENAI_API_KEY=...)"
        )

    return api_key, model
