def calculate_risk_score(probability):
    """
    Convert probability into score out of 100
    """
    return round(probability * 100)


def get_risk_category(score):

    if score >= 80:
        return "High Risk"

    elif score >= 50:
        return "Medium Risk"

    else:
        return "Low Risk"