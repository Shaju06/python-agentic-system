from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import yaml
import os

load_dotenv()

def load_yaml(path):
    with open(path, 'r') as file:
        return yaml.safe_load(file)
    

def create_crew(duration, budget):
    agent_config = load_yaml('config/agents.yaml')
    task_config = load_yaml('config/tasks.yaml')
    agents = []
    for agent_info in agent_config['agents']:
        agent = Agent(
            **agent_info,
            # goal=agent_info['goal'],
            # backstory=agent_info['backstory'],
            llm=LLM(model=os.getenv("LLM_MODEL"), temperature=0.7),
            verbose=True,
            allow_delegation=False
        )
        agents.append(agent)

    tasks = []
    for i, task_info in enumerate(task_config['tasks']):
        assigned_agent = next((
            a for a in agents if a.role == task_info['agent_role']
        ),
        None)
        
        if assigned_agent is None:
            raise ValueError(f"No agent found with role {task_info['agent_role']} for task {task_info['description']}")


        task = Task(
            description=task_info['description'].format(duration=duration, budget=budget),
            expected_output=task_info['expected_output'],
            agent=assigned_agent,
            context=tasks[:i] if i > 0 else []
        )
        tasks.append(task)

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        tracing=True
        # memory=True
    )
    
    return crew