from typing import List

from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer
from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    VALID_INFLUENCER_TYPES = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }

    VALID_CAMPAIGN_TYPES = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        influencer = self._get_influencer(username)
        if influencer is not None:
            return f"{username} is already registered."

        new_influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        campaign = self._get_campaign(campaign_id)
        if campaign is not None:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self._get_influencer(influencer_username)
        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        campaign = self._get_campaign(campaign_id)
        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        is_eligible = campaign.check_eligibility(influencer.engagement_rate)
        if not is_eligible:
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self) -> dict:
        campaign_follower_dict: dict = {}

        for campaign in self.campaigns:
            if campaign.approved_influencers:
                campaign_follower_dict[campaign] = (
                    sum(inf.reached_followers(campaign.__class__.__name__) for inf in campaign.approved_influencers)
                )

        return campaign_follower_dict

    def influencer_campaign_report(self, username: str) -> str:
        influencer = self._get_influencer(username)
        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."
        else:
            return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        new_line = '\n'
        reached_followers_dict = self.calculate_total_reached_followers()
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        report = f"$$ Campaign Statistics $${new_line}"
        campaign_infos = []
        for campaign in sorted_campaigns:
            campaign_infos.append(f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {reached_followers_dict[campaign]}")
        report += new_line.join(campaign_infos)
        return report

    def _get_influencer(self, influencer_username: str):
        influencer = [i for i in self.influencers if i.username == influencer_username]
        return influencer[0] if influencer else None

    def _get_campaign(self, c_id: int):
        campaign = [c for c in self.campaigns if c.campaign_id == c_id]
        return campaign[0] if campaign else None
