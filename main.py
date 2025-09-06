from app.context_window import ContextWindow
from app.claude_client import ClaudeClient
from app.pizza_agent import PizzaAgent, system_prompt


def main():
    print("🍕 Welcome to Mamma's Pizza Delivery Chat!")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("-" * 50)
    
    # Initialize the agent
    context = ContextWindow(conversation_history=[])
    claude_client = ClaudeClient(system_prompt=system_prompt)
    agent = PizzaAgent(context=context, claude_client=claude_client)
    
    try:
        while True:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\n🍕 Thanks for choosing Mamma's Pizza! Goodbye!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            try:
                # Get agent response
                response = agent.send_message(user_input)
                print(f"\n🤖 Pizza Bot: {response}")
                
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                print("Please try again.")
                
    except KeyboardInterrupt:
        print("\n\n🍕 Thanks for choosing Mamma's Pizza! Goodbye!")


if __name__ == "__main__":
    main()
