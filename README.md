Ai travel planner portfolio · MD
# ✈ AI Travel Planner — Multi-Agent System
### By Kithuni Perera
 
---
 
## The Problem Worth Solving
 
Travel planning is genuinely hard. A typical trip requires a traveler to juggle three completely separate mental tasks at once: figuring out *what* to do each day, deciding *where* to sleep, and calculating *how much* it will all cost — all while keeping those three things consistent with each other. Most travelers switch between five or six different tabs, apps, and spreadsheets to pull this together. The result is either an overwhelming pile of bookmarks that never becomes a real plan, or a plan that turns out to be wildly over budget only after hours of work.
 
There is no single tool that coordinates these three tasks intelligently. Search engines return generic listicles. Booking apps focus on transactions, not planning. Chatbots answer one question at a time. **Nobody had built a system that treats travel planning as the multi-dimensional, interconnected problem it actually is** — until this project.
 
---
 
## Why I Chose to Build This
 
I wanted to go beyond a simple chatbot and explore what it really means to build a production-style AI system. The AI Travel Planner gave me a concrete, relatable problem domain where the complexity is real but understandable, and where the value of a good solution is immediately obvious to anyone who has planned a trip.
 
More specifically, I wanted to answer a question that genuinely interested me: *What happens when you stop giving one AI everything to do and instead give specialized agents specific responsibilities?* Can they coordinate? Can they produce better, more reliable outputs than a single general-purpose model? This project was my way of finding out by building — not just reading about it.
 
---
 
## Problem Analysis
 
Before writing a single line of code, I mapped out why existing approaches fall short:
 
**Single-model chatbots** forget context across a long planning session. Ask about hotels, then ask about budget, and the budget often doesn't reflect the hotels you just discussed.
 
**Generic travel sites** are transactional. They optimize for booking, not for thinking.
 
**Static itinerary generators** produce the same template regardless of budget, duration, or travel style.
 
**The core insight** was that travel planning has three distinct *knowledge domains* — activities, accommodation, and finance — and conflating them into one undifferentiated prompt produces mediocre outputs across all three. Separating them into specialized agents, coordinated by a central brain, would let each agent go deeper in its domain while the coordinator kept everything aligned.
 
This is exactly how real travel agencies work: a destination specialist, an accommodations specialist, and a financial advisor each contribute their expertise and a coordinator assembles the final package.
 
---
 
## Architecture & Design Decisions
 
```
User Input
    │
    ▼
Coordinator Agent      ← Main brain: interprets intent, delegates, assembles output
    │
    ├──► Itinerary Agent   → Day-by-day activities, timing, local food tips
    ├──► Hotel Agent       → 3-tier accommodation options (budget / mid / luxury)
    └──► Budget Agent      → Itemised cost breakdown + money-saving strategies
    │
    ▼
Complete, Coherent Travel Plan
```
 
The **Coordinator Agent** is the critical design element. It does not just pass the user's message directly to sub-agents. It parses intent, extracts parameters (destination, duration, budget tier), and issues structured delegation requests. When sub-agents return their outputs, the coordinator synthesises them into a single, readable plan — resolving any inconsistencies before the user ever sees a response.
 
Each **specialist agent** receives only the information it needs. The Hotel Agent knows the budget tier. The Budget Agent knows what hotels were recommended. This prevents the classic problem of agents producing outputs that contradict each other.
 
---
 
## Technology Stack & Why
 
| Technology | Role | Why This Choice |
|---|---|---|
| **Python 3.12** | Core language | Dominant language for AI/ML; rich ecosystem; readable code |
| **Google ADK** | Agent orchestration framework | Native support for multi-agent hierarchies; clean agent-to-agent communication APIs; production-grade tooling |
| **Gemini 2.0 Flash** | Underlying LLM | Fast inference; strong instruction-following; well-suited for structured, domain-specific outputs |
| **VS Code** | Development environment | Industry standard; excellent Python and Git integration |
 
**Why Google ADK specifically?** Most tutorials show you how to call an LLM API. ADK forced me to think about *agent architecture* — how agents are defined, how they discover and call each other, how to manage state across a multi-turn conversation involving multiple models. That architectural discipline is the real skill this project built.

## Key Learnings
 
**1. Prompt engineering is architecture.** How you structure a sub-agent's system prompt determines the quality and consistency of its output far more than the model you choose. I rewrote each agent's prompt three to four times before the outputs were reliably structured.
 
**2. Coordinator design is the hardest part.** Getting the coordinator to correctly parse ambiguous user input ("I want to visit Bali for 10 days on a budget" — what currency? which airports? budget for one or two people?) and issue unambiguous delegation requests required significant iteration.
 
**3. Agent communication debugging is a new skill.** When the final output was wrong, it was rarely obvious whether the fault was in the coordinator's delegation, a sub-agent's output, or the coordinator's synthesis step. I developed a practice of logging intermediate agent outputs during development — a habit that transfers directly to any distributed system work.
 
**4. Multi-agent systems are not always better.** Early in the project I experimented with having the coordinator handle everything in one pass. For simple queries it was actually faster and equally good. The specialist architecture pays off most on complex, long-duration queries where depth in each domain matters. Knowing *when* to use multi-agent design is as important as knowing *how*.
 
**5. Framework choice shapes your thinking.** Using Google ADK rather than rolling a custom solution forced me to think about agents as first-class objects with defined interfaces — not just prompts wrapped in Python functions. That mental model is more transferable.
 
---
 
## Why This Project Stands Out
 
Most AI portfolio projects are one of two things: a wrapper around a single API call, or a clone of a tutorial. This project is neither.
 
**It demonstrates systems thinking.** The value is not in the code of any single file — it is in the design of how four agents communicate, delegate, and synthesise. That is an architectural skill, not just a coding skill.
 
**It solves a real, complex problem.** Travel planning genuinely benefits from multi-domain coordination. The problem structure naturally justifies the solution structure. This is not a system looking for a problem.
 
**It reflects production patterns.** The modular, single-responsibility agent structure mirrors how real AI systems at scale are being built today. Hiring managers and engineering teams looking at this project see code that reflects how AI engineering actually works in production.
 
**It shows independent judgment.** The technology choices — ADK, Gemini 2.0 Flash, the specific coordinator/specialist split — were made deliberately based on analysis of the problem, not just copied from a tutorial. The project documentation explains the *why* behind every major decision.
 
**It is extensible.** The architecture could support a visa-requirements agent, a flight-search agent, or a real-time weather agent with no changes to existing code. That extensibility is proof the design is sound.
 
---
 
*Built by Kithuni Perera . Inspired by the Google Cloud ADK + A2A lab.*
