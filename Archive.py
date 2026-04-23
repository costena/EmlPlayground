import os.path

import yaml


class Archive:
    def __init__(self):
        self.filePath = 'save.yaml'

    def dump(self, inventoryWidget, taskWidget):
        with open(self.filePath, 'w') as f:
            yaml.dump({
                'inventory': inventoryWidget.dump(),
                'task': taskWidget.dump(),
            }, f, yaml.Dumper)

    def load(self, inventoryWidget, taskWidget):
        if not os.path.exists(self.filePath):
            return
        with open(self.filePath, 'r') as f:
            data = yaml.load(f, yaml.Loader)
        inventoryWidget.load(data['inventory'])
        taskWidget.load(data['task'])
