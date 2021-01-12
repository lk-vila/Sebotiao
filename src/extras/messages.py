'''

Creates the formated messages to be sent on to the discord.

'''

# from discord import Embed
# from extras.constants import Colours


class MessageFormater:
    '''
    Formats messages before sending (e.g. Embeds, links, tags etc).
    '''

    @staticmethod
    def ajuda():
        '''
        Custom made help command.
        '''

        message = '''
        Meu prefixo de comandos é: `tiao ` (perceba o espaço depois de "tiao")\n
        > `ajuda` : recursivo.\n
        > `set_def_role ROLE` : configura o role/cargo default que o automod colocará nos novos membros\n
        > `set_no_role_as_default`: coloca todas as pessoas sem role como o role default\n
        > `set_cursed_words PALAVRA_1,PALAVRA_2,...` : adiciona palavra(s) à lista de palavras indesejadas\n
        > `list_cursed_words` : lista as palavras banidas\n
        > `uncurse_words PALAVRA_1,PALAVRA_2,...`: remove palavras da lista\n
        '''

        return message

    @staticmethod
    def cursed_words_msg(user_id):
        '''
        The reply when someone says a cursed word.
        '''
        return f'Aqui nois nao usa esses termo nao blz.Fas o favor <@{user_id}> obrigado .'

    # @staticmethod
    # def stream_notification(user_id, twitch_url):
    #     message = Embed(
    #         title='Ta na hora de ver uma live braba!',
    #         url=twitch_url,
    #         color=Colours.bright_green
    #     )
    #
    #     # message.add_field('')
    #
    #     message.set_footer('Venha para o pântano!')
