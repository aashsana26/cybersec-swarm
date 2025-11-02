from swarm_graph import build_swarm_graph

# Test Run file
def run_test():
    # Build the LangGraph app
    app = build_swarm_graph()

    # Initial test state (must be a dict)
    state = {"target": "demo.testserver.local", "logs": []}
    print("=== Starting Cybersecurity AI Swarm Test ===\n")

    # Invoke the workflow
    result = app.invoke(state)

    print("\n=== Final Result ===")
    for line in result["logs"]:
        print(line)

    print("\nTotal log lines:", len(result["logs"]))
    print("Target:", result["target"])

if __name__ == "__main__":
    run_test()
