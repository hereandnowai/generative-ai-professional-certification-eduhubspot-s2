# what is a state in langgraph?
# A state in LangGraph refers to a specific condition or configuration of the system at a given point in time.
# It represents the current values of all relevant variables and parameters that define the system's behavior.
# In the context of LangGraph, a state can be used to track the progress of computations, manage transitions
# between different stages of processing, and facilitate decision-making based on the current context.
# States are essential for modeling dynamic systems and enabling complex interactions within the LangGraph framework.


from typing import TypedDict, NotRequired
from langgraph.graph import StateGraph, START, END

