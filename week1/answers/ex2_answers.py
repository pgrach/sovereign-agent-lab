"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "get_edinburgh_weather", "calculate_catering_cost", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach" # "The Haymarket Vaults" also recognised as meeting all constraints

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = """Four issues encountered:
1. The original parser looked for Anthropic-format 'tool_use' blocks in content,
   but LangChain/OpenAI stores tool calls in message.tool_calls attribute.
   Fix: replaced the parser to use getattr(m, 'tool_calls', []).
2. Llama-3.3-70B on Nebius, given a complex multi-step prompt, dumped all planned
   tool calls as a JSON text string instead of using native function calling.
   The model was 'planning' rather than 'executing'. Fix (credit: shakirali - on discord):
   added a system prompt to create_react_agent instructing the model to
   'work through tasks step by step, calling one tool at a time'.
   This nudged the model into proper ReAct behavior.
3. The JSON output shows \u00a3 which is the Unicode escape for £ (pound sterling).
   Not a bug — json.dumps() escapes non-ASCII characters by default.
4. Since the model confirmed the Albanach as the venue, I got a bit confused
   as to why task B was still picking the Haymarket Vaults for image gen (which was hardcoded). 
   In production, I would expect the model output to pass the venue_name to task B. 

""" # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://api.nebius.ai/v1/images/generations/69367657-4620-4084-947f-7f1594896687/image.png"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The Bow Bar does not meet the requirements for 160 vegan guests tonight. 
However, The Albanach is available and meets all the constraints. The current 
weather in Edinburgh is clear, making it suitable for an outdoor area at the venue. 
The estimated total catering cost for the event is £3200. A promotional event flyer 
image has been generated for The Albanach, which can be accessed at the provided URL.
"""

SCENARIO_1_FALLBACK_VENUE = "The Albanach"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known venues meet the capacity and dietary requirements.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = True   # True or False

SCENARIO_3_RESPONSE = """
  I cannot perform this task as it requires additional functionality beyond 
  what is available in the given functions.
"""

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
Yes, this behaviour would be acceptable in a real booking assistant. 
It is important for the assistant to be able to handle requests that are 
outside of its scope and to inform the user about its limitations.
It is also important for the assistant to be able to handle requests that 
are outside of its scope and to inform the user about its limitations.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
        """

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
LangGraph's Mermaid output shows a single cyclic graph: __start__ -> agent <-> tools -> __end__.
The LLM decides at every step whether to call a tool or emit a final answer. All routing is implicit.

Rasa CALM's flows.yml (note: the answer template says rules.yml but the actual file is
exercise3_rasa/data/flows.yml) defines explicit, deterministic flows (e.g. confirm_booking)
with ordered steps: collect guest_count, collect vegan_count, collect deposit, then run
action_validate_booking. The LLM only decides WHICH flow to start; after that, Rasa executes
steps in a fixed sequence.

Trade-off: LangGraph is flexible but unpredictable (the agent can improvise, retry, or
hallucinate). Rasa CALM is rigid but auditable -- every path is readable and explicit.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
In Scenario 3 (out-of-scope train times), the agent tried to call get_last_train_time — a tool
that does not exist. Rather than refusing outright, it invented a plausible function name and
attempted the call. LangGraph caught the error and returned 'not a valid tool', at which point
the agent recovered gracefully. This shows Llama does not validate tool names against the
registry before calling — it relies on the framework's error handling as a safety net.

Additionally, without explicit fallback instructions in the prompt (my pivot experiment 
where i removed the prompt to check other venues if the first one fails), the agent 
simply reported failure instead of proactively checking other venues.

Image generation outputs are really ugly. I would not use it in production, it 
hallucinates objects, cannot draw words or numbers, and the quality is very low overall.


"""
