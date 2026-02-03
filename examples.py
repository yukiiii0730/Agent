#!/usr/bin/env python3
"""
Simple examples of using the Web Search Agent.
"""

from web_search_agent import WebSearchAgent


def example_1_basic_search():
    """
    Example 1: Perform a basic web search.
    """
    print("\n" + "="*80)
    print("Example 1: Basic Web Search")
    print("="*80 + "\n")
    
    # Create an agent instance
    agent = WebSearchAgent()
    
    # Search for something
    query = "artificial intelligence news"
    results = agent.search(query, num_results=5)
    
    # Display the results
    print(f"Search results for: '{query}'\n")
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   {result['snippet']}\n")


def example_2_fetch_content():
    """
    Example 2: Fetch and read content from a specific URL.
    """
    print("\n" + "="*80)
    print("Example 2: Fetch Content from URL")
    print("="*80 + "\n")
    
    # Create an agent instance
    agent = WebSearchAgent()
    
    # Fetch content from a URL
    url = "https://www.python.org"
    content = agent.fetch_content(url, max_length=500)
    
    print(f"Content from {url}:\n")
    print(content)


def example_3_search_and_read():
    """
    Example 3: Search and automatically fetch content from top results.
    """
    print("\n" + "="*80)
    print("Example 3: Search and Fetch Content")
    print("="*80 + "\n")
    
    # Create an agent instance
    agent = WebSearchAgent()
    
    # Search and get detailed content
    query = "Python web scraping tutorial"
    summary = agent.search_and_summarize(query, num_results=2)
    
    print(f"Detailed results for: '{summary['query']}'\n")
    for i, result in enumerate(summary['results'], 1):
        print(f"\n{'='*80}")
        print(f"Result {i}: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"{'='*80}")
        print(f"\nSnippet: {result['snippet']}")
        print(f"\nContent preview:\n{result['content'][:300]}...\n")


def main():
    """
    Run all examples.
    Note: These examples require internet access.
    Use test_agent.py for offline testing.
    """
    print("\n" + "="*80)
    print("Web Search Agent Examples")
    print("="*80)
    
    try:
        # Run example 1
        example_1_basic_search()
        
        # Run example 2
        example_2_fetch_content()
        
        # Run example 3
        example_3_search_and_read()
        
    except Exception as e:
        print(f"\n⚠️  Error: {e}")
        print("\nNote: These examples require internet access.")
        print("If you're testing offline, please run: python test_agent.py")


if __name__ == "__main__":
    main()
