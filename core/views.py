from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Filing

@csrf_exempt
def receive_filing(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Filing.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                filing_date=data.get('filing_date')
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST allowed'})
