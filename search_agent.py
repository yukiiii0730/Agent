#!/usr/bin/env python3
"""
Web Search Agent
一个联网搜索agent - A web search agent that can perform internet searches
"""

import sys
from typing import List, Dict, Optional
from duckduckgo_search import DDGS


class SearchAgent:
    """A web search agent that can perform internet searches."""
    
    def __init__(self, max_results: int = 10):
        """
        Initialize the search agent.
        
        Args:
            max_results: Maximum number of search results to return (default: 10)
        """
        self.max_results = max_results
        self.ddgs = DDGS()
    
    def search(self, query: str, max_results: Optional[int] = None) -> List[Dict[str, str]]:
        """
        Perform a web search for the given query.
        
        Args:
            query: The search query string
            max_results: Maximum number of results to return (overrides default if provided)
            
        Returns:
            List of search results, each containing title, link, and snippet
        """
        if not query or not query.strip():
            return []
        
        results_limit = max_results if max_results is not None else self.max_results
        
        try:
            # Perform the search using DuckDuckGo
            results = []
            search_results = self.ddgs.text(query, max_results=results_limit)
            
            for idx, result in enumerate(search_results, 1):
                results.append({
                    'rank': idx,
                    'title': result.get('title', 'N/A'),
                    'link': result.get('href', 'N/A'),
                    'snippet': result.get('body', 'N/A')
                })
            
            return results
        except Exception as e:
            print(f"Error performing search: {e}", file=sys.stderr)
            return []
    
    def format_results(self, results: List[Dict[str, str]]) -> str:
        """
        Format search results for display.
        
        Args:
            results: List of search results
            
        Returns:
            Formatted string representation of results
        """
        if not results:
            return "No results found."
        
        formatted = []
        formatted.append(f"\n{'='*80}")
        formatted.append(f"Found {len(results)} results:")
        formatted.append(f"{'='*80}\n")
        
        for result in results:
            formatted.append(f"[{result['rank']}] {result['title']}")
            formatted.append(f"    URL: {result['link']}")
            formatted.append(f"    {result['snippet']}")
            formatted.append("")
        
        return "\n".join(formatted)
    
    def interactive_search(self):
        """
        Run the agent in interactive mode, allowing continuous searches.
        """
        print("="*80)
        print("Web Search Agent / 联网搜索代理")
        print("="*80)
        print("Type your search query and press Enter. Type 'quit' or 'exit' to stop.")
        print("-"*80)
        
        while True:
            try:
                query = input("\nSearch query: ").strip()
                
                if not query:
                    continue
                    
                if query.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                
                print(f"\nSearching for: '{query}'...")
                results = self.search(query)
                print(self.format_results(results))
                
            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}", file=sys.stderr)


def main():
    """Main entry point for the search agent."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Web Search Agent - 联网搜索代理',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python search_agent.py
  
  # Direct search
  python search_agent.py -q "Python programming"
  
  # Limit results
  python search_agent.py -q "machine learning" -n 5
        """
    )
    
    parser.add_argument(
        '-q', '--query',
        type=str,
        help='Search query (if not provided, runs in interactive mode)'
    )
    
    parser.add_argument(
        '-n', '--max-results',
        type=int,
        default=10,
        help='Maximum number of results to return (default: 10)'
    )
    
    args = parser.parse_args()
    
    # Create the agent
    agent = SearchAgent(max_results=args.max_results)
    
    # Run in interactive or direct mode
    if args.query:
        # Direct search mode
        print(f"Searching for: '{args.query}'...")
        results = agent.search(args.query)
        print(agent.format_results(results))
    else:
        # Interactive mode
        agent.interactive_search()


if __name__ == '__main__':
    main()
