from rest_framework import serializers

from stats.models import (AidContactClickEvent,
                          AidMatchProjectEvent, AidEligibilityTestEvent,
                          PromotionDisplayEvent, PromotionClickEvent)


class AidContactClickEventSerializer(serializers.ModelSerializer):
    querystring = serializers.CharField(allow_blank=True)

    class Meta:
        model = AidContactClickEvent
        fields = '__all__'


class AidMatchProjectEventSerializer(serializers.ModelSerializer):
    querystring = serializers.CharField(allow_blank=True)

    class Meta:
        model = AidMatchProjectEvent
        fields = '__all__'


class AidEligibilityTestEventSerializer(serializers.ModelSerializer):
    querystring = serializers.CharField(allow_blank=True)

    class Meta:
        model = AidEligibilityTestEvent
        fields = '__all__'


class PromotionDisplayEventSerializer(serializers.ModelSerializer):
    querystring = serializers.CharField(allow_blank=True)  # required=False

    class Meta:
        model = PromotionDisplayEvent
        fields = '__all__'


class PromotionClickEventSerializer(serializers.ModelSerializer):
    querystring = serializers.CharField(allow_blank=True)  # required=False

    class Meta:
        model = PromotionClickEvent
        fields = '__all__'
