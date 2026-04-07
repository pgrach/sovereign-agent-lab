"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Despite the fact that the model correctly answered the question in all three conditions, 
there were some interesting differences in its responses. 
In the plain condition, the model correctly identified the Haymarket Vaults as the correct 
answer. However, in the XML and sandwich conditions, the model identified the Albanach 
as the correct answer. This is interesting because it is not the same answer as 
the one given in the plain condition. 
Maybe XML prompt formatting suggests that the model should seach for the safest option? 
180 Albanach vs 160 Haymarket Vaults when the question asks for "at least 160 guests" 
(which is the minimum) suggests that Albanach is a safer option. 
Or could it be Primacy bias that favors Albanach (top) for XML and sandwich conditions?
It is also interesting to note that the model gave the same answer 
in both the XML and sandwich conditions, even though the sandwich condition 
had the question repeated at the end. This suggests that the model may be more likely 
to give the same answer in both conditions, regardless of the formatting. So sandwich 
prompting for this dataset may be redundant.
Overall for this dataset the formatting does not seem to matter much.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
Adding near miss distractors did not change the results for this dataset. 
I think the Holyrood Arms was the most dangerous distractor because it satisfied 
capacity and vegan constraints, only failing on status.
But I also experimented with:
1. expanded dataset (added 20 more venues) with the same model. And I got 
the same output.
2. another model (even with 4x smaller than Part C). It still got 
everything right.

"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
It seems that the smaller model is more sensitive to the formatting of the prompt. 
The Haymarket Vaults was picked as correct answer in all three conditions for the smaller model.
XML and sandwich prompting have switched to The Haymarket Vaults as the correct answer from
Albanach for the larger model. The only reason for that I can think of is that smaller model
is less "smart" and suggests the most "obvious" answer with 160 capacity (the exactly required capacity). 
Albanach with 180 capacity is a safer bet in general, so it could be wiser 
to have extra capacity just in case.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
What I find interesting is that the bigger Llama-3.3-70B model spends 
less tokens than the smaller one Llama-3.1-8B. More efficient tokeniser?
Context formatting potentially matters when the dataset is larger 
or when there are more distractors (although it did not matter in my case). 
I tried a smaller model with larger dataset and it was still able 
to get the correct answer in all conditions. 
In this case the dataset was small and there were only a few distractors, 
so the formatting certainly did not matter to find the correct answer.
One carefull thought is that XML primes the model to scan top-down 
(query appears first → evaluate systematically → grab the first valid match
 = Albanach). While plain prompting encourages more free-form search.
Another suggestion is that XML's structured format triggers more 
analytical reasoning, leading the model to prefer the venue 
with extra headroom (180 vs exactly 160).

"""
