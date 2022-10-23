import urllib


def bloggers_context_processor(request):
    pagination_prefix = '?'
    query = dict(request.GET)
    query.pop('page', None)
    if query:
        pagination_prefix += f'{urllib.parse.urlencode(query, doseq=True)}&'
    return {'pagination_prefix': pagination_prefix}
