import pytest
from swarmsync import AgentTeam, Agent, Task
from swarmsync.common import ModelFactory
from swarmsync.tools.tool_manager import ToolManager

@pytest.fixture
def model_factory():
    return ModelFactory()

@pytest.fixture
def team(model_factory):
    return AgentTeam(
        name="test_team",
        description="Test team",
        rule="Test rule",
        model=model_factory.get_model("gpt-4"),
        max_steps=5
    )

@pytest.fixture
def agent(model_factory):
    return Agent(
        name="test_agent",
        system_prompt="Test system prompt",
        model=model_factory.get_model("gpt-4"),
        description="Test agent"
    )

def test_team_creation(team):
    assert team.name == "test_team"
    assert team.description == "Test team"
    assert team.rule == "Test rule"
    assert team.max_steps == 5

def test_agent_creation(agent):
    assert agent.name == "test_agent"
    assert agent.system_prompt == "Test system prompt"
    assert agent.description == "Test agent"

def test_team_agent_addition(team, agent):
    team.add(agent)
    assert len(team.agents) == 1
    assert team.agents[0].name == "test_agent"

def test_task_creation():
    task = Task(content="Test task")
    assert task.content == "Test task"

def test_tool_manager():
    tool_manager = ToolManager()
    browser_tool = tool_manager.create_tool("browser")
    assert browser_tool is not None 