from amazonproduct import API
api = API(access_key_id='AKIAJXG6BBQM6YDLYEKA',
          secret_access_key='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',
          associate_tag='zhicheng-20',
          locale='us')

for book in api.item_search('Books', Publisher='Galileo Press'):
    print '%s: "%s"' % (book.ItemAttributes.Author,
                        book.ItemAttributes.Title)
