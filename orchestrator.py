class Orchestrator:

    def build(self, task):

        workflow = []

        if "email" in task:
            workflow.append("email_api")

        if "identity" in task:
            workflow.append("identity_api")

        return workflow
