from pydantic import BaseModel

class TransactionInput(BaseModel):
    step:int
    type:int
    amount:float
    oldbalanceOrg:float
    newbalanceOrig:float
    oldbalanceDest:float
    newbalanceDest:float
    balance_diff_orig:float
    balance_diff_dest:float
    amount_to_balance_ratio:float
    is_zero_balance_org:int
    is_zero_balance_dest:int
    hour_of_day:int