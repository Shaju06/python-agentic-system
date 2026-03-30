# import sys
# from crew import create_crew

# duration = sys.argv[1] if len(sys.argv) > 1 else "7"
# budget = sys.argv[2] if len(sys.argv) > 2 else "mid-range"

# print(f"\n🇻🇳 Vietnam Travel Agent starting...")
# print(f"📅 Duration: {duration} days | 💰 Budget: {budget}\n")

# crew = create_crew(duration=f"{duration} days", budget=budget)
# result = crew.kickoff()

# print("\n========== YOUR VIETNAM TRAVEL PLAN ==========\n")
# print(result)

from flow import VietnamTravelFlow

flow = VietnamTravelFlow()
flow.kickoff()