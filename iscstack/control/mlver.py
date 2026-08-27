"""
MLVer™ - Machine Learning Verification
Part of AIControlStack™
"""
class MLVer:
    def verify(self, decision: dict) -> dict:
        if not decision.get("id"):
            return {"verified": False, "reason": "Missing decision id"}
        if decision.get("confidence", 0) < 0.5:
            return {"verified": False, "reason": "Low confidence"}
        return {"verified": True, "reason": "Decision logically consistent"}
    def is_valid(self, decision):
        return self.verify(decision)["verified"]
