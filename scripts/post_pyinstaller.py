import shutil
from pathlib import Path

projectPATH = Path(__file__).resolve().parent.parent.absolute()


def post_pyinstaller() -> None:
    print("-" * 50)
    shutil.copy(projectPATH / "Final2x_core/config.yaml", projectPATH / "dist/Final2x-core/config.yaml")
    print("Copied config to dist folder~")

    print("-" * 50)


if __name__ == "__main__":
    post_pyinstaller()
