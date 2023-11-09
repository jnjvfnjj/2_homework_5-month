from rest_framework import serializers
from apps.historytransfer.models import HistoryTransfer

class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('from_user', 'to_user', 'is_complated', 'created_at', 'amount')