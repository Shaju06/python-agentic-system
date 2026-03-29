from crewai import Agent
from config import LLM_MODEL


def create_travel_agent():
    """
    Creates a travel agent with specific instructions for planning a trip to Vietnam.
    """
    itinerary_planning_agent = Agent(
        role="Vietnam Itinerary Planner",
        goal="Create the best day-by-day travel plan for Vietnam",
         backstory="""You are an expert Vietnam travel planner with 10 years 
        of experience. You know every city, temple, beach and hidden gem. 
        You create practical, exciting itineraries that balance must-see 
        spots with off-the-beaten-path experiences.""",
        llm=LLM_MODEL,
        verbose=True,
        allow_delegation=False
    )

    food_explorer = Agent(
        role="Vietnamese Food Expert",
        goal="Guide travelers to the best authentic food experiences in Vietnam",
        backstory="""You are a Vietnamese food expert who has eaten at 
        thousands of street stalls and restaurants across the country. 
        You know exactly what to eat in each city, where locals go, 
        and what dishes tourists always miss.""",
        llm=LLM_MODEL,
        verbose=True,
        allow_delegation=False
    )

    budget_advisor = Agent(
        role="Vietnam Travel Budget Advisor",
        goal="Help travelers understand costs and save money in Vietnam",
        backstory="""You are a budget travel expert for Southeast Asia. 
        You know the real costs of accommodation, food, transport and 
        activities in Vietnam. You help travelers get the most value 
        without missing out on great experiences.""",
        llm=LLM_MODEL,
        verbose=True,
        allow_delegation=False
    )

    return itinerary_planning_agent, food_explorer, budget_advisor
