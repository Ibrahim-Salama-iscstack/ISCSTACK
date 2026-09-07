from ..control.mlver import MLVer
from ..core.aigov import AIGovCore

class APIRegulator:
    def __init__(self):
        self.verifier = MLVer()
        self.gov = AIGovCore()
        self._revoked = set()
    def revoke(self, operator_id):
        self._revoked.add(operator_id)
        self.gov.revoke(operator_id)
    def intercept(self, context):
        op = context.get("operator") or context.get("env", "unknown")
        if op in self._revoked or self.gov.is_revoked(op):
            return {"decision": "BLOCKED", "reason": "AuthorityRevoked", "audit": {"operator": op}}
        v = self.verifier.verify(context)
        if not v.get("verified"):
            return {"decision": "BLOCKED", "reason": v.get("reason")}
        return {"decision": "ALLOWED", "audit": {"operator": op}}
