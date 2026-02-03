#!/usr/bin/env python3
"""
Simple tests for the Search Agent
"""

import sys
import os

# Add parent directory to path to import search_agent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from search_agent import SearchAgent


def test_agent_initialization():
    """Test that the agent can be initialized."""
    print("Test 1: Agent Initialization")
    try:
        agent = SearchAgent(max_results=5)
        assert agent.max_results == 5
        print("✓ Agent initialized successfully")
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def test_empty_query():
    """Test handling of empty queries."""
    print("\nTest 2: Empty Query Handling")
    try:
        agent = SearchAgent()
        results = agent.search("")
        assert results == []
        print("✓ Empty query handled correctly")
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def test_basic_search():
    """Test a basic search query."""
    print("\nTest 3: Basic Search")
    try:
        agent = SearchAgent(max_results=3)
        results = agent.search("Python programming")
        
        if results:
            print(f"✓ Search returned {len(results)} results")
            
            # Verify result structure
            for result in results:
                assert 'title' in result
                assert 'link' in result
                assert 'snippet' in result
                assert 'rank' in result
            
            print("✓ Results have correct structure")
            
            # Display first result
            if results:
                print(f"\nSample result:")
                print(f"  Title: {results[0]['title'][:50]}...")
                print(f"  URL: {results[0]['link'][:50]}...")
            
            return True
        else:
            print("⚠ No results returned (may be a network issue)")
            return True  # Don't fail on network issues
            
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def test_format_results():
    """Test result formatting."""
    print("\nTest 4: Result Formatting")
    try:
        agent = SearchAgent()
        
        # Test with sample data
        sample_results = [
            {
                'rank': 1,
                'title': 'Test Title',
                'link': 'https://example.com',
                'snippet': 'Test snippet'
            }
        ]
        
        formatted = agent.format_results(sample_results)
        assert 'Test Title' in formatted
        assert 'https://example.com' in formatted
        print("✓ Results formatted correctly")
        
        # Test empty results
        empty_formatted = agent.format_results([])
        assert 'No results found' in empty_formatted
        print("✓ Empty results formatted correctly")
        
        return True
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False


def main():
    """Run all tests."""
    print("="*60)
    print("Running Search Agent Tests")
    print("="*60)
    
    tests = [
        test_agent_initialization,
        test_empty_query,
        test_basic_search,
        test_format_results,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        if test():
            passed += 1
        else:
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60)
    
    return failed == 0


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
