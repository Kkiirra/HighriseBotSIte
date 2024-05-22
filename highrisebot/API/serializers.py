from rest_framework import serializers
from .models import BotModerator, HighrisePlayers


class BotModeratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotModerator
        fields = '__all__'

    def update(self, instance, validated_data):
        ignorewords = validated_data.get('ignorewords', None)
        filter_words = validated_data.get('filter_words', None)

        if ignorewords:
            instance.ignorewords += " " + ignorewords

        if filter_words:
            instance.filter_words += " " + filter_words

        for field, value in validated_data.items():
            if field != 'filter_words' and field != 'ignorewords':
                setattr(instance, field, value)

        instance.save()
        return instance

    def remove_word(self, instance, word, field_name):
        if field_name not in ['ignorewords', 'filter_words']:
            raise ValueError("Некорректное имя поля. Используйте 'ignorewords' или 'filter_words'.")

        current_words = getattr(instance, field_name)
        if current_words:
            words_list = current_words.split()
            filtered_words = ' '.join(filter(lambda w: w != word, words_list))
            setattr(instance, field_name, filtered_words)
            instance.save()


class HighrisePlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighrisePlayers
        fields = '__all__'
