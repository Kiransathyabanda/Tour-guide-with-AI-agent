from crewai import Agent, Task, Process, Crew
import os

os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'  
os.environ["OPENAI_API_KEY"] = 'your-api-key'

project = "Tour guide"
place = "nagpur to manali"
is_verbose = True

places_agent = Agent(
    role="Places identifier",
    goal=f"accurately retrieve the tourist places from {place} and its history that people can visit and have a good time which are famous",
    backstory=f"You are an AI assistant whose only job is to retrieve the tourist places from {place} and that places should be famous and people should be able to visit that places and its history",
    verbose=True,
    allow_delegation=False
)

planner_agent = Agent(
    role="planner",
    goal=f"accurately make a proper plan with the time, place, distance, if available public transport route and the transportation with the good time to visit and a proper planning",
    backstory="You are an AI assistant whose only job is to make a proper plan to visit those places and schedule accordingly",
    verbose=True,
    allow_delegation=False
)

place_identifier = Task(
    description=f"find the famous tourist places to visit in {place}.",
    agent=places_agent,
    expected_output=f"a proper retriever of the places and information based on the {place}.",
)

planner = Task(
    description=f"preparing a proper plan for visiting.",
    agent=planner_agent,
    expected_output="preparing a proper plan with proper timings and places with the distance based on the information provided by the 'places_agent' agent.",
)

crew = Crew(
    agents=[places_agent, planner_agent],
    tasks=[place_identifier, planner],
    verbose=2,
    process=Process.sequential
)

output = crew.kickoff()
print(output)
