from registry import registry
from orchestrator import Orchestrator
from sandbox import Sandbox
from scanzaclip import scanzaclip

class FaceAuto:

    def __init__(self):
        self.orchestrator = Orchestrator()
        self.sandbox = Sandbox(registry)

    def run(self, request):

        task = request["input"]

        decision = scanzaclip(task)

        workflow = self.orchestrator.build(task)

        result = self.sandbox.execute(workflow, request)

        return {
            "decision": decision,
            "workflow": workflow,
            "result": result
        }
