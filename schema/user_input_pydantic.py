from pydantic import BaseModel , Field
from typing import Annotated,Optional

class UserInput(BaseModel):
   
   senior_citizen : Annotated[str ,Field(...,description="is user is senior citizen or not" ,example="Yes")]
   partner:  Annotated[str ,Field(...,description="Does user has partner ('Married or Unmarried')", example="Yes")]
   dependents : Annotated[str,Field(..., description="user has any dependents",example="No")]      
   tenure   :  Annotated[int , Field(...,description="how many months the customer has been with company",examples=["0","1" ,"2","3","4"])]
   phone_service  : Annotated[str ,Field(..., description="Services Subscribed user having phone_service",example="Yes")]
   multiple_lines:Annotated[str , Field(...,description="Services Subscribed what services the user has",example="No phone service")]
   internet_service:Annotated[str ,Field(...,description="Services Subscribed what Internet Service user using", example="DSL")]
   online_security: Annotated[str ,Field(...,description="Online security Internet add-on services", example="No")]
   online_backup: Annotated[str ,Field(...,description="Online backup Internet add-on services", example="No")]
   device_protection: Annotated[str ,Field(...,description="Device protection Internet add-on services", example="No")] 
   tech_support: Annotated[str ,Field(...,description="Device protection Internet add-on services", example="No")]
   streaming_tv: Annotated[str ,Field(...,description="Streaming tv Internet add-on services", example="No")] 
   streaming_movies: Annotated[str ,Field(...,description="Streaming movies Internet add-on services", example="No")] 
   contract: Annotated[str , Field(..., example="Month-to-month")]
   paperless_billing: Annotated[str ,Field(...,description="Paperless Billing methode", example="Yes")]
   payment_method: Annotated[str ,Field(...,description="Billing methode", example="Electronic check")]
   monthly_charges: Annotated[float ,Field(...,description="Monthly Charges What they pay each month", example=70.35)]
   total_charges: Optional[float] = Field(None,description="Total charges paid by customer",example=845.5)


COLUMN_MAPPING = {
    "senior_citizen": "Senior Citizen",
    "partner": "Partner",
    "dependents": "Dependents",
    "tenure": "Tenure",
    "phone_service": "Phone Service",
    "multiple_lines": "Multiple Lines",
    "internet_service": "Internet Service",
    "online_security": "Online Security",
    "online_backup": "Online Backup",
    "device_protection": "Device Protection",
    "tech_support": "Tech Support",
    "streaming_tv": "Streaming TV",
    "streaming_movies": "Streaming Movies",
    "contract": "Contract",
    "paperless_billing": "Paperless Billing",
    "payment_method": "Payment Method",
    "monthly_charges": "Monthly Charges",
    "total_charges": "Total Charges"
}
