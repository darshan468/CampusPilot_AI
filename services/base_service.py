from abc import ABC


class BaseService(ABC):
    """
    Base class for all CampusPilot services.
    """

    def __init__(self, service_name: str):
        self.service_name = service_name

    def log(self, message: str):
        print(f"[{self.service_name}] {message}")