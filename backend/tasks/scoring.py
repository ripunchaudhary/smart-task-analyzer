from datetime import date

def calculate_scores(tasks, weights):
    today = date.today()
    
    # blockers count
    blockers = {t['task_id']: 0 for t in tasks}
    for t in tasks:
        for dep in t.get("dependencies", []):
            if dep in blockers:
                blockers[dep] += 1

    results = []

    for t in tasks:
        # Urgency calc
        if "due_date" in t and t["due_date"]:
            days = (t["due_date"] - today).days
            if days < 0:
                urgency = 1.0
            else:
                urgency = max(0, 1 - (days / 30))
        else:
            urgency = 0.3

        # Importance (normalize)
        importance = t.get("importance", 5) / 10

        # Effort (lower hours = higher score)
        hours = t.get("estimated_hours", 4)
        effort = 1 - min(hours / 8, 1)

        # Dependency score
        dependency = min(blockers[t["task_id"]] / 5, 1)

        final_score = (
            urgency * weights['w_u'] +
            importance * weights['w_i'] +
            effort * weights['w_e'] +
            dependency * weights['w_d']
        )

        results.append({
            "task_id": t["task_id"],
            "title": t["title"],
            "score": round(final_score, 3),
            "urgency": urgency,
            "importance": importance,
            "effort": effort,
            "dependency": dependency
        })

    return sorted(results, key=lambda x: x["score"], reverse=True)



# NEW FUNCTION FOR SUGGEST API
    

def get_top_suggestions(scored_tasks, limit=3):
    """Returns top N tasks with explanation."""
    suggestions = []

    for t in scored_tasks[:limit]:
        reason = (
            f"Urgency: {t['urgency']:.2f}, "
            f"Importance: {t['importance']:.2f}, "
            f"Effort: {t['effort']:.2f}, "
            f"Dependency: {t['dependency']:.2f}. "
            f"Final score: {t['score']}"
        )

        suggestions.append({
            "task_id": t["task_id"],
            "title": t["title"],
            "score": t["score"],
            "reason": reason
        })

    return suggestions



# Optional Check (not required for Django)

if __name__ == "__main__":
    sample_tasks = [
        {
            "task_id": "1",
            "title": "Finish report",
            "due_date": date(2024, 7, 10),
            "estimated_hours": 3,
            "importance": 8,
            "dependencies": []
        },
        {
            "task_id": "2",
            "title": "Prepare presentation",
            "due_date": date(2024, 7, 5),
            "estimated_hours": 5,
            "importance": 9,
            "dependencies": ["1"]
        },
        {
            "task_id": "3",
            "title": "Team meeting",
            "due_date": None,
            "estimated_hours": 1,
            "importance": 6,
            "dependencies": []
        }
    ]

    weights = {
        'w_u': 0.4,
        'w_i': 0.3,
        'w_e': 0.2,
        'w_d': 0.1
    }

    scores = calculate_scores(sample_tasks, weights)
    for score in scores:
        print(score)

    print("\nTop Suggestions:")
    print(get_top_suggestions(scores, limit=3))
