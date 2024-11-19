from typing import Union

import torch
from ccrestoration.util.device import default_device


def get_device(device: str) -> Union[torch.device, str]:
    """
    Get device from string

    :param device: device string
    """
    if device.startswith("auto"):
        return default_device()
    elif device.startswith("cpu"):
        return torch.device("cpu")
    elif device.startswith("cuda"):
        return torch.device("cuda")
    elif device.startswith("mps"):
        return torch.device("mps")
    elif device.startswith("directml"):
        import torch_directml

        return torch_directml.device()
    elif device.startswith("xpu"):
        return torch.device("xpu")
    else:
        print(f"Unknown device: {device}, use auto instead.")
        return default_device()
