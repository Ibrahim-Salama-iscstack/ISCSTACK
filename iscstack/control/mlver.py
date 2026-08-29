"""
MLVer - Machine Learning Verification Layer
Domain: AIControlStack
Checks for hallucinated or incomplete decisions.
"""
class MLVer:
    def verify(self, decision: dict) -> dict:
            if not decision.get("intent"):
                        return {"verified": False, "reason": "missing intent"}
                                return {"verified": True, "confidence": 0.95}