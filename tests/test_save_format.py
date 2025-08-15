from Final2x_core import SRConfig, sr_queue

from .util import CONFIG_PATH


class Test_SAVE_FORMAT:
    def test_case_save_format(self) -> None:
        config: SRConfig = SRConfig.from_yaml(CONFIG_PATH)
        config.target_scale = 4
        for _format in [".png", ".jpg", ".webp", ".tiff"]:
            config.save_format = _format
            sr_queue(config=config)
