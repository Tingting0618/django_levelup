# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import serializers
# from levelupapi.models import Gamer
# from levelupapi.views.event import EventSerializer

# @api_view(['GET'])
# def get_gamer_profile(request):
#     # import pdb; pdb.set_trace()
#     # return Response()
#     gamer=request.auth.user.gamer
#     return Response(gamer)

# class GamerSerializer(serializers.ModelSerializer):
#     attending = EventSerializer(many=True)
#     class Meta:
#         model = Gamer
#         fields = ('id', 'bio', 'attending')