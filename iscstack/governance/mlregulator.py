"""
MLRegulator™ - Regulatory Mediation & Authority Check
Part of ISCGovernance™
Answers: Does this agent have authority or did permission leak?
"""
class MLRegulator:
    def __init__(self):
        self.authority_matrix = {
            "marketing-agent": ["create_campaign", "analyze_data"],
            "devops-agent": ["delete_db", "restart_service"],
            "risk-agent": ["evaluate_risk"],
            "verification-agent": ["verify_decision"],
            "execution-agent": ["execute_api"]
        }

    def has_authority(self, agent_id: str, action: str) -> dict:
        allowed = self.authority_matrix.get(agent_id, [])
        if action not in allowed:
            return {
                "allowed": False,
                "reason": f"Authority mismatch: agent '{agent_id}' cannot perform '{action}'. Permission belongs to another agent.",
                "expected_owner": [k for k,v in self.authority_matrix.items() if action in v]
            }
        return {"allowed": True, "reason": "Authority verified"}

    def validate(self, agent_id, action):
        result = self.has_authority(agent_id, action)
        if not result["allowed"]:
            raise PermissionError(result["reason"])
        return result
