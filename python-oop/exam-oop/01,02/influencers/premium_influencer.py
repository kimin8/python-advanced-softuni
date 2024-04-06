from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE: float = 0.85

    FOLLOWER_MULTIPLIER = {
        "HighBudgetCampaign": 1.5,
        "LowBudgetCampaign": 0.8
    }

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:
        result = campaign.budget * self.PAYMENT_PERCENTAGE
        return result

    def reached_followers(self, campaign_type: str) -> int:
        multiplier = self.FOLLOWER_MULTIPLIER[campaign_type]
        result = (self.followers * self.engagement_rate) * multiplier
        return int(result)
