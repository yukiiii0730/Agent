# Web Search Agent (联网检索Agent)

A simple yet powerful web search agent that can search the web and retrieve information from search results.

## Features

- 🔍 **Web Search**: Search the web using DuckDuckGo (no API key required)
- 📄 **Content Extraction**: Fetch and extract text content from web pages
- 🎯 **Smart Parsing**: Clean and parse HTML content intelligently
- 🚀 **Easy to Use**: Simple Python API with clear examples

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yukiiii0730/Agent.git
cd Agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Search

```python
from web_search_agent import WebSearchAgent

# Create agent instance
agent = WebSearchAgent()

# Perform a search
results = agent.search("Python programming tutorials", num_results=5)

# Display results
for result in results:
    print(f"Title: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"Snippet: {result['snippet']}\n")
```

### Search and Fetch Content

```python
from web_search_agent import WebSearchAgent

# Create agent instance
agent = WebSearchAgent()

# Search and fetch content from top results
summary = agent.search_and_summarize("machine learning basics", num_results=3)

# Access the results
for result in summary['results']:
    print(f"Title: {result['title']}")
    print(f"Content: {result['content'][:200]}...\n")
```

### Fetch Specific URL

```python
from web_search_agent import WebSearchAgent

# Create agent instance
agent = WebSearchAgent()

# Fetch content from a specific URL
content = agent.fetch_content("https://example.com")
print(content)
```

## Running Examples

Run the included example script:

```bash
python web_search_agent.py
```

This will demonstrate:
1. Simple web search with result display
2. Search with content fetching from top results

## API Reference

### `WebSearchAgent`

Main agent class for web searching and content retrieval.

#### Methods

- **`search(query: str, num_results: int = 5)`**
  - Search the web for the given query
  - Returns: List of dictionaries with 'title', 'url', and 'snippet'

- **`fetch_content(url: str, max_length: int = 5000)`**
  - Fetch and extract text content from a URL
  - Returns: Extracted text content as string

- **`search_and_summarize(query: str, num_results: int = 3)`**
  - Search and fetch content from top results
  - Returns: Dictionary with query and detailed results

## Requirements

- Python 3.7+
- requests>=2.31.0
- beautifulsoup4>=4.12.0
- lxml>=4.9.0

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.