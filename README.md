# Multi-Agent AI Frameworks

## Overview
This repository provides descriptions and implementation examples for popular multi-agent AI frameworks. Each framework is explored through a dedicated folder containing a `README.md`, an `example.py`, and a `requirements.txt` file. The goal is to offer a comprehensive resource for understanding and implementing multi-agent systems.

## Table of Contents
1. [Frameworks](#frameworks)
2. [Setup Instructions](#setup-instructions)
3. [Comparison of Frameworks](#comparison-of-frameworks)
4. [Contributing](#contributing)
5. [License](#license)

## Frameworks

| **Framework**     | **Description**                                                 | **Documentation**          |
|--------------------|-----------------------------------------------------------------|----------------------------|
| **Phidata**        | A Python-based framework for converting LLMs into agents.       | [Phidata Docs](#)          |
| **OpenAI_Swarm**   | An experimental, lightweight multi-agent orchestration framework by OpenAI. | [OpenAI Swarm GitHub](#)   |
| **CrewAI**         | A framework for building and deploying AI agents with extensive integrations. | [CrewAI Docs](#)           |
| **Autogen**        | An open-source framework for building agentic systems.          | [Autogen GitHub](#)        |
| **LangGraph**      | A node-based framework for complex AI workflows within the LangChain ecosystem. | [LangGraph GitHub](#)      |

## Setup Instructions

### Prerequisites
- Python 3.10+
- Virtual environment (recommended)

### General Setup
1. Clone the Repository:
    ```bash
    git clone https://github.com/yourusername/multi-agent-ai-frameworks.git
    ```
2. Navigate to the Framework Folder:
    ```bash
    cd multi-agent-ai-frameworks/<framework_name>
    ```
3. Set Up Virtual Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the Example:
    ```bash
    python example.py
    ```

## Comparison of Frameworks

| **Feature**               | **Phidata** | **OpenAI_Swarm** | **CrewAI** | **Autogen** | **LangGraph** |
|---------------------------|-------------|------------------|------------|-------------|---------------|
| **Ease of Use**           | High        | Medium           | High       | Medium      | Medium        |
| **Scalability**           | High        | High             | High       | High        | High          |
| **Integration Capabilities** | High    | Medium           | High       | Medium      | Medium        |
| **Community Support**     | Medium      | Low              | High       | Medium      | Medium        |
| **Cost**                  | Free        | Free             | Free       | Free        | Free          |

## Contributing
We welcome contributions! If you'd like to add more frameworks or improve existing examples, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License
This repository is licensed under the [MIT License](LICENSE).
