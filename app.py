from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Unit Converter</title>
</head>
<body>
    <h2>Unit Converter</h2>

    <form method="post">
        <input type="number" step="any" name="value" placeholder="Enter value" required>

        <select name="conversion">
            <option value="c_to_f">Celsius to Fahrenheit</option>
            <option value="km_to_miles">KM to Miles</option>
            <option value="kg_to_pounds">KG to Pounds</option>
        </select>

        <button type="submit">Convert</button>
    </form>

    {% if result %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def convert():
    result = None

    if request.method == "POST":
        value = float(request.form["value"])
        conversion = request.form["conversion"]

        if conversion == "c_to_f":
            result = (value * 9/5) + 32
        elif conversion == "km_to_miles":
            result = value * 0.621371
        elif conversion == "kg_to_pounds":
            result = value * 2.20462

    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

