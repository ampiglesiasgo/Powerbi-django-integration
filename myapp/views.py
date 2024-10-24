from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def powerbi_report(request):
    # Aquí puedes pasar la URL de embed del reporte a la plantilla
    context = {
        'embed_url': 'https://app.powerbi.com/reportEmbed?reportId=de793919-dad1-4fcb-a454-083a6525c8fa&autoAuth=true&ctid=c9d3fdbd-45f2-469e-a4fa-200c24d97f45'
    }
    return render(request, 'powerbi_report.html', context)