import importlib
import inspect
import pkgutil

from agents.base_agent import BaseAgent


class PluginLoader:

    @staticmethod
    def discover(container):

        discovered = {}

        import agents

        for _, module_name, _ in pkgutil.iter_modules(
            agents.__path__
        ):

            if module_name in (
                "base_agent",
                "supervisor_agent",
                "merger_agent",
            ):
                continue

            module = importlib.import_module(
                f"agents.{module_name}"
            )

            for _, cls in inspect.getmembers(
                module,
                inspect.isclass
            ):

                if (
                    issubclass(cls, BaseAgent)
                    and cls != BaseAgent
                ):

                    try:

                        agent = cls(container)

                        discovered[
                            agent.agent_name
                        ] = agent

                    except Exception as e:

                        print(
                            f"Failed to load "
                            f"{cls.__name__}: {e}"
                        )

        return discovered