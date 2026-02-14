from flask import Flask, render_template, request

app = Flask(__name__)
def get_difficulty_weight(level):
    if level.lower() == "easy":
        return 1
    elif level.lower() == "medium":
        return 2
    elif level.lower() == "hard":
        return 3
    return 1


@app.route("/", methods=["GET", "POST"])
def index():
    study_plan = {}

    if request.method == "POST":
        subjects = request.form.getlist("subject")
        marks = request.form.getlist("marks")
        difficulties = request.form.getlist("difficulty")
        total_hours = float(request.form["total_hours"])

        priorities = {}
        total_priority = 0

        for i in range(len(subjects)):
            weight = get_difficulty_weight(difficulties[i])
            priority = (100 - int(marks[i])) * weight
            priorities[subjects[i]] = priority
            total_priority += priority

        for subject, priority in priorities.items():
            hours = (priority / total_priority) * total_hours
            study_plan[subject] = round(hours, 2)

    return render_template("index.html", study_plan=study_plan)


if __name__ == "__main__":
    app.run(debug=True)

