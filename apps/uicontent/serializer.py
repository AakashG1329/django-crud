from rest_framework import serializers

from apps.uicontent.models import Uicontent

class UicontentSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source='User.name', read_only=True)

    class Meta:
        model = Uicontent
        fields = "__all__"