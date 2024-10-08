from django.shortcuts import render

# Create your views here.

#from rest_framework import generics
from rest_framework.views import APIView
from userprof.models import *
from .serializers import *
#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated,AllowAny

'''''
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET','POST','DELETE','PUT','PATCH'])
def userprofotest(request):
   if request.method == 'GET':
       TESTO ={
      'A':'a',
      'B':['b','e'],
      'C':'c',
       }
       return Response(TESTO)

   elif request.method == 'POST':
       data=request.data
       print('in post')
       print(data)

       return Response(data)
   
@api_view(['GET','POST','DELETE','PUT','PATCH','DELETE'])
def userprofo(request):
       if request.method == 'GET':
            #data = testomodel.objects.all()
            data = testomodel.objects.filter(color__isnull=False)
            #data1=deletebutton.objects.all()
            serilizers=testomodelserial(data,many=True)
            return Response(serilizers.data)
       elif request.method == 'POST':
            data = request.data
            serilizers=testomodelserial(data=data)
            if serilizers.is_valid():
                 serilizers.save()
                 return Response(serilizers.data) 
            return Response(serilizers.errors)  
       elif request.method == 'PUT':
            data = request.data
            obj=testomodel.objects.get(id=data['id'])
            serilizers=testomodelserial(obj,data=data)
            if serilizers.is_valid():
                 serilizers.save()
                 return Response(serilizers.data) 
            return Response(serilizers.errors) 
       elif request.method == 'PATCH':
            data = request.data
            obj=testomodel.objects.get(id=data['id'])
            serilizers=testomodelserial(obj,data=data,partial=True)
            if serilizers.is_valid():
                 serilizers.save()
                 return Response(serilizers.data) 
            return Response(serilizers.errors)  
       else :
            data = request.data
            obj=testomodel.objects.get(id=data['id'])
            obj.delete()
            return Response({'message':'deleteddd'})  
'''
@permission_classes([AllowAny]) 
@api_view(['POST'])            
def registrationuser(request):
     if request.method=='POST':
          data = request.data
       
          serilizers=PostaddressSerializer(data=data)
          
          if serilizers.is_valid():
                 serilizers.save()
                 #deletebutton.objects.create(
                 # user=serilizers['user'])
    
    
    
                 
                 
                 return Response({'serial1':serilizers.data})
          
          return Response(serilizers.errors)

     
@api_view(['POST'])            
def login(request):
     if request.method=='POST':
           data= request.data
           serializerss = loginserializers(data=data)
           if not serializerss.is_valid():
                 
                 return Response({'status':serializerss.errors,'status2':'error in searializer'}) 
           print(serializerss.data)
           print(serializerss.validated_data)
          # user = authenticate(username=User.objects.filter(serializerss.data['username']),password=User.objects.filter(serializerss.data['password']))
           validated_data = serializerss.validated_data
           username = validated_data.get('username')
           password = validated_data.get('password')
           print(username)
           print(password)
           user_exists = User.objects.filter(username=username).exists()
           print(f"User exists: {user_exists}")
           if not user_exists:
                return Response({'status':'no user found'})

           try:
                    user_profile = deletebutton.objects.get(user=User.objects.get(username=username))
                    
                    if user_profile.deleteq:
                         return Response({'status':'deactivate'})
           except deletebutton.DoesNotExist:
                    return Response({'status':'profile not found'})

           user = authenticate(request,username=username, password=password)
           print(user)
           if not user :
                return Response({'status':'user not found'}) 
         
           token, _ = Token.objects.get_or_create(user=user)
           return Response({'status':serializerss.data,'token':str(token)})
           
                
'''         
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])     
@api_view(['GET'])            
def show_data(request):
     #data = userprofilee.objects.filter(user=request.user)
     #print(data)
   #  serializers= PostaddressSerializer(data)
     return Response({'status':'you are in','data':"data"})
'''

class person_data(APIView):
     permission_classes=[IsAuthenticated]
     authentication_classes=[TokenAuthentication]
     def get(self,request):
          data = userprofilee.objects.filter(user=request.user)
          print(data)
          serializers= showserializers(data,many=True)
          print(serializers.data)
          return Response({'status':'you are in','data':serializers.data})
class delete_data(APIView):
     permission_classes=[IsAuthenticated]
     authentication_classes=[TokenAuthentication]
     def get(self,request):
          deel = User.objects.get(username=request.user)
          userdel = deletebutton.objects.get(user=deel)
          userdel.deleteq = True
    
    
     
          userdel.save()
          
          try:
              # Get the user's 
               token = Token.objects.get(user=request.user)
            # Delete the token to log out the use
               token.delete()
               return Response({"message": "Successfully delete out."})
          except Token.DoesNotExist:
               return Response({"error": "Invalid token."})



          print(userdel)
          return Response({'status':'you are delete','data':'serializers'})
     #logout(request)
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        try:
            # Get the user's token
            token = Token.objects.get(user=request.user)
            # Delete the token to log out the user
            token.delete()
            return Response({"message": "Successfully logged out."})
        except Token.DoesNotExist:
            return Response({"error": "Invalid token."})

'''
@api_view(['POST'])
def registrationuser(request):
    if request.method == 'POST':
        data = request.data
        serializer = PostaddressSerializer(data=data)

        if serializer.is_valid():
            user_profiles = serializer.save()

            # Serialize the list of created profiles to return as a response
            response_data = PostaddressSerializer(user_profiles, many=True).data

            return Response({'user_profiles': response_data})

        return Response(serializer.errors)
'''

'''
class person(APIView):
     def get(self,request):
         
            #data = testomodel.objects.all()
            data = testomodel.objects.filter(color__isnull=False)
            #data1=deletebutton.objects.all()
            serilizers=testomodelserial(data,many=True)
            return Response(serilizers.data)
     def post(self,request):
            data = request.data
            serilizers=testomodelserial(data=data)
            if serilizers.is_valid():
                 serilizers.save()
                 return Response(serilizers.data) 
            return Response(serilizers.errors) 
            '''