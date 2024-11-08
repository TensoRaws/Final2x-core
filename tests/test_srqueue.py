from Final2x_core import SRConfig, sr_queue

from .util import CONFIG_PATH


class Test_SRQUEUE:
    def test_queue(self) -> None:
        config: SRConfig = SRConfig.from_yaml(CONFIG_PATH)
        config.target_scale = 1.14514
        sr_queue(config=config)
