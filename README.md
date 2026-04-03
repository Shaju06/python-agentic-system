# 🇻🇳 Travel Agent

A multi-agent AI system built with **CrewAI** and **Groq** that generates a fully personalised Vietnam travel plan — including a day-by-day itinerary, city-by-city food guide, and realistic budget breakdown — and exports everything to a styled PDF.

---

## How it works

Three specialised AI agents collaborate sequentially to produce your travel plan:

| Agent | Role |
|---|---|
| **Vietnam Itinerary Planner** | Crafts a day-by-day trip across cities, temples, beaches, and hidden gems |
| **Vietnamese Food Expert** | Recommends must-try dishes, street food spots, and local restaurants per city |
| **Vietnam Travel Budget Advisor** | Breaks down realistic daily costs for accommodation, food, transport, and activities |

Each agent is assigned a dedicated task. They run one after another (sequential process), and the combined output is printed to the terminal and optionally exported to a branded PDF report.

---

## Project structure

```
python-agentic-system/
├── agents.py          # Defines the three CrewAI agents
├── tasks.py           # Defines the task for each agent
├── crew.py            # Assembles and runs the crew
├── main.py            # Entry point — loads config and kicks off the crew
├── main-crew.py       # Alternative entry point
├── config.py          # Trip duration, budget style, and LLM model settings
├── pdf_generator.py   # Generates a styled PDF from agent outputs (ReportLab)
└── config/            # Additional configuration files
```

---

## Prerequisites

- Python 3.10+
- A [Groq](https://console.groq.com/) API key (for fast LLM inference)

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/Shaju06/python-agentic-system.git
cd python-agentic-system
```

**2. Install dependencies**

```bash
pip install crewai python-dotenv reportlab
```

**3. Create a `.env` file**

```env
GROQ_API_KEY=your_groq_api_key_here
```

**4. Configure your trip**

Edit `config.py` to set your trip duration and budget style:

```python
TRIP_DURATION = "14 days"
BUDGET_STYLE  = "mid-range"   # e.g. "budget", "mid-range", "luxury"
```

---

## Usage

Run the main entry point:

```bash
python main.py
```

The three agents will execute in sequence and print your complete Vietnam travel plan to the terminal.

To generate a PDF report, use the `pdf_generator.py` module after the crew has run — it produces a branded PDF with a teal header banner, an itinerary section, a food guide, and a budget breakdown table.

---

## Tech stack

- [CrewAI](https://github.com/joaomdmoura/crewAI) — multi-agent orchestration framework
- [Groq](https://groq.com/) — fast LLM inference
- [ReportLab](https://www.reportlab.com/) — PDF generation
- [python-dotenv](https://github.com/theskumar/python-dotenv) — environment variable management

---

## Example output

The crew produces three sections:

- **Itinerary** — a day-by-day plan covering which cities to visit, how many days to spend, top activities, and travel tips between cities
- **Food Guide** — per-city recommendations for must-try dishes, street food markets, and local restaurants
- **Budget Breakdown** — daily cost estimates for accommodation, meals, transport, and activities, plus money-saving tips and a total trip estimate

---

## License

This project is open source. Feel free to fork and adapt it for other destinations or use cases.
