from crewai import Task

def create_tasks(itinerary_planner, food_explorer, budget_advisor, duration, budget):

    plan_itinerary = Task(
        description=f"""Create a detailed {duration} Vietnam itinerary for a 
        {budget} traveler. Include: which cities to visit, how many days in 
        each, top 3 things to do per city, best time to travel between cities, 
        and any important travel tips.""",
        expected_output="A clear day-by-day itinerary with cities, activities and travel tips",
        agent=itinerary_planner
    )

    food_guide = Task(
        description=f"""Create a Vietnam food guide for a {duration} trip. 
        For each major city in the itinerary, list: 3 must-try dishes, 
        where to find the best street food, one local restaurant recommendation, 
        and any food safety tips.""",
        expected_output="A city-by-city food guide with dishes, locations and tips",
        agent=food_explorer
    )

    budget_breakdown = Task(
        description=f"""Create a realistic daily budget breakdown for a {budget} 
        traveler in Vietnam for {duration}. Include costs for: accommodation, 
        meals, local transport, activities, and a total trip estimate. 
        Add 3 money-saving tips.""",
        expected_output="A clear budget table with daily costs and total trip estimate",
        agent=budget_advisor
    )

    return [plan_itinerary, food_guide, budget_breakdown]