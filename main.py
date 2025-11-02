from swarm_graph import build_swarm_graph

# We're invoking the agents here
def run_swarm(target: str = "target.example.com"):
    app = build_swarm_graph()
    # The initial state is the target string; observer will use it
    initial_state = {"target": target, "logs": []}
    result = app.invoke(initial_state)
    return result

if __name__ == "__main__":
    print("Running swarm on sample target...")
    out = run_swarm("demo.example.com")
    import json
    print(json.dumps(out, indent=2))
