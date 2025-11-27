async function analyze() {
    const rawText = document.getElementById("jsonInput").value;
    const strategy = document.getElementById("strategy").value;

    let tasks;

    // Safe JSON parse
    try {
        tasks = JSON.parse(rawText);
    } catch (e) {
        alert("❌ Invalid JSON format!");
        return;
    }

    // API Call
    let response = await fetch(`http://127.0.0.1:8000/api/tasks/analyze/?strategy=${strategy}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(tasks)
    });

    let data = await response.json();

    displayResultCards(data);
}

// Priority color class based on score
function getPriorityClass(score) {
    if (score >= 0.60) return "high";     // red
    if (score >= 0.40) return "medium";   // yellow
    return "low";                         // green
}

// Render cards
function displayResultCards(data) {
    const output = document.getElementById("output");
    output.innerHTML = "";  // clear previous results

    data.forEach(task => {
        const card = document.createElement("div");
        card.className = `card ${getPriorityClass(task.score)}`;

        card.innerHTML = `
            <h3>${task.title} — <strong>${task.score}</strong></h3>

            <p><strong>Urgency:</strong> ${task.urgency.toFixed(2)}</p>
            <p><strong>Importance:</strong> ${task.importance.toFixed(2)}</p>
            <p><strong>Effort:</strong> ${task.effort.toFixed(2)}</p>
            <p><strong>Dependency:</strong> ${task.dependency.toFixed(2)}</p>
        `;

        output.appendChild(card);
    });
}
