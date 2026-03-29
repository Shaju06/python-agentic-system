import os
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL")

TRIP_DURATION = 7  # Duration of the trip in days
BUDGET_STYLE = "mid-range"
DESTINATION = "Vietnam"