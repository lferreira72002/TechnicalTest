import json

def sort_by_price_ascending(json_string):
    
    def alpsort(object):
        return object['name']


    
    json_object = json.loads(json_string)
    json_object.sort(key = alpsort)
    sortedoutput = ""
    
    prices = []
    for i in json_object:
        prices.append(i.get('price'))

    prices.sort()

    for i in range(len(prices)):
        for j in range(len(prices)):
            if json_object[j].get('price') == prices[i]:
                sortedoutput = sortedoutput +  '{"name":' + json_object[j].get('name') + ',"price":' + str(json_object[j].get('price')) + '}'
                json_object.pop(j)
                break

    print(sortedoutput)


print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"orange","price":9.99}, {"name":"juice","price":9.99}]'))