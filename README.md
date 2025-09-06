# A Super Simple ReAct Agent

This project is to help get you setup with a basic ReAct agent as quickly and as simple as possible.

No fancy frameworks, no complex dependencies, just some simple python code using the Anthropic API directly.

You'll see that it's actually really simple to do.

Using frameworks (like LangChain) can add a lot of complexity, and hide what is actually going on behind the scenes.

If you are going to be building with Agents, it's important to know how they actually work. And by building your own
you can have a lot more control over how they behave as well.

A lot of times is probably best to start with a simple setup like this, with no framework included, and maybe just add
things like extra dependencies or frameworks later on, if you really see a need.

For more on building out your AI agents, check out the ["12 Factor Agents"](https://github.com/humanlayer/12-factor-agents) guide as well. That is a good read.

## What does the agent do?

It's a conversational agent, with tool calling abilities, which means you can do some pretty powerful things it.

For this example, I have set it up as a Pizza Delivery agent that gets your name, address and creates an order, using the
tools it has.

The point is to demonstrate how to build conversation agent you can interact with in natural language, that has the ability
to call tools, and process the results from those tools to see what to do do next.

In this example, the agents goal is to:
- get your name
- check if you exist in their registry via a tool call (this is to show an example of a tool call, and will always return `False`)
- if you don't exist, to ask for you address
- to ask what pizza you would like
- create an order with your name, address and pizza via a tool call

## Why did I build this?

There is something kind of complicated of visualising an Agent that can loop and do things on its own. I think imaging
things with recursion is general kind of hard to do.

I wanted to build my own ReAct agent, and searched for how to do that. There were definitiely some helpful guides on the
web, that allowed me to get started and figure it out.

I did notice though, that even those guides added features and methods which completely necessary for getting just a basic
ReAct agent working. Once I realised how simple one could be, I thought, why not create one and a write up about to show
how simple it can be. And to help other people getting started as well.

In a lot of ways, this is the startup code I wish I had when building out my fist ReAct agent.

I'm going to be working on a blog post/tutorial to go along with this also, that will add a lot of extra helpful detail as
well, as well as some links to external resource I found really helpful when trying to figure out ReAct agents.

Anyways, let's get strated!

## Getting Started

### Install `uv` and Create a Virtual Environment

First, get `uv` installed. It's a modern package manager for python, and blazingly fast. I tried it out for the first time
in this project, and was wowed with how fast it was

To install uv, run this in your terminal:

`curl -LsSf https://astral.sh/uv/install.sh | sh`

Then restart your terminal so the uv command is available.

You can check that it’s working with:

`uv --version`

Now create and initialise the virtual environment:

```bash
uv venv
source .venv/bin/activate
```

## Install Dependencies

Now install the dependencies:

```bash
uv sync
```

## Set Your Anthropic API Key

Now set your Anthropic API key as an environment variable in the .env file
(can get one from their website if you dont have one yet)

```bash
ANTHROPIC_API_KEY=
```

## Run the Agent
Now you can run the agent with:

```bash
python main.py
```

This will open up a chat interface in your terminal, where the agent will ask you questions in order to get your
pizza order and address.

The console output will show all the Tool calls and tool results the agent uses, to make it clear what is going on in
background as you chat with the agent.

To point is to show you how easy it is to setup a nicely working, conversation agent, that has tools at it disposal to
get things done as well.

