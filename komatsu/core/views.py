from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import OS
from django.views.decorators.csrf import csrf_exempt



def actualizar_estado_trabajo(request):
    print("La vista se ha ejecutado correctamente")
    if request.method == 'POST':
        print("La vista LLEGO AQUI 01")
        os_id = request.POST.get('os_id')
        print("La vista LLEGO AQUI 02")
        nuevo_estado_trabajo = request.POST.get('nuevo_estado_trabajo')
        print("La vista LLEGO AQUI 03")
        try:
            print("Entra al try")
            # Obtener el objeto OS y actualizar su estado de trabajo
            os_obj = OS.objects.get(id=os_id)
            print("pasas el obj")
            os_obj.estado_trabajo = nuevo_estado_trabajo
            os_obj.estado = 'IN_PROCESS'  # Cambiar el estado a IN_PROCESS
            os_obj.save()
            return JsonResponse({'success': True})
        except OS.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'La orden de servicio no existe.'})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido.'})




def actualizar_os(request):
    if request.method == 'POST':
        motivo = request.POST.get('motivo')
        # Realiza las operaciones necesarias con el motivo
        # Por ejemplo, guardar en la base de datos
        
        # Redirige al usuario a la página os_list
        return redirect('os_list')
    else:
        return HttpResponse('Método no permitido', status=405)

def actualizar_os(request, os_id, estado_trabajo):
    os_instance = get_object_or_404(OS, pk=os_id)

    if estado_trabajo.upper() == 'ARMADO':
        # Actualizar el estado de trabajo del OS
        os_instance.estado_trabajo = 'ARMADO'
    elif estado_trabajo.upper() == 'DESARME':
        # Actualizar el estado de trabajo del OS
        os_instance.estado_trabajo = 'DESARME'
    else:
        # Devolver un error si la opción de estado de trabajo no es válida
        return JsonResponse({'error': 'Opción de estado de trabajo no válida.'}, status=400)

    # Cambiar el estado del OS de "TODO" a "IN_PROCESS"
    os_instance.estado = 'IN_PROCESS'

    # Guardar los cambios en la base de datos
    os_instance.save()

    # Devolver una respuesta exitosa
    return JsonResponse({'message': 'OS actualizado exitosamente.'})


def detalle_os(request, os_id):
    # Aquí puedes agregar lógica para obtener los datos del OS con el ID proporcionado
    # Por ejemplo, supongamos que tienes un modelo llamado OS y deseas obtener los datos del OS:
    # os = OS.objects.get(pk=os_id)

    # Por ahora, asumamos que no hay lógica adicional y solo renderizamos la página
    return render(request, 'core/detalle_os.html', {'os_id': os_id})

@csrf_exempt
def update_os_estado_trabajo(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        os_id = data['os_id']
        estado_trabajo = data['estado_trabajo']

        os_instance = OS.objects.get(pk=os_id)
        os_instance.estado_trabajo = estado_trabajo
        os_instance.save()

        return JsonResponse({'message': 'Estado de trabajo actualizado correctamente.'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def os_list(request):
    os_dict = {
        'TODO': OS.objects.filter(estado='TODO'),
        'IN_PROCESS': OS.objects.filter(estado='IN_PROCESS'),
        'DONE': OS.objects.filter(estado='DONE'),
    }

    if request.method == 'POST':
        os_ids = request.POST.getlist('os_id')
        estados_trabajo = request.POST.getlist('estado_trabajo')
        for os_id, estado_trabajo in zip(os_ids, estados_trabajo):
            os = OS.objects.get(pk=os_id)
            os.estado_trabajo = estado_trabajo
            os.save()
        return redirect('os_list')

    return render(request, 'core/os_list.html', {'os_dict': os_dict})



def update_os_estado_trabajo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        os_id = data['os_id']
        estado_trabajo = data['estado_trabajo']

        os_instance = OS.objects.get(pk=os_id)
        os_instance.estado_trabajo = estado_trabajo
        os_instance.save()

        return JsonResponse({'message': 'Estado de trabajo actualizado correctamente.'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def pantalla_principal(request):
    todo_os = OS.objects.filter(estado='TODO')
    in_process_os = OS.objects.filter(estado='IN_PROCESS')
    done_os = OS.objects.filter(estado='DONE')
    return render(request, 'core/pantalla_principal.html', {'todo_os': todo_os, 'in_process_os': in_process_os, 'done_os': done_os})

def iniciar_os(request, os_id):
    os = OS.objects.get(pk=os_id)
    if request.method == 'POST':
        os.estado_trabajo = request.POST.get('estado_trabajo')
        os.estado = 'IN_PROCESS'
        os.save()
        # Implementa el resto de la lógica aquí
    return render(request, 'core/iniciar_os.html', {'os': os})
