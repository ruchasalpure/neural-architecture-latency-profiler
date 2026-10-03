from crewai import Agent

neural_architecture_latency_profiler = Agent(
    role="Neural Architecture Latency Profiler",
    goal="Deliver high-precision autonomous Neural Architecture Latency Profiler operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
