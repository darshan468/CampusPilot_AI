from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for all CampusPilot tools.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def execute(self, **kwargs) -> Any:
        """
        Execute the tool.
        """
        pass

    def before_execute(self):
        print(f"[Tool] {self.name} started")

    def after_execute(self):
        print(f"[Tool] {self.name} completed")