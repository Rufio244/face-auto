class Sandbox:

    def __init__(self, registry):
        self.registry = registry

    def execute(self, workflow, data):

        results = []

        for api in workflow:

            func = self.registry.get(api)

            if func:
                try:
                    results.append(func(data))
                except Exception as e:
                    results.append({"error": str(e), "api": api})

        return results
