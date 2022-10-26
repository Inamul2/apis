import traceback

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerData
from .serializers import CustomerSerializer


class searchCustomers(APIView):

    def post(self, request):
        try:
            self.validate(request)
            if not request.data['searchTerm']:
                if request.data['Order of response'] == "ASC":
                    data = CustomerData.objects.all().order_by('name')
                else:
                    data = CustomerData.objects.all().order_by('-name')
            else:
                if request.data['Order of response'] == "ASC":
                    data = CustomerData.objects.filter(name__icontains=request.data['searchTerm']).order_by('name')
                else:
                    data = CustomerData.objects.filter(name__icontains=request.data['searchTerm']).order_by('-name')
            serialize = CustomerSerializer(data, many=True)
            return Response({'Status': 'Success', "Message": "List of Customer retrieved Successfully",
                             "Customers": serialize.data}, status=status.HTTP_200_OK)

        except Exception as e:
            if str(e) in ["'searchTerm' key missing in the request body",
                          "'Order of response' key can only have value of ASC or DESC",
                          "JSON have no keys"]:
                return Response({'Status': 'Failed', "Error": str(e)}, status=400)
            return Response({'Status': 'Failed', "Error": "Some Internal Error Occured - " + str(e)}, status=500)

    def validate(self, request):
        if not request.data:
            raise Exception("JSON have no keys")
        if "searchTerm" not in request.data:
            raise Exception("'searchTerm' key missing in the request body")
        if "Order of response" in request.data:
            if request.data['Order of response'] not in ["ASC", "DESC"]:
                raise Exception("'Order of response' key can only have value of ASC or DESC")


class addCustomers(APIView):

    def post(self, request):
        try:
            name = request.data['name']
            dob = request.data['dob']
            address = request.data['address']
            phoneNumber = request.data['phoneNumber']
            emailAddress = request.data['emailAddress']
            city = request.data['city']
            state = request.data['state']
            country = request.data['country']
            pinCode = request.data['pinCode']
            CustomerData.objects.create(name=name, dob=dob, address=address, phoneNumber=phoneNumber,
                                        emailAddress=emailAddress, city=city, state=state, country=country,
                                        pinCode=pinCode)

            serialize = CustomerSerializer(request.data)
            return Response({'Status': 'Success', "Message": "Customer Added Successfully", "Customer": serialize.data},
                            status=status.HTTP_200_OK)
        except Exception:
            print(traceback.format_exc())
            return Response({'Status': 'Failed', "Error": "Some Internal Error Occured"}, status=500)
