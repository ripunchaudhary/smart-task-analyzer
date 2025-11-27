from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskInputSerializer
from .scoring import calculate_scores, get_top_suggestions


# STRATEGY WEIGHTS

STRATEGIES = {
    "fastest": {"w_u": 0.1, "w_i": 0.2, "w_e": 0.6, "w_d": 0.1},
    "impact": {"w_u": 0.15, "w_i": 0.7, "w_e": 0.05, "w_d": 0.1},
    "deadline": {"w_u": 0.7, "w_i": 0.1, "w_e": 0.05, "w_d": 0.15},
    "smart": {"w_u": 0.35, "w_i": 0.35, "w_e": 0.15, "w_d": 0.15},
}


# ANALYZE API  (POST)

class AnalyzeTasks(APIView):
    def post(self, request):
        strategy = request.GET.get("strategy", "smart")

        serializer = TaskInputSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        tasks = serializer.validated_data
        scores = calculate_scores(tasks, STRATEGIES[strategy])

        return Response(scores)



# SUGGEST API (POST)

@api_view(['POST'])
def suggest_tasks(request):
    """Returns top 3 recommended tasks with explanations."""
    strategy = request.GET.get("strategy", "smart")

    # Validate input tasks
    serializer = TaskInputSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)

    tasks = serializer.validated_data

    # Calculate scores
    scored = calculate_scores(tasks, STRATEGIES[strategy])

    # Pick top 3 tasks
    suggestions = get_top_suggestions(scored, limit=3)

    return Response(suggestions)
