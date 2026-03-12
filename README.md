# LangChain Output Parsers

This repository demonstrates structured output parsing techniques in LangChain using different output parsers including:

- StrOutputParser
- JsonOutputParser
- PydanticOutputParser
- StructuredOutputParser (legacy)

The goal of this project is to understand how to enforce deterministic, structured responses from language models and convert raw LLM output into usable Python objects.

The examples use HuggingFace models through LangChain and focus on building reliable output pipelines for downstream processing.

---

# Architecture Goal

Large Language Models return text by default.

In real applications, we often need:

- JSON
- Typed objects
- Validated schemas
- Clean strings
- Structured data

LangChain Output Parsers allow us to convert model output into structured formats.

This repository explores multiple parser types and chaining patterns.

---

# Repository Structure

```
LANGCHAIN OUTPUT PARSERS/
│
├── jsonoutputparser.py
├── Pydantic_outputparser.py
├── Stroutputparser.py
├── Structured_output_parser.py
├── stroutputparser1.py
├── test.py
├── requirements.txt
└── .env
```

---

# File-by-File Explanation

## 1. jsonoutputparser.py

Purpose:
Demonstrates `JsonOutputParser` for converting LLM output into Python dictionaries.

What it does:

- Uses PromptTemplate with format instructions
- Injects parser instructions into prompt
- Calls HuggingFace model
- Parses output into JSON

Key concepts:

- format_instructions
- parser.get_format_instructions()
- template | model | parser chain
- automatic dictionary conversion

Result type:

```
dict
```

Use case:

- APIs
- Structured responses
- Data extraction
- Tool calling pipelines

---

## 2. Pydantic_outputparser.py

Purpose:
Demonstrates `PydanticOutputParser` for schema-validated output.

What it does:

- Defines Pydantic model
- Enforces field types
- Validates LLM output
- Parses response into typed object

Example schema:

- name
- age
- location

Key concepts:

- BaseModel
- Field validation
- Schema enforcement
- Deterministic outputs

Result type:

```
Pydantic object
```

Use case:

- Production systems
- Agents
- Tool calls
- API responses
- Typed pipelines

This is the recommended parser for modern LangChain workflows.

---

## 3. Stroutputparser.py

Purpose:
Demonstrates `StrOutputParser` for simple text parsing and chaining.

What it does:

- Generates detailed report
- Feeds output into another prompt
- Generates summary
- Uses chain operator

Pipeline:

Prompt → Model → Parser → Prompt → Model → Parser

Key concepts:

- chaining
- multi-step prompts
- text transformation
- output reuse

Result type:

```
string
```

Use case:

- summarization pipelines
- multi-step reasoning
- RAG post-processing
- report generation

---

## 4. Structured_output_parser.py

Purpose:
Demonstrates legacy `StructuredOutputParser`.

Note:
This parser is deprecated in newer LangChain versions.
PydanticOutputParser should be used instead.

What it does:

- Defines response schema manually
- Generates format instructions
- Parses model output

Key concepts:

- ResponseSchema
- StructuredOutputParser
- format instructions
- schema-based parsing

Result type:

```
dict
```

Use case:

- older LangChain versions
- simple schema parsing

---

## 5. stroutputparser1.py

Purpose:
Additional experiments with string parsing and chaining.

Used for testing parser pipelines and prompt chaining behavior.

---

## 6. test.py

Purpose:
Testing file for experimenting with parser behavior.

Used for debugging and quick validation of parser output.

---

## 7. requirements.txt

Contains dependencies for:

- langchain
- langchain-core
- langchain-huggingface
- transformers
- python-dotenv
- pydantic

The repository is configured to work with HuggingFace models.

---

## 8. .env

Used for storing environment variables.

Example:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

This file should not be committed.

---

# Concepts Covered

- Output parsing
- JSON parsing
- Schema validation
- Prompt format instructions
- Parser chaining
- Typed outputs
- HuggingFace integration
- Prompt → Model → Parser pipeline

---

# Installation

```
git clone https://github.com/irfanahmed040/Langchain-output-parsers.git
cd Langchain-output-parsers
```

Create virtual environment

```
python -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Create `.env`

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

# Running Examples

```
python jsonoutputparser.py
```

```
python Pydantic_outputparser.py
```

```
python Stroutputparser.py
```

```
python Structured_output_parser.py
```

---

# Engineering Focus

This repository focuses on:

- Deterministic LLM output
- Structured responses
- Schema validation
- Prompt-parser pipelines
- Reliable AI system design

These patterns are required for building:

- RAG systems
- AI agents
- Tool calling models
- Production LLM services
