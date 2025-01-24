from langchain_ollama import ChatOllama

def create_ollama_client(model: str) -> ChatOllama:
    return ChatOllama(
        model=model,
        temperature=0
    )

def generate_response(task: str, prompt: str, llm: ChatOllama):
    """Function to generate a response from the LLM given a specific task and user prompt"""

    messages = [
        ("system", f"You are a helpful assistant that is tasked to {task}"),
        ("human", prompt)
    ]

    response = llm.invoke(messages)
    return response.content

def email_checker(task: str, specifics: str | None, rules: list[str] | None, salutations: list[str] | None, names: list[str] | None, data: dict, llm: ChatOllama):
    content: str = "" if specifics is None else specifics
    email_rules: str = "No specific rules" if rules is None else ', '.join(rules)
    possible_salutations: str = "Good day" if salutations is None else ", ".join(salutations)
    possible_names: str = "" if names is None else ", ".join(names)

    prompt = ""
    output = "" if task not in ["checker", "crafting"] else data["expected_outputs"][task]
    email_specs = f"""
    The following are the email specifications to be considered to meet the email etiquette standards:

    Rules: {email_rules}

    Possible saluations in email: {possible_salutations}

    Names indicated in the email: {possible_names}

    The email should follow the rules, use any of the possible salutations, and specify one (or more) of the names in the email stated above.
    """
    llm_task = "" if task not in ["checker", "crafting"] else data["tasks"][task]

    if task == "checker":
        prompt = f"Check if the email follows the proper etiquette. {email_specs}\n\nMy email is as follows: {content}\n\nThe output of the email should be a {output}."
    elif task == "crafting":
        prompt = f"Generate an email that follows the proper etiquette. {email_specs}. \n\nThe email should be about {content}.\n\nThe output of the email should be a {output}."
    else:
        return "Not part of the task"
    
    return generate_response(llm_task, prompt, llm)
