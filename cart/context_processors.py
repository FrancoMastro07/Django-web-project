def total_value(request):
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total += float(value["price"])
    else:
        total = "You have to log-in to see the shopping cart"
    return {"total_value":total}