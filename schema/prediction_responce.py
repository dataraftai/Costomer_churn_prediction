from pydantic import BaseModel ,Field

class PredictionResponce(BaseModel):
    predicted : int = Field(...,description="prediction for are customers are likely to be expensive",example=0)
    churn_label : str = Field(...,description="The predicted category for are customers are likely to be churn or not churn",example="Churn")
    churn_probability : float = Field(...,description="Confidance score for more like to be predicted (range 0 to 1) ")
