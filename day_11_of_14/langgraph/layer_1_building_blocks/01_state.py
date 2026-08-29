# what is a state in langgraph?
# A state in LangGraph refers to a specific condition or configuration of the system at a given point in time.
# It represents the current values of all relevant variables and parameters that define the system's behavior.
# In the context of LangGraph, a state can be used to track the progress of computations, manage transitions
# between different stages of processing, and facilitate decision-making based on the current context.
# States are essential for modeling dynamic systems and enabling complex interactions within the LangGraph framework.


from typing import TypedDict, NotRequired
from langgraph.graph import StateGraph, START, END

class LoanState(TypedDict):
    applicant: str
    income: float
    emi: float
    ratio: NotRequired[float]

def compute_ratio(state):
    return {"ratio": round(state["emi"] / state["income"], 2)}

b = StateGraph(LoanState)
b.add_node("compute_ratio", compute_ratio)
b.add_edge(START, "compute_ratio")
b.add_edge("compute_ratio", END)
graph = b.compile()

print(graph.invoke({"applicant": "Carly", "income": 150000, "emi": 45000}))