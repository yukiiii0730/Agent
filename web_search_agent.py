#!/usr/bin/env python3
"""
Web Search Agent (联网检索Agent)
A simple agent that can search the web and retrieve information.
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
import time
import urllib.parse


class WebSearchAgent:
    """
    Web Search Agent that can perform web searches and retrieve information.
    """
    
    def __init__(self, user_agent: str = None):
        """
        Initialize the Web Search Agent.
        
        Args:
            user_agent: Custom user agent string (optional)
        """
        self.user_agent = user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        })
    
    def search(self, query: str, num_results: int = 5) -> List[Dict[str, str]]:
        """
        Search the web for the given query.
        
        Args:
            query: Search query string
            num_results: Number of results to return (default: 5)
            
        Returns:
            List of dictionaries containing search results with 'title', 'url', and 'snippet'
        """
        print(f"🔍 Searching for: {query}")
        
        # Use DuckDuckGo HTML search (doesn't require API key)
        search_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
        
        try:
            response = self.session.get(search_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            results = []
            
            # Parse DuckDuckGo results
            result_divs = soup.find_all('div', class_='result')
            
            for div in result_divs[:num_results]:
                try:
                    # Extract title and URL
                    title_elem = div.find('a', class_='result__a')
                    if not title_elem:
                        continue
                    
                    title = title_elem.get_text(strip=True)
                    url = title_elem.get('href', '')
                    
                    # Extract snippet
                    snippet_elem = div.find('a', class_='result__snippet')
                    snippet = snippet_elem.get_text(strip=True) if snippet_elem else ""
                    
                    if title and url:
                        results.append({
                            'title': title,
                            'url': url,
                            'snippet': snippet
                        })
                except Exception as e:
                    print(f"⚠️  Error parsing result: {e}")
                    continue
            
            print(f"✅ Found {len(results)} results")
            return results
            
        except Exception as e:
            print(f"❌ Search error: {e}")
            return []
    
    def fetch_content(self, url: str, max_length: int = 5000) -> str:
        """
        Fetch and extract text content from a URL.
        
        Args:
            url: URL to fetch
            max_length: Maximum length of content to return (default: 5000)
            
        Returns:
            Extracted text content
        """
        print(f"📄 Fetching content from: {url}")
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'lxml')
            
            # Remove script and style elements
            for script in soup(["script", "style", "header", "footer", "nav"]):
                script.decompose()
            
            # Get text content
            text = soup.get_text(separator=' ', strip=True)
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            # Limit length
            if len(text) > max_length:
                text = text[:max_length] + "..."
            
            print(f"✅ Fetched {len(text)} characters")
            return text
            
        except Exception as e:
            print(f"❌ Fetch error: {e}")
            return ""
    
    def search_and_summarize(self, query: str, num_results: int = 3) -> Dict[str, Any]:
        """
        Search for a query and fetch content from top results.
        
        Args:
            query: Search query string
            num_results: Number of results to process (default: 3)
            
        Returns:
            Dictionary containing search results and their content
        """
        results = self.search(query, num_results)
        
        summary = {
            'query': query,
            'results': []
        }
        
        for result in results:
            content = self.fetch_content(result['url'], max_length=2000)
            summary['results'].append({
                'title': result['title'],
                'url': result['url'],
                'snippet': result['snippet'],
                'content': content
            })
            time.sleep(1)  # Be polite to servers
        
        return summary


def main():
    """
    Example usage of the Web Search Agent.
    """
    # Create agent instance
    agent = WebSearchAgent()
    
    # Example 1: Simple search
    print("\n" + "="*80)
    print("Example 1: Simple Web Search")
    print("="*80)
    query = "Python programming tutorials"
    results = agent.search(query, num_results=3)
    
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   Snippet: {result['snippet'][:100]}...")
    
    # Example 2: Search and fetch content
    print("\n" + "="*80)
    print("Example 2: Search and Fetch Content")
    print("="*80)
    query = "machine learning basics"
    summary = agent.search_and_summarize(query, num_results=2)
    
    print(f"\nQuery: {summary['query']}")
    for i, result in enumerate(summary['results'], 1):
        print(f"\n{i}. {result['title']}")
        print(f"   URL: {result['url']}")
        print(f"   Content preview: {result['content'][:200]}...")


if __name__ == "__main__":
    main()
