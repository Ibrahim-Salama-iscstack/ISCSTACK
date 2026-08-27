"""
MLAIO™ - Action & Interaction Orchestration
Part of AIControlStack™
Ensures decision from Agent 1 goes to Agent 2 before Agent 3
"""
class MLAIO:
    def __init__(self):
        self.expected_chain = ["risk-agent", "verification-agent", "execution-agent"]

    def orchestrate(self, current_agent: str, next_agent: str, decision: dict) -> dict:
        try:
            curr_idx = self.expected_chain.index(current_agent)
            next_idx = self.expected_chain.index(next_agent)
        except ValueError:
            return {"allowed": True, "reason": f"Custom chain: {current_agent} -> {next_agent}"}

        if next_idx != curr_idx + 1:
            return {
                "allowed": False,
                "reason": f"Orchestration violation: {current_agent} tried to jump to {next_agent}, must go to {self.expected_chain[curr_idx+1]} first. Decision {decision.get('id')} must follow chain {self.expected_chain}"
            }
        return {"allowed": True, "reason": f"Orchestration OK: {current_agent} -> {next_agent}"}
