from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class person(BaseModel):

    name: str = Field(description="Name of the person"),
    age: int = Field(gt=18, description="Age of the person"),
    location: str = Field(description="Location of the person where he/she belongs from")


parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template="provide the name, age and location of a {place} person \n {format_instructions}",
    input_variables=['place'],
    partial_variables={"format_instructions": parser.get_format_instructions}
)

prompt = template.invoke({'place':"Saudi"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

chain = template|model|parser
result = chain.invoke({'place':'Saudi'})