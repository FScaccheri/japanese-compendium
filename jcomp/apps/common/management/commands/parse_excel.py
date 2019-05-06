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

    def handle(self, *args, **options):
        try:
            file_name = options.get('file_name')
        except Exception:
            raise CommandError('The file name argument is missing.')

        if '.xlsx' not in file_name:
            file_name += '.xlsx'
            self.stdout.write(self.style.WARNING('The entered file name was not the correct format, '
                                                 'but it was correctly added.'))

        data = get_data(file_name)
        vocabulary_data = data['vocabulary']
        verbs_data = data['verbs']
        adjectives_data = data['adjectives']
        kanji_data = data['kanji']

        word_counter = 0
        for word in vocabulary_data:
            new_word = Word(
                hiragana=word[0],
                translation=word[1]
            )
            type = word[2] if 2 < len(word) else None
            new_word.source = word[3] if 3 < len(word) else None
            new_word.save()

        self.stdout.write(self.style.SUCCESS("Successfully created '%s' words" % word_counter))

        # TODO: >create Words ONLY from words sheet of excel.
        #  >Complete remaining Verb and Adjective fields from other sheets.
        #  >Search for existing word, replace it with new Verb/Adjective object
        #  and delete the old one
        #  >Create Kanji from kanji sheet of excel

