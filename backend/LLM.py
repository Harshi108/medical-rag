import os
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

load_dotenv()

MODEL_NAME = "microsoft/phi-2"
generator = None

def load_model():
    global generator

    if generator is None:
        print("Loading tokenizer...")

        tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True
        )

        print("Loading model...")

        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )

        print("Creating pipeline...")

        generator = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer
        )

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

print("Loading model...")
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
    low_cpu_mem_usage = True
)

print("Creating pipeline...")
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)


def generate_answer(question, context):
    load_model()

    prompt = f"""
You are a helpful Medical AI Assistant.

Instructions:
-answer only using the providedd context
-do not make up information
-if the context does not contain the answer, reply:"i couldnt find that information in the uploaded medical documents"

Context:
{context}

Question:
{question}

Answer:
"""

    response = generator(
        prompt,
        max_new_tokens=150,
        do_sample=False,
        return_full_text=False
    )

    return response[0]["generated_text"]


if __name__ == "__main__":

    answer = generate_answer(
        "What are the symptoms of diabetes?",
        """
        Symptoms of diabetes include increased thirst,
        frequent urination,
        fatigue,
        blurred vision,
        and unexplained weight loss.
        """
    )

    print("\nAnswer:\n")
    print(answer)