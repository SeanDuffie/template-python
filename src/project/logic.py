""" @file logic.py
    @author Sean Duffie
    @brief 

Raises:
    ValueError: The API KEY was not found in the .env file.
"""

from loguru import logger
from project.models import UserProfile, CalculationResult
from project.utils import slugify

def process_data(input_value: int) -> int:
    """
    Core business logic: Multiplies a value by 2.
    In a real app, this would be your math, database queries, 
    or AI model calls.
    """
    logger.debug(f"Processing data with input: {input_value}")
    
    if input_value < 0:
        logger.warning("Received a negative value!")
        
    result = input_value * 2
    
    logger.info(f"Logic complete. Result: {result}")
    return result

def process_user_request(user_data: dict, val: int) -> CalculationResult:
    """
    Orchestrates a request by validating the user and 
    executing the core logic.
    """
    # 1. Validation: Convert dict to Pydantic model (fails loud if data is bad)
    user = UserProfile(**user_data)
    logger.info(f"Processing request for user: {user.username}")

    # 2. Logic: Call the core engine
    result_val = process_data(val)
    
    # 3. Utilities: Optional side-task (e.g., logging a 'slugified' name)
    logger.debug(f"Task slug: {slugify(user.username)}")

    # 4. Return: Wrap the output in a structured Result model
    return CalculationResult(
        input_value=val, 
        output_value=result_val
    )
