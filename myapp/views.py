from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def powerbi_report(request):
    # Aquí puedes pasar la URL de embed del reporte a la plantilla
    context = {
        'embed_url': 'https://app.powerbi.com/view?r=eyJrIjoiNGI4NTUyMzItN2M1ZC00N2FlLWExY2ItMDQ1OGUxNjQyZjQ3IiwidCI6ImM5ZDNmZGJkLTQ1ZjItNDY5ZS1hNGZhLTIwMGMyNGQ5N2Y0NSIsImMiOjR9'
    }
    return render(request, 'powerbi_report.html', context)