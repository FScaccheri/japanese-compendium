import json
from django.core.management.base import BaseCommand, CommandError
from jcomp.apps.common.models import Word
from jcomp.apps.verbs.models import Verb
from jcomp.apps.adjectives.models import Adjective
from jcomp.apps.kanji.models import Kanji
from pyexcel_xlsx import get_data


class Command(BaseCommand):
    help = 'Parse an Excel file with format .xlsx to retrieve its data' \
           ' and create the corresponding models'

    def add_arguments(self, parser):
        parser.add_argument('file_name')
        parser.add_argument('rows_offset', nargs='?', default=1, type=int)

    def handle(self, *args, **options):
        offset = options['rows_offset'] - 1

        try:
            file_name = options.get('file_name')
        except Exception:
            raise CommandError('The file name argument is missing.')

        if '.xlsx' not in file_name:
            file_name += '.xlsx'
            self.stdout.write(self.style.WARNING('The entered file name was not the correct format, '
                                                 'but it was correctly parsed.'))

        self.data = get_data(file_name)

        vocabulary_data = self.parse_data_from_excel('vocabulary', 'ごい', offset)
        verbs_data = self.parse_data_from_excel('verbs', 'どうし', offset)
        adjectives_data = self.parse_data_from_excel('adjectives', 'けいようし', offset)
        kanji_data = self.parse_data_from_excel('kanji', 'かんじ', offset)

        verbs_hiragana_list = [verb[1] for verb in verbs_data]
        adjectives_hiragana_list = [adjective[1] for adjective in adjectives_data]
        verbs = [(verb[1], verb[2]) for verb in verbs_data]
        adjectives = [(adjective[1], adjective[2]) for adjective in adjectives_data]

        vocabulary =  vocabulary_data.copy()

        word_counter = 0
        for word in vocabulary_data:
            hiragana = word[0]
            # Maybe refactor this
            translation = word[1]
            created = Word.objects.get_or_create(hiragana=hiragana, translation=translation)[1]
            if created:
                word_counter += 1

        self.stdout.write(self.style.SUCCESS("Successfully created %s words" % word_counter))

        verbs_counter = 0
        for verb in verbs_data:
            hiragana = verb[1]
            defaults = {'group': verb[0], 'translation': verb[2]}
            created = Verb.objects.get_or_create(hiragana=hiragana, defaults=defaults)[1]
            if created:
                verbs_counter += 1

        self.stdout.write(self.style.SUCCESS("Successfully created %s verbs" % verbs_counter))

        adjectives_counter = 0
        for adjective in adjectives_data:
            hiragana = adjective[1]
            defaults = {'group': adjective[0], 'translation': adjective[2]}
            created = Adjective.objects.get_or_create(hiragana=hiragana, defaults=defaults)[1]
            if created:
                adjectives_counter += 1
        
        self.stdout.write(self.style.SUCCESS("Successfully created %s adjectives" % adjectives_counter))

        # TODO: Create Kanji from kanji sheet of excel

    def parse_data_from_excel(self, romaji_key, hiragana_key, offset):
        try:
            return list(filter(None, self.data[romaji_key][offset:]))
        except KeyError:
            return list(filter(None, self.data[hiragana_key][offset:]))
