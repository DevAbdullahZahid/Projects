# Orchestrator to manage the agents
from agents.requirement_analysis_agent import RequirementAnalysisAgent
from agents.proposal_generation_agent import ProposalGenerationAgent
from agents.communication_agent import CommunicationAgent
from agents.project_planning_agent import ProjectPlanningAgent
from agents.relationship_management_agent import RelationshipManagementAgent
from agents.market_intelligence_agent import MarketIntelligenceAgent

class Orchestrator:
    def __init__(self):
        self.requirement_analysis = RequirementAnalysisAgent()
        self.proposal_generation = ProposalGenerationAgent()
        self.communication = CommunicationAgent()
        self.project_planning = ProjectPlanningAgent()
        self.relationship_management = RelationshipManagementAgent()
        self.market_intelligence = MarketIntelligenceAgent()

    def execute_workflow(self, client_data):
        # Step 1: Requirement Analysis
        analysis = self.requirement_analysis.parse_requirements(client_data)
        
        # Step 2: Proposal Generation
        proposal = self.proposal_generation.generate_proposal(analysis)
        
        # Step 3: Project Planning
        project_plan = self.project_planning.plan_project(proposal)
        
        # Step 4: Market Intelligence
        market_analysis = self.market_intelligence.analyze_market()
        
        # Step 5: Relationship Management
        relationship_status = self.relationship_management.manage_client(client_data['name'])
        
        # Step 6: Communication
        communication_status = self.communication.communicate("Proposal sent")
        
        return {
            "analysis": analysis,
            "proposal": proposal,
            "project_plan": project_plan,
            "market_analysis": market_analysis,
            "relationship_status": relationship_status,
            "communication_status": communication_status
        }
