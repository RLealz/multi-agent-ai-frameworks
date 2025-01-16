# Phidata: Building Multi-Agent AI Systems

Phidata is a Python-based framework for converting Large Language Models (LLMs) into powerful AI agents. It supports multi-agent collaboration, built-in UIs, and seamless integration with cloud services like AWS. With Phidata, you can build agents that automate workflows, analyze data, and solve complex problems.

## Key Features
- **Built-in agent UI**: Run and manage agents locally or in the cloud.
- **Multi-agent collaboration**: Agents can transfer tasks and work together.
- **Model independence**: Use LLMs from OpenAI, Anthropic, Mistral, and more.
- **Deployment**: Deploy agents to AWS or GitHub with ease.

## Example: Financial AI Agent
This example demonstrates how to build a financial AI agent using Phidata and OpenAI. The agent fetches stock data and summarizes analyst recommendations.

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/multi-agent-ai-frameworks.git
   cd multi-agent-ai-frameworks/phidata
2. **Set up a virtual environment:**:
   ```bash
   python -m venv venv
   cd venv
   source bin/activate  # On Windows: venv\Scripts\activate
3. **Install the dependencies:**:
   ```bash
   pip install -r requirements.txt
4. **Run the example:**:
   ```bash
   python example.py

### Code Explanation
The example.py script creates a financial AI agent that uses Yahoo Finance data to summarize analyst recommendations for a given stock (e.g., TSLA).

### Learn More
- [Phidata Documentation](https://phidata-docs.netlify.app/)
- [Phidata GitHub](https://github.com/Phidata-Open-Source/phidata)