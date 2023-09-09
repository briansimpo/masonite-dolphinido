from masonite.packages import PackageProvider
from dolphinido.commands import *

class DolphinidoProvider(PackageProvider):

    def configure(self):
        self.root("dolphinido")\
        .name("dolphinido")\
        .config("config/fingerprint.py", publish=True)\
        .migrations(
            "migrations/create_audios_table.py", 
            "migrations/create_audio_fingerprints_table.py"
        )\
        .commands(
            FingerprintCommand,
            RadioCommand,
            RecogFileCommand,
            RecogMicCommand,
            RecogRadioCommand
        )

    def register(self):
        super().register()

    def boot(self):
        pass
