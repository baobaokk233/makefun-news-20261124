"""Copy the finished news image to the output directory.

The entry image, entry.png, sits next to this script. Running this
script copies it unchanged into the output directory, so the result
is byte-identical on every run.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise SystemExit("entry.png is missing next to main.py")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("copied entry.png differs in size from the source")


if __name__ == "__main__":
    main()
