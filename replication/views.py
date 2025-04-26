from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import json
from .models import FilingRecord
from django.shortcuts import render

@csrf_exempt
def receive_filing(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            content = data.get('content')

            # Save the received data into the database
            FilingRecord.objects.create(title=title, content=content)

            return JsonResponse({'status': 'success', 'message': 'Filing entry received successfully at replica!'})
        
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': f'JSON Decode Error: {str(e)}'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error: {str(e)}'})

    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'})

def view_filing_records(request):
    # Retrieve all filing records from the database
    records = FilingRecord.objects.all()
    return render(request, 'replica/view_filing_records.html', {'records': records})
