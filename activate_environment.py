from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI

# Configure the model to use Ollama
model = OpenAIChatCompletionsModel(
    model="llama3.2",
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1")
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
