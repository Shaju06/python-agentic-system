from crewai import Crew, Process
from agents import create_travel_agent
from tasks import create_tasks
from config import  TRIP_DURATION, BUDGET_STYLE

import os
from dotenv import load_dotenv
load_dotenv()

print("🇻🇳 Vietnam Travel Agent starting...\n")

itinerary_planner, food_explorer, budget_advisor = create_travel_agent()

tasks = create_tasks(itinerary_planner, food_explorer, budget_advisor, TRIP_DURATION, BUDGET_STYLE)

# Assemble the crew
crew = Crew(
    agents=[itinerary_planner, food_explorer, budget_advisor],
    tasks=tasks,
    process=Process.sequential,  # agents work one after another
    # verbose=True,
    tracing=True
)

# Run it!
result = crew.kickoff()

print("\n========== YOUR VIETNAM TRAVEL PLAN ==========\n")
print(result)