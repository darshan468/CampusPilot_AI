from graph.agent_manager import AgentManager

from services.database_service import DatabaseService
from services.llm_service import LLMService
from services.rag_service import RAGService

from repositories.student_repository import StudentRepository
from repositories.study_repository import StudyRepository
from repositories.assignment_repository import AssignmentRepository
from repositories.placement_repository import PlacementRepository

from tools.study_tool import StudyTool
from tools.assignment_tool import AssignmentTool
from tools.placement_tool import PlacementTool
from tools.rag_tool import RAGTool

from agents.study_agent import StudyAgent
from agents.assignment_agent import AssignmentAgent
from agents.placement_agent import PlacementAgent
from agents.rag_agent import RAGAgent


class ServiceContainer:
    """
    ==========================================================
    CampusPilot AI - Dependency Injection Container
    ==========================================================

    Responsibilities
    ----------------
    • Initialize Services
    • Initialize Repositories
    • Initialize Tools
    • Initialize Agents
    • Register Agents with AgentManager
    """

    def __init__(self):

        try:

            # ==================================================
            # SERVICES
            # ==================================================

            self.database = DatabaseService()
            self.llm = LLMService()
            self.rag = RAGService()

            # ==================================================
            # REPOSITORIES
            # ==================================================

            self.student_repository = StudentRepository(
                self.database
            )

            self.study_repository = StudyRepository(
                self.database
            )

            self.assignment_repository = AssignmentRepository(
                self.database
            )

            self.placement_repository = PlacementRepository(
                self.database
            )

            # ==================================================
            # TOOLS
            # ==================================================

            self.study_tool = StudyTool(
                self.study_repository,
                self.llm
            )

            self.assignment_tool = AssignmentTool(
                self.assignment_repository,
                self.llm
            )

            self.placement_tool = PlacementTool(
                self.placement_repository,
                self.llm
            )

            self.rag_tool = RAGTool(
                self.rag
            )

            # ==================================================
            # AGENTS
            # ==================================================

            self.study_agent = StudyAgent(
                self.study_tool
            )

            self.assignment_agent = AssignmentAgent(
                self.assignment_tool
            )

            self.placement_agent = PlacementAgent(
                self.placement_tool
            )

            self.rag_agent = RAGAgent(
                self.rag_tool
            )

            # ==================================================
            # AGENT MANAGER
            # ==================================================

            self.agent_manager = AgentManager()

            self.agents = {

                "study": self.study_agent,

                "assignment": self.assignment_agent,

                "placement": self.placement_agent,

                "rag": self.rag_agent,

            }

            for name, agent in self.agents.items():

                self.agent_manager.register(
                    name,
                    agent
                )

        except Exception as e:

            raise RuntimeError(
                f"ServiceContainer initialization failed: {e}"
            )