from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

# Create 

def workers_list(request):
    # Execute raw SQL to fetch data from the workers table in the deploy-test database
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, age FROM workers")
        rows = cursor.fetchall()

    # Prepare data to pass to the template
    workers_data = []
    for row in rows:
        workers_data.append({
            'id': row[0],
            'name': row[1],
            'email': row[2],
            'age': row[3],
        })

    # Render the template with the data
    return render(request, 'workers_list.html', {'workers_data': workers_data})