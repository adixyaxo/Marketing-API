
from pydantic import BaseModel, ConfigDict # BaseModel is a class which is inherited into the class you want to apply types to


from pydantic import Field # Field kisi bhi field ko optional ya required banane ke liye use hota hai

from pydantic import field_validator, model_validator, computed_field

from  typing import Optional, Literal

from typing import List

class Marketing(BaseModel):
  Campaign_ID:int = Field(...,ge=0, description="Unique identifier for the marketing campaign")
  Company:str = Field(..., description="Name of the company")
  Campaign_Type:str = Field(..., description="Type of the marketing campaign")
  Target_Audience:str = Field(..., description="Target audience for the campaign")
  Duration:int = Field(...,ge=0, description="Duration of the campaign in days")
  Sales:float = Field(...,ge=0, description="Total sales generated from the campaign")
  Profit:float = Field(default=None,ge=0, description="Total profit generated from the campaign")
  Profit_Margin:float = Field(default=None,ge=0, description="Profit margin as a percentage")

  @field_validator("Campaign_Type")
  @classmethod
  def validate_campaign_type(cls, value):
    return value.title()

  @field_validator("Target_Audience")
  @classmethod
  def validate_target_audience(cls, value):
    return value.title()

  @field_validator("Company")
  @classmethod
  def validate_company(cls, value):
    return value.title()

  @field_validator("Duration")
  @classmethod
  def validate_duration(cls, value):
    if value < 0:
      raise (-1)*value
    return value

  @model_validator(mode="after")
  def calculate_profit_margin(self):
    if self.Profit_Margin is None and self.Sales > 0:
      if self.Sales > 0:
        self.Profit_Margin = (self.Profit / self.Sales) * 100
      return self
    else:
      return self

  @model_validator(mode="after")
  def calculate_profit(self):
    if self.Profit is None and self.Sales > 0:
      self.Profit = self.Sales * self.Profit_Margin / 100
      return self
    else:
      return self