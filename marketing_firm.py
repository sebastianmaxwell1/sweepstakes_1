from marketing_firm_creator import MarketingFirmCreator

class MarketingFirm:

    def __init__(self):
        self.manager = MarketingFirmCreator()

    def create_sweepstakes(self):
        sweep = self.manager.choose_manager()
        return sweep