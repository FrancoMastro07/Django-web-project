def total_value(request):
    total = 125
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total += (float(value["price"]) * value["amount"])
    return {"total_amount":total}