from pydantic_ai import Agent, RunContext

age_agent = Agent(
    'ollama:llama3.1:8b', 
    retries=3,
    system_prompt="You will be asked for the age of a person, use the 'get_user_age' function to get the just the age of the user using the name of the person as parameter",
    )

@age_agent.tool
async def get_user_age(ctx: RunContext[str]) -> int:
    return 30

result = age_agent.run_sync('How old is the user: Hami?')
print(result.data)
#> city='London' country='United Kingdom'
print(result.cost())
#> Cost(request_tokens=57, response_tokens=8, total_tokens=65, details=None