from swarmsync import AgentTeam, Agent, Task
from swarmsync.common import ModelFactory
from swarmsync.tools.tool_manager import ToolManager

def main():
    # Initialize the model factory
    model_factory = ModelFactory()
    
    # Create a team
    team = AgentTeam(
        name="example_team",
        description="A simple example team",
        rule="Work together to solve tasks efficiently",
        model=model_factory.get_model("gpt-4"),
        max_steps=10
    )
    
    # Create and add agents to the team
    researcher = Agent(
        name="researcher",
        system_prompt="You are a research specialist who gathers and analyzes information.",
        model=model_factory.get_model("gpt-4"),
        description="Research and analysis expert"
    )
    
    developer = Agent(
        name="developer",
        system_prompt="You are a software developer who implements solutions.",
        model=model_factory.get_model("gpt-4"),
        description="Software development expert"
    )
    
    # Add tools to agents
    tool_manager = ToolManager()
    browser_tool = tool_manager.create_tool("browser")
    if browser_tool:
        researcher.add_tool(browser_tool)
    
    # Add agents to team
    team.add(researcher)
    team.add(developer)
    
    # Create and run a task
    task = Task(content="Research the latest trends in AI and create a summary")
    result = team.run(task, output_mode="print")
    
    # Print the interaction diagram
    team.print_stepwise_interaction_diagram(result)

if __name__ == "__main__":
    main() 