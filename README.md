# Agent - 联网搜索代理 (Web Search Agent)

一个简单但功能强大的联网搜索agent，可以执行互联网搜索并返回格式化的结果。

A simple yet powerful web search agent that can perform internet searches and return formatted results.

## Features / 功能特性

- 🔍 **Web Search**: Perform internet searches using DuckDuckGo (no API key required)
- 🎯 **Easy to Use**: Simple command-line interface and interactive mode
- 📊 **Formatted Results**: Clean, readable search results with titles, URLs, and snippets
- 🌐 **No API Keys**: Uses DuckDuckGo which doesn't require API keys
- 🐍 **Pure Python**: Written in Python 3 with minimal dependencies

## Installation / 安装

### Prerequisites / 前置要求

- Python 3.7 or higher

### Steps / 步骤

1. Clone the repository:
```bash
git clone https://github.com/yukiiii0730/Agent.git
cd Agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage / 使用方法

### Interactive Mode / 交互模式

Run the agent in interactive mode for continuous searches:

```bash
python search_agent.py
```

This will start an interactive session where you can enter search queries continuously until you type `quit` or `exit`.

### Direct Search / 直接搜索

Perform a single search directly from the command line:

```bash
# Basic search
python search_agent.py -q "Python programming"

# Limit the number of results
python search_agent.py -q "machine learning" -n 5
```

### Command-Line Options / 命令行选项

- `-q, --query`: Search query string
- `-n, --max-results`: Maximum number of results to return (default: 10)
- `-h, --help`: Show help message

## Examples / 示例

### Example 1: Interactive Mode
```bash
$ python search_agent.py
================================================================================
Web Search Agent / 联网搜索代理
================================================================================
Type your search query and press Enter. Type 'quit' or 'exit' to stop.
--------------------------------------------------------------------------------

Search query: Python web frameworks

Searching for: 'Python web frameworks'...

================================================================================
Found 10 results:
================================================================================

[1] Best Python Web Frameworks
    URL: https://example.com/python-frameworks
    Python has many powerful web frameworks including Django, Flask, FastAPI...

[2] Django vs Flask
    URL: https://example.com/django-vs-flask
    Comparing the two most popular Python web frameworks...

...
```

### Example 2: Direct Search
```bash
$ python search_agent.py -q "artificial intelligence" -n 3

Searching for: 'artificial intelligence'...

================================================================================
Found 3 results:
================================================================================

[1] Artificial Intelligence - Wikipedia
    URL: https://en.wikipedia.org/wiki/Artificial_intelligence
    Artificial intelligence is the simulation of human intelligence...

[2] What is AI?
    URL: https://example.com/what-is-ai
    A comprehensive guide to understanding artificial intelligence...

[3] AI Applications
    URL: https://example.com/ai-applications
    Real-world applications of artificial intelligence in various industries...
```

## Architecture / 架构

The agent consists of a single main module:

- **SearchAgent**: The core agent class that handles web searches
  - `search()`: Performs web search using DuckDuckGo
  - `format_results()`: Formats search results for display
  - `interactive_search()`: Runs interactive search mode

## Dependencies / 依赖项

- `duckduckgo-search`: For performing web searches without API keys (automatically includes all necessary dependencies)

## License / 许可证

This project is open source and available under the MIT License.

## Contributing / 贡献

Contributions are welcome! Feel free to submit issues or pull requests.

## Author / 作者

yukiiii0730