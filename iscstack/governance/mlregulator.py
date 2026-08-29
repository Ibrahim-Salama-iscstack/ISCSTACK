class MLRegulator:
    def __init__(self):
        self.name = "MLRegulator"
    def validate(self, model: dict) -> dict:
        return {"valid": True, "layer": self.name}
