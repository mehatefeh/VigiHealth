def analyze_blood_pressure(systolic, diastolic, pulse):
    if systolic > 140 or diastolic > 90:
        status = "فشار خون بالا! لطفاً با پزشک تماس بگیرید."
    elif systolic < 90 or diastolic < 60:
        status = "فشار خون پایین! مراقب باشید."
    else:
        status = "فشار خون شما نرمال است. ادامه دهید."

    return {
        "status": status,
        "advice": "ورزش منظم و تغذیه سالم را فراموش نکنید."
    }
