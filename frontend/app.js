const form = document.getElementById("predictionForm");
const resultBox = document.getElementById("result");
const errorBox = document.getElementById("error");

const API_URL = "http://127.0.0.1:8000/predict";

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    resultBox.classList.add("hidden");
    errorBox.classList.add("hidden");

    const payload = {
        hours_studied: Number(document.getElementById("hoursStudied").value),
        sleep_hours: Number(document.getElementById("sleepHours").value),
        attendance_rate: Number(document.getElementById("attendanceRate").value),
        previous_score: Number(document.getElementById("previousScore").value)
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail ? "Invalid input values." : "Prediction request failed.");
        }

        const data = await response.json();

        resultBox.textContent = `Predicted Exam Score: ${data.predicted_score.toFixed(2)}`;
        resultBox.classList.remove("hidden");

    } catch (error) {
        errorBox.textContent = error.message;
        errorBox.classList.remove("hidden");
    }
});