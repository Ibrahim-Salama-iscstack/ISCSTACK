class AIGovCore:
    def __init__(self):
        self.revoked_operators = set()
    def revoke(self, operator_id):
        self.revoked_operators.add(operator_id)
    def is_revoked(self, operator_id):
        return operator_id in self.revoked_operators
    def check_policy(self, context):
        op = context.get("operator")
        if op and self.is_revoked(op):
            return {"allowed": False}
        return {"allowed": True}
