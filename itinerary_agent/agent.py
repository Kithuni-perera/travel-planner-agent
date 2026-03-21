# itinerary_agent/agent.py
# -----------------------------------------------
# ITINERARY AGENT
# This agent creates a day-by-day travel plan
# based on the destination and number of days.
# -----------------------------------------------

from google.adk.agents import LlmAgent

# Create the Itinerary Agent
# This agent only focuses on planning activities
root_agent = LlmAgent(
    # Name must match the folder name exactly
    name="itinerary_agent",

    # We use Gemini 2.0 Flash — it's FREE via Google AI Studio
    model="gemini-2.0-flash",

    # This is the system instruction — it tells the agent its job
    instruction="""
    You are an expert travel itinerary planner.
    
    Your job is to create a detailed day-by-day travel plan.
    
    When given a destination and number of days, you will:
    1. Suggest the best activities for each day
    2. Include morning, afternoon, and evening plans
    3. Recommend local food to try each day
    4. Add helpful travel tips (best time to visit each place, etc.)
    
    Format your response clearly like this:
    
    DAY 1:
    - Morning: [activity]
    - Afternoon: [activity]  
    - Evening: [activity]
    - Food tip: [local food recommendation]
    
    DAY 2:
    ... and so on
    
    Keep it practical, exciting, and realistic.
    """,

    description="Creates a detailed day-by-day travel itinerary with activities and food tips.",
)
