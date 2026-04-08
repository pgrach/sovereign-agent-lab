"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
2026-04-08 11:22:38 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
2026-04-08 11:39:40 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  calling to confirm a booking

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


How many guests are you confirming for tonight's event?
Your input ->  hundred sixty guests
And how many of those guests will need vegan meals?
Your input ->  about fifty
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  five hundred
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "The deposit amount exceeded the organiser's authorised limit of £300."   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
2026-04-08 11:46:20 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit):
Your input ->  calling to confirm a booking

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

How many guests are you confirming for tonight's event?
Your input ->  160 guests

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers




Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
After I asked about parking for the speakers, the agent responded with: "I'm sorry, I'm not trained to help with that. I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly. Would you like to continue with confirm booking?" This indicates that the agent was able to detect that the request was outside of its scope and politely declined to help.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
In contrast to LangGraph's approach in Exercise 2, where the out-of-scope request was handled by a separate Python function that returned a specific error message, Rasa CALM handles out-of-scope requests using its built-in out-of-scope detection mechanism. 
This allows CALM to gracefully handle unexpected user inputs without requiring custom code for each scenario. 
Additionally, CALM's ability to maintain context throughout the conversation enables it to provide more relevant responses compared to LangGraph's more rigid structure.
This at the end is a good thing, as it allows the agent to be more flexible and adaptable to different situations, leading to less user frustration.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["actions/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
I tested the cutoff guard by temporarily modifying the `validate_booking_confirmation` function in `actions/actions.py` to always return `True` for the time check, regardless of the actual time. 
This allowed me to simulate a scenario where the cutoff guard was triggered, even though the current time did not meet the 16:45 threshold. 
I then ran `uv run rasa shell` and interacted with the bot, providing the required information for the booking confirmation. 
The bot correctly identified that the cutoff guard was triggered and returned the polite response, indicating that it could not proceed with the booking due to the time constraint.
But it also did not drop the ball - suggesting to escalate and call back later. Can I call you back within 15 minutes?
This is a good example of a well-designed agent that can handle unexpected situations gracefully.
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
In CALM, the LLM handles slot extraction (from_llm mappings) that previously required
Python regex in ValidateBookingConfirmationForm. "About 160 people", "one-sixty", and
"we're expecting 160" all become 160.0 automatically -- no parsing code needed.

Python STILL handles the business rules (deposit limit, capacity cap, vegan ratio,
cutoff guard) via ActionValidateBooking. This is deliberate: financial and legal
constraints must be deterministic. An LLM might reason "350 is close enough to 300"
but Python enforces the hard boundary without negotiation.

The old approach was more trustworthy for slot extraction -- regex is predictable.
But it was brittle: "about 160" needed a specific pattern. CALM trades that
predictability for natural language flexibility, which is the right trade-off
for conversational input where users never speak in a standard format.
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
CALM's setup cost (config.yml, domain.yml, flows.yml, endpoints.yml, rasa train,
two terminals, licence) buys you deterministic flow control. The CALM agent CANNOT
improvise a response it wasn't designed for -- it deflects cleanly ("I'm not trained
to help with that"). It CANNOT call a tool not defined in flows.yml.

For the booking confirmation use case, this is a feature, not a limitation. When a
pub manager calls to confirm £5,000+ worth of catering, you want a predictable agent
that follows the script, not one that might hallucinate a confirmation or invent
a discount. LangGraph's flexibility is powerful for open-ended research, but
dangerous for transactional workflows where every word has financial consequences.

The extra setup cost buys auditability: every possible path is visible in flows.yml.
"""
