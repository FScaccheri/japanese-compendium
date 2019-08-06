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

        data = get_data(file_name)
        
        # Yikes
        # TODO: Create Words, then replace for Verbs and Adjectives
        try:
            vocabulary_data = list(filter(None, data['vocabulary'][offset:]))
        except KeyError:
            vocabulary_data = list(filter(None, data['ごい'][offset:]))
        
        try:
            verbs_data = list(filter(None, data['verbs'][offset:]))
        except KeyError:
            verbs_data = list(filter(None, data['どうし'][offset:]))

        try:
            adjectives_data = list(filter(None, data['adjectives'][offset:]))
        except KeyError:
            adjectives_data = list(filter(None, data['けいようし'][offset:]))
        
        try:
            kanji_data = list(filter(None, data['kanji'][2:]))
        except KeyError:
            kanji_data = list(filter(None, data['かんじ'][2:]))

        verbs_hiragana_list = [verb[1] for verb in verbs_data]
        adjectives_hiragana_list = [adjective[1] for adjective in adjectives_data]

        word_counter = 0
        for word in vocabulary_data:
            word_hiragana = word[0]
            # Maybe refactor this
            
            translation = word[1]
            type = word[2] if 2 < len(word) else None
            source = word[3] if 3 < len(word) else None
            new_word = Word.objects.filter(
                hiragana=word_hiragana,
                verb__isnull=True,
                adjective__isnull=True
            )
            if not new_word:
                Word.objects.create(hiragana=word[0], translation=translation,
                                    # type=type,
                                    source=source)
                word_counter += 1

        self.stdout.write(self.style.SUCCESS("Successfully created %s words" % word_counter))

        verbs_counter = 0
        for index, verb in enumerate(verbs_data):
            hiragana = verb[1]
            if index == 0: # Verb 'DESU' is an exception and has no group (maybe fill up the cell with a 0 value)
                Verb.objects.get_or_create(hiragana=hiragana, translation=verb[2], group=0)
            else:

                defaults = {'group': verb[0], 'translation': verb[2]}
                
                created = Verb.objects.get_or_create(
                    hiragana=hiragana,
                    defaults=defaults
                )[1]
                if created:
                    verbs_counter += 1

        self.stdout.write(self.style.SUCCESS("Successfully updated %s verbs" % verbs_counter))

        adjectives_counter = 0
        for adjective in adjectives_data:
            hiragana = adjective[1]
            defaults = {'group': adjective[0], 'translation': adjective[2]}
            created = Adjective.objects.get_or_create(
                hiragana=hiragana,
                defaults=defaults
            )[1]
            if created:
                adjectives_counter += 1
        
        self.stdout.write(self.style.SUCCESS("Successfully updated %s adjectives" % adjectives_counter))

        # TODO:
        #  >Create Kanji from kanji sheet of excel
