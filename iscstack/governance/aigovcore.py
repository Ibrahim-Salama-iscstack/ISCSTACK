"""
AIGovCore - Policy Definition Layer
Defines which actions are allowed.
"""
class AIGovCore:
    def __init__(self):
            self.policies = {"block_delete_prod": True}

                def check_policy(self, action: dict) -> bool:
                        if action.get("intent") == "delete_db" and action.get("env") == "prod":
                                    return False
                                            return True