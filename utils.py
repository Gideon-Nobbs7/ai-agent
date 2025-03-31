import re


def extract_details(prompt: str):
    product_pattern = r"(price of the|show me|find|list|what phone|phones|laptops|items|have|budget of|amount of|more than) (.+?)(?:\?| with| under|$)"                        
    budget_pattern = r"(\d+)"

    product_match = re.search(product_pattern, prompt, re.IGNORECASE)
    product_name = product_match.group(2) if product_match else None
                                          
    budget_match = re.search(budget_pattern, prompt)
    budget = int(budget_match.group(0)) if budget_match else None

    return product_name, budget
