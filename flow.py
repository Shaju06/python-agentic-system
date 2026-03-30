from crewai.flow.flow import Flow, listen, start, router, or_
from pydantic import BaseModel
from crew import create_crew

class TripState(BaseModel): 
    duration: str = "2 weeks"
    budget: str = "mid-range"
    needs_visa_info: bool = False
    itinerary: str = ""
    final_plan: str = ""


class VietnamTravelFlow(Flow[TripState]): 

    @start
    def get_user_input(self):
        print("\n🇻🇳 Welcome to Vietnam Travel Agent!\n")
        
        duration = input("How many days? (e.g. 7): ")
        budget = input("Budget style? (budget/mid-range/luxury): ")
        
        # save to state — accessible everywhere in flow
        self.state.duration = f"{duration} days"
        self.state.budget = budget
        self.state.needs_visa_info = int(duration) > 14

    @router(get_user_input)
    def check_trip_type(self):
        if self.state.budget == "budget":
            return "budget_route"
        elif self.state.budget == "luxury":
            return "luxury_route"
        else:
            return "midrange_route"

    @listen("budget_route")
    def handle_budget_trip(self):
        print("\n🎯 Budget trip detected — optimising for value...\n")
        crew = create_crew(
            duration=self.state.duration,
            budget="budget"
        )
        result = crew.kickoff()
        self.state.final_plan = str(result)

    @listen("luxury_route")
    def handle_luxury_trip(self):
        print("\n✨ Luxury trip detected — going premium...\n")
        crew = create_crew(duration=self.state.duration, budget="luxury")
        result = crew.kickoff()
        self.state.final_plan = str(result)

    @listen('midrange_route')
    def handle_midrange_trip(self):
        print("\n🎯 Mid-range trip — best of both worlds...\n")
        crew = create_crew(
            duration=self.state.duration,
            budget="mid-range"
        )
        result = crew.kickoff()
        self.state.final_plan = str(result)

    @listen(or_(handle_budget_trip, handle_luxury_trip, handle_midrange_trip))
    def check_visa(self):
        # this runs after ANY of the three above finish
        if self.state.needs_visa_info:
            print("\n⚠️  Trip is over 14 days — adding visa information...\n")
            print("Vietnam visa on arrival: 45 days max for most nationalities")
            print("E-visa available at: evisa.xuatnhapcanh.gov.vn")

    @listen(check_visa)
    def save_plan(self):
        # save final plan to a file
        with open("my_vietnam_plan.txt", "w") as f:
            f.write(self.state.final_plan)
        print("\n✅ Your travel plan saved to my_vietnam_plan.txt!")
        print("\n========== YOUR VIETNAM TRAVEL PLAN ==========\n")
        print(self.state.final_plan)
