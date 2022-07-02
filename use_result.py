
class Nothing:
    def apply(self, game):
        pass


class TriggerMemory:
    def __init__(self, memory_name):
        self.memory_name = memory_name

    def apply(self, game):
        game.view.trigger_memory(self.memory_name)


class ConsumeItem:
    def __init__(self, item):
        self.item = item

    def apply(self, game):
        game.inventory.remove_item(self.item)


class ComposedUseResult:
    def __init__(self, results):
        self.results = results

    def apply(self, game):
        for result in self.results:
            result.apply(game)
