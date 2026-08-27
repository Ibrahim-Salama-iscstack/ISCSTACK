"""
APIRegulator™ - Execution Boundary Enforcement (Commit Node)
Part of ISCGovernance™
BLOCK / ALLOW + Authority Receipt
"""
class APIRegulator:
    def __init__(self, aigovcore, mlregulator):
        self.aigovcore = aigovcore
        self.mlregulator = mlregulator

    def intercept(self, agent_id: str, action: str, decision: dict, policy_name: str = "no_prod_delete"):
        auth = self.mlregulator.has_authority(agent_id, action)
        if not auth["allowed"]:
            return {"status": "BLOCKED", "layer": "MLRegulator™", "receipt": auth}
        policy = self.aigovcore.load_policy(policy_name)
        if action == "delete_db" and "marketing" in agent_id:
            return {"status": "BLOCKED", "layer": "APIRegulator™", "receipt": {"reason": f"Violates policy: {policy}"}}
        return {"status": "ALLOWED", "layer": "APIRegulator™", "receipt": {"authority": auth, "policy": policy, "decision_id": decision.get("id")}}

    def enforce(self, *args, **kwargs):
        return self.intercept(*args, **kwargs)
