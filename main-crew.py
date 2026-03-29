from crew import create_crew
from pdf_generator import generate_pdf


def main():
    print("🇻🇳 Vietnam Travel Agent starting...\n")

    duration = input("Enter your trip duration (e.g. '1 week', '10 days', '2 weeks'): ")
    budget = input("Enter your budget style (e.g. 'budget-conscious', 'mid-range', 'luxury'): ")

    print(f"\nPlanning your {duration} Vietnam trip on a {budget} budget...\n")

    crew = create_crew(duration, budget)
    result = crew.kickoff()

    itinerary_output = result.tasks_output[0].raw
    food_output      = result.tasks_output[1].raw
    budget_output    = result.tasks_output[2].raw

    print("\n=== Plan Ready — Generating PDF... ===\n")

    # ── Generate & save PDF locally ──
    pdf_buffer = generate_pdf(
        itinerary_output,
        food_output,
        budget_output,
        duration,
        budget
    )
    
    filename = f"vietnam_plan_{duration.replace(' ', '_')}.pdf"
    with open(filename, "wb") as f:
        f.write(pdf_buffer.read())

    print(f"✅ Travel plan saved as: {filename}")

    # print("\n========== YOUR VIETNAM TRAVEL PLAN ==========\n")
    # print(result)


if __name__ == "__main__":
    main()