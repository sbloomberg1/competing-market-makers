from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class RoundInput(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    episodes: Literal[256, 2048, 8192] = 8192
    batch_size: Literal[256] = 256
    deadline_ms: Literal[100] = 100


if __name__ == "__main__":
    import json
    from pathlib import Path
    Path("input.schema.json").write_text(json.dumps(RoundInput.model_json_schema(), indent=2) + "\n")
