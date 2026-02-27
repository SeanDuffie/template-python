""" @file models.py
    @author Sean Duffie
    @brief This ensures that when data moves between your API, CLI, and Logic, it is always valid.
"""

from pydantic import BaseModel, Field
from datetime import datetime

class UserProfile(BaseModel):
    """A professional data model for a User."""
    username: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool = True

class CalculationResult(BaseModel):
    """The structured output of our logic engine."""
    input_value: int
    output_value: int
    timestamp: datetime = Field(default_factory=datetime.now)
