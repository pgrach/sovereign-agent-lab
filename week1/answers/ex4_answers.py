"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "Agent looped calling search_venues repeatedly and hit the recursion limit without producing a final answer"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
I changed the status of "The Albanach" to "full" in `venue_server.py` and reran the client. 
The agent correctly used `search_venues` to find available venues and then `get_venue_details` 
to retrieve the address for the best match. No files other than `venue_server.py` needed updating, 
as the LangGraph client automatically discovered and used the available tools.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 283   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 219   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP allows the client to discover and use tools dynamically without 
needing to know their implementation details. This separation of concerns 
makes the system more modular and easier to maintain, as tools can be 
developed and updated independently of the client.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- MCP Venue Server exposes tools via a standard protocol so any client 
can discover and use them without code changes.

- LangGraph Research Agent handles open-ended venue search using a flexible 
ReAct loop where the LLM decides steps dynamically.

- Rasa CALM Confirmation Agent handles the structured booking call using 
deterministic flows for auditable financial decisions.

- Nebius-hosted LLMs (Llama 3.3 70B) provide the reasoning backbone running 
on sovereign infrastructure.

- Python business rules in ActionValidateBooking enforce hard constraints 
deterministically because LLMs cannot be trusted with financial boundaries.

"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph is right for research because it needs flexibility: 
it pivoted from The Bow Bar to The Albanach on its own and even invented 
a non-existent tool. Rasa CALM is right for the booking call because it follows 
a fixed script. Swapping them would be dangerous: a LangGraph agent might hallucinate 
a confirmation, while a Rasa agent cannot improvise when the first venue is full. 
Each framework's strength is the other's weakness.

"""
