from django.shortcuts import HttpResponse
from django.db.models import Q
import json
import logging
logger = logging.getLogger(__name__)
class Datatable(object):
  def __init__(self, model=None, fields=None):
    self.fields = fields
    self.model = model

  def get_response(self, request):
    start = request.GET['start']
    end = request.GET['length']
    draw = request.GET['draw']
    search = request.GET['search[value]']
    search = str(search)
    queries = [Q(**{f + '__contains': search}) for f in self.fields]
    qs = reduce(lambda x, y: x | y, queries)
    order = dict(enumerate(self.fields))
    dirs = {'asc': '', 'desc': '-'}
    ordering = dirs[request.GET['order[0][dir]']] + order[int(request.GET['order[0][column]'])]
    objects = self.model.objects.order_by(ordering)
    total_records = self.model.objects.count()
    logger.error("ksjksjksjskj")
    # objects = objects.filter(qs)[start:(int(start) + int(end))]
    ob = objects.filter(qs)
    objects = ob[start:(int(start) + int(end))]
    filtered = ob.count()
    data = [
      [str(getattr(a, field)) for field in self.fields] for a in objects
    ]
    return HttpResponse(json.dumps({
      "draw": draw,
      "recordsTotal": total_records,
      "recordsFiltered": filtered,
      "data": data,
    }), content_type='application/json')
