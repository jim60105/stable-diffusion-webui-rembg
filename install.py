import importlib.metadata

import launch
from packaging.version import Version

REMBG_VERSION = "2.0.85"


def rembg_outdated():
    try:
        return Version(importlib.metadata.version("rembg")) < Version(REMBG_VERSION)
    except importlib.metadata.PackageNotFoundError:
        return True


if rembg_outdated():
    launch.run_pip(f"install rembg=={REMBG_VERSION} --no-deps", "rembg")

for dep in ['onnxruntime', 'pymatting', 'pooch', 'scipy', 'scikit-image', 'jsonschema', 'tqdm']:
    if not launch.is_installed(dep):
        launch.run_pip(f"install {dep}", f"{dep} for REMBG extension")
