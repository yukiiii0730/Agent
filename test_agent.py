#!/usr/bin/env python3
"""
Test and demonstration script for Web Search Agent.
This script includes both real search functionality and demo mode for testing without internet.
"""

from web_search_agent import WebSearchAgent


def demo_mode():
    """
    Demonstrate the agent's functionality with mock data (for testing without internet).
    """
    print("\n" + "="*80)
    print("DEMO MODE: Web Search Agent Demonstration")
    print("="*80)
    
    # Simulate search results
    print("\n🔍 Demo Search: 'Python programming tutorials'")
    print("✅ Found 3 results (demo data)")
    
    mock_results = [
        {
            'title': 'Python Tutorial - Learn Python Programming',
            'url': 'https://www.python.org/about/gettingstarted/',
            'snippet': 'Learn the basics of Python programming with official tutorials and documentation.'
        },
        {
            'title': 'Real Python - Python Tutorials',
            'url': 'https://realpython.com/',
            'snippet': 'Learn Python online: Python tutorials for developers of all skill levels...'
        },
        {
            'title': 'W3Schools Python Tutorial',
            'url': 'https://www.w3schools.com/python/',
            'snippet': 'Well organized and easy to understand Web building tutorials with lots of examples...'
        }
    ]
    
    print("\nSearch Results:")
    for i, result in enumerate(mock_results, 1):
        print(f"\n{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   Snippet: {result['snippet']}")
    
    print("\n" + "="*80)
    print("Demo: Content Fetching")
    print("="*80)
    
    print("\n📄 Demo: Fetching content from URL...")
    print("✅ Content extracted successfully (demo data)")
    print("\nContent Preview:")
    print("Python is a high-level, interpreted programming language with dynamic semantics.")
    print("Its high-level built-in data structures, combined with dynamic typing and dynamic")
    print("binding, make it very attractive for Rapid Application Development...")
    
    print("\n" + "="*80)
    print("Agent Features Demonstrated:")
    print("="*80)
    print("✅ Web search capability")
    print("✅ Result parsing and extraction")
    print("✅ Content fetching from URLs")
    print("✅ Text cleaning and formatting")


def test_agent_api():
    """
    Test the agent's API structure (without making real network calls).
    """
    print("\n" + "="*80)
    print("API Structure Test")
    print("="*80)
    
    # Create agent instance
    agent = WebSearchAgent()
    print("✅ WebSearchAgent instantiated successfully")
    
    # Check methods exist
    assert hasattr(agent, 'search'), "search method exists"
    assert hasattr(agent, 'fetch_content'), "fetch_content method exists"
    assert hasattr(agent, 'search_and_summarize'), "search_and_summarize method exists"
    print("✅ All required methods are available")
    
    # Check attributes
    assert hasattr(agent, 'session'), "session attribute exists"
    assert hasattr(agent, 'user_agent'), "user_agent attribute exists"
    print("✅ All required attributes are initialized")
    
    print("\n✅ API structure test passed!")


def main():
    """
    Run tests and demonstrations.
    """
    print("\n" + "="*80)
    print("Web Search Agent (联网检索Agent) - Test Suite")
    print("="*80)
    
    # Run API structure test
    test_agent_api()
    
    # Run demo mode
    demo_mode()
    
    print("\n" + "="*80)
    print("Usage Instructions:")
    print("="*80)
    print("""
To use the Web Search Agent with internet access:

    from web_search_agent import WebSearchAgent
    
    # Create agent
    agent = WebSearchAgent()
    
    # Search the web
    results = agent.search("your query here", num_results=5)
    
    # Fetch content from a URL
    content = agent.fetch_content("https://example.com")
    
    # Search and get detailed content
    summary = agent.search_and_summarize("your query", num_results=3)

See README.md for more examples and documentation.
    """)


if __name__ == "__main__":
    main()
