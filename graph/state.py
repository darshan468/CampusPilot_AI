from typing import TypedDict, List, Dict, Any, Optional


class AgentState(TypedDict, total=False):
    """
    Shared state used across all CampusPilot AI agents.

    Every agent reads from and updates this shared state.
    """

    # =====================================================
    # User Request
    # =====================================================

    query: str
    action: str

    # =====================================================
    # Supervisor
    # =====================================================

    agents: List[str]
    current_agent: str

    execution_plan: List[Dict[str, Any]]

    reason: str
    confidence: float

    # =====================================================
    # Student Profile
    # =====================================================

    student: Dict[str, Any]

    # =====================================================
    # Conversation Memory
    # =====================================================

    memory: Dict[str, Any]

    # =====================================================
    # Study Planner
    # =====================================================

    study_plan: Optional[str]

    # =====================================================
    # Assignment Planner
    # =====================================================

    assignment_plan: Optional[str]

    # =====================================================
    # Timetable
    # =====================================================

    timetable: Optional[Any]

    day: str
    subject: str
    faculty: str
    start_time: str
    end_time: str
    room: str

    timetable_id: int
    updated_data: Dict[str, Any]

    # =====================================================
    # Placement
    # =====================================================

    placement: Optional[str]

    # =====================================================
    # Career Guidance
    # =====================================================

    career_plan: Optional[str]

    # =====================================================
    # RAG
    # =====================================================

    rag_response: Optional[str]

    # =====================================================
    # Agent Outputs
    # =====================================================

    responses: List[str]

    agent_results: Dict[str, Any]

    result: Any

    final_response: Optional[str]

    # =====================================================
    # Workflow Status
    # =====================================================

    status: str

    # =====================================================
    # Error Handling
    # =====================================================

    error: Optional[str]