from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.
from django.shortcuts import render
from .forms import AddressForm

class ReactView(APIView):

    serializer_class = ReactSerializer

    def get(self, request):
        output = [{"employee": output.employee, "department": output.department}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):

        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# class ReactView(APIView):

#     serializer_class = ReactSerializer

#     def get(self, request):
#         output = [{"employee": output.employee, "department": output.department}
#                   for output in React.objects.all()]
#         return Response(output)

#     def post(self, request):

#         serializer = ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

from django.shortcuts import render,redirect
from .forms import AddressForm

def add_record(APIView):
    serializer_class = AdressSerializer
    def get(self, request):
        output = [{"employee": output.employee, "department": output.department}
                  for output in React.objects.all()]
        return Response(output)
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = AddressForm()

    return render(request, 'add_record.html', {'form': form})

