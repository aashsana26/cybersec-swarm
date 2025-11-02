from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from agents import observer, predictor, attacker, defender, archivist

class SwarmState(TypedDict):
    target: str
    logs: list[str]

def build_swarm_graph():

    graph = StateGraph(SwarmState)
    graph.add_node("observer", observer.observer_agent)
    graph.add_node("predictor", predictor.predictor_agent)
    graph.add_node("attacker", attacker.attacker_agent)
    graph.add_node("defender", defender.defender_agent)
    graph.add_node("archivist", archivist.archivist_agent)

    graph.add_edge("observer", "predictor")
    graph.add_edge("predictor", "attacker")
    graph.add_edge("attacker", "defender")
    graph.add_edge("defender", "archivist")
    graph.add_edge("archivist", END)
    graph.set_entry_point("observer")

    return graph.compile()
