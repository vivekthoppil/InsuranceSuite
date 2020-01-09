import json

from rest_framework.renderers import JSONRenderer


class CoreJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    pagination_object_label = 'objects'
    pagination_count_label = 'count'

    def render(self, data, media_type=None, renderer_context=None):
        if data.get('results', None) is not None:
            return json.dumps({
                self.pagination_object_label: data['results'],
                self.pagination_count_label: data['count'],
                'next': data['next'],
                'previous': data['previous']
            })

        elif data.get('errors', None) is not None:
            return super(CoreJSONRenderer, self).render(data)

        else:
            return json.dumps({
                self.object_label: data
            })
