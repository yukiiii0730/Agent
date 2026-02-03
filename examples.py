#!/usr/bin/env python3
"""
Example usage of the Search Agent

This file demonstrates various ways to use the Search Agent programmatically.
"""

from search_agent import SearchAgent


def example_basic_search():
    """Example: Perform a basic search."""
    print("="*80)
    print("Example 1: Basic Search")
    print("="*80)
    
    agent = SearchAgent(max_results=5)
    results = agent.search("Python web frameworks")
    
    print(agent.format_results(results))


def example_multiple_searches():
    """Example: Perform multiple searches."""
    print("\n" + "="*80)
    print("Example 2: Multiple Searches")
    print("="*80)
    
    agent = SearchAgent(max_results=3)
    
    queries = [
        "artificial intelligence",
        "machine learning",
        "deep learning"
    ]
    
    for query in queries:
        print(f"\n--- Results for: '{query}' ---")
        results = agent.search(query)
        
        if results:
            print(f"Found {len(results)} results:")
            for result in results[:2]:  # Show top 2
                print(f"  • {result['title']}")
                print(f"    {result['link']}")
        else:
            print("  No results found")


def example_custom_formatting():
    """Example: Custom result formatting."""
    print("\n" + "="*80)
    print("Example 3: Custom Formatting")
    print("="*80)
    
    agent = SearchAgent(max_results=5)
    results = agent.search("Python programming tutorials")
    
    if results:
        print(f"\nCustom formatted results:")
        print(f"{'#'*80}")
        
        for result in results:
            print(f"\n{result['rank']}. {result['title']}")
            print(f"   Link: {result['link']}")
            print(f"   Description: {result['snippet'][:100]}...")
            print(f"   {'-'*78}")


def example_programmatic_use():
    """Example: Using the agent programmatically."""
    print("\n" + "="*80)
    print("Example 4: Programmatic Use")
    print("="*80)
    
    agent = SearchAgent()
    
    # Simulate a workflow that needs search results
    query = "Python best practices"
    print(f"\nSearching for: {query}")
    
    results = agent.search(query, max_results=3)
    
    # Process results programmatically
    if results:
        urls = [r['link'] for r in results]
        titles = [r['title'] for r in results]
        
        print(f"\nExtracted {len(urls)} URLs:")
        for i, (title, url) in enumerate(zip(titles, urls), 1):
            print(f"  {i}. {title}")
            print(f"     -> {url}")
    else:
        print("No results to process")


def main():
    """Run all examples."""
    print("\n" + "#"*80)
    print("# Search Agent Examples - 搜索代理示例")
    print("#"*80 + "\n")
    
    try:
        example_basic_search()
        example_multiple_searches()
        example_custom_formatting()
        example_programmatic_use()
        
        print("\n" + "="*80)
        print("All examples completed!")
        print("="*80)
        
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("\nNote: These examples require an internet connection.")


if __name__ == '__main__':
    main()
