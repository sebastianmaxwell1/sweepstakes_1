from marketing_firm import MarketingFirmCreator

class MarketingFirm:

    def __init__(self):
        self.manager = MarketingFirmCreator()

    def create_sweepstakes(self):
        sweep = self.manager.choose_manager()
        return sweep