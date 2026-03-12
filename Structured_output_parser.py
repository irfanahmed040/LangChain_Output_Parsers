from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers.structured import StructuredOutputParser, ResponseSchema #structured output parser is no longer supported ... use Pydantic output parser instead



load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


schema = [
    ResponseSchema(name = 'fact_1', description = "Fact 1 about topic"),
    ResponseSchema(name = 'fact_2', description = "Fact 2 about topic"),
    ResponseSchema(name = 'fact_3', description = "Fact 3 about topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)


template = PromptTemplate(
    template="Give 3 facts about the topic : {topic}\n{format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'Black Hole theory'})
# result = model.invoke(prompt)
# Final_result = parser.parse(result.content)
# print(Final_result)

chain = template|model|parser
result = chain.invoke({'topic':'black hole'})
print(result)