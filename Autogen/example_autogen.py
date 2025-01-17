
# Import necessary libraries
from autogen import AssistantAgent, UserProxyAgent, Task

# Define agents and their roles
assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful assistant.",
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    system_message="You are a user interacting with an assistant.",
)

# Define a task for the agents
task = Task(
    description="Search for information about AI trends in 2023 and analyze them.",
)

# Assign the task to the user proxy agent
user_proxy.add_task(task)

# Run the multi-agent system
user_proxy.run()

# Print the result
print("Result:", user_proxy.last_task.result)