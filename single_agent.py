from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

# Add the api_key parameter (can be any string, Ollama doesn't use it)
model = OpenAIChatCompletionsModel(
    model="gemma3:12b",
    openai_client=AsyncOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"  # Required by OpenAI client but not used by Ollama
    )
)

# Create a simple agent
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=model
)

# Run the agent with a query
result = Runner.run_sync(agent, "Create a meal plan for a week.")
print(result.final_output)
