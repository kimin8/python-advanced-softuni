from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    BUDGET: float = 5000.0
    ENGAGEMENT_RATE_MULTIPLIER: float = 1.2

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, self.BUDGET, required_engagement)

    def check_eligibility(self, engagement_rate: float) -> bool:
        return engagement_rate >= self.required_engagement * self.ENGAGEMENT_RATE_MULTIPLIER
