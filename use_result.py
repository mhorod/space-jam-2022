
class Nothing:
    def apply(self, game):
        pass


class TriggerMemory:
    def __init__(self, memory_name):
        self.memory_name = memory_name

    def apply(self, game):
        game.view.trigger_memory(self.memory_name)


class ConsumeItem:
    def __init__(self, item_name):
        self.item_name = item_name

    def apply(self, game):
        game.inventory.remove_item(self.item_name)
