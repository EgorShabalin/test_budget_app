from utils import read_file, get_data
from db import get_all_objects
from model import Budget_item


def find(request):
    result = set()
    request = str(request)
    objects = get_all_objects()
    for obj in objects:
        if obj.id.find(request):
            result.add(obj)
        if obj.date.find(request):
            result.add(obj)
        if obj.cat.find(request):
            result.add(obj)
        if obj.amount.find(request):
            result.add(obj)
        if obj.desc.find(request):
            result.add(obj)
    return result


find("у")
