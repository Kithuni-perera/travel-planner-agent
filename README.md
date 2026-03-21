# ✈ AI Travel Planner — Multi-Agent System

A multi-agent AI application built with **Google ADK** and **Gemini 2.0 Flash** that creates complete travel plans using specialized AI agents working together.

---

## What It Does

You type: *"Plan a 5-day trip to Tokyo with a mid-range budget"*

The system returns:
- 📅 A full day-by-day itinerary with activities and food tips
- 🏨 Hotel recommendations at 3 price points
- 💰 A detailed budget breakdown with money-saving tips

---

## Architecture

```
User Input
    │
    ▼
Coordinator Agent (main brain)
    │
    ├──► Itinerary Agent  → Day-by-day activities
    ├──► Hotel Agent      → Accommodation options  
    └──► Budget Agent     → Cost breakdown
    │
    ▼
Complete Travel Plan
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Programming language |
| Google ADK | Agent Development Kit |
| Gemini 2.0 Flash | Free AI model (via AI Studio) |
| VS Code | Code editor |

---

## Project Structure

```
travel_planner_agent/
│
├── coordinator_agent/       # Main agent — talks to user & delegates
│   ├── __init__.py
│   └── agent.py
│
├── itinerary_agent/         # Builds day-by-day travel plan
│   ├── __init__.py
│   └── agent.py
│
├── hotel_agent/             # Suggests accommodation options
│   ├── __init__.py
│   └── agent.py
│
├── budget_agent/            # Calculates cost breakdown
│   ├── __init__.py
│   └── agent.py
│
├── .env                     # Your API key (never share this!)
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## Setup & Run

### Step 1 — Clone the project
```bash
git clone https://github.com/YOUR_USERNAME/travel-planner-agent
cd travel_planner_agent
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Get your FREE API key
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click **Get API Key** → **Create API Key**
3. Copy the key

### Step 4 — Add your API key
Open the `.env` file and replace `your_api_key_here`:
```
GOOGLE_API_KEY=paste_your_key_here
```

### Step 5 — Run the app
```bash
adk web
```

Then open your browser at: **http://localhost:8000**

Select `coordinator_agent` and start chatting!

---

## Example Prompts to Try

- *"Plan a 7-day trip to Paris for 2 people with a mid-range budget"*
- *"I want to visit Bali for 10 days on a budget"*
- *"Plan a luxury 5-day trip to New York City"*
- *"What's the best time to visit Japan?"*

---

## What I Learned Building This

- How to build a **multi-agent AI system** using Google ADK
- How agents **delegate tasks** to specialist sub-agents
- How to use **Gemini 2.0 Flash** via Google AI Studio (free)
- How **agent coordination** works in real AI applications
- Debugging agent communication and prompt engineering

---

## Author

Built by [Your Name] as a portfolio project.  
Inspired by the Google Cloud ADK + A2A lab.

---

## License

MIT License — free to use and modify.
