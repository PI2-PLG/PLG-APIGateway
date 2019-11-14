from endpoints.models import Endpoint

'''

No lugar de "localhost" você deve colocar o ip local da sua máquina :)

'''
localhost = "[ADD IP LOCAL AQUI]"
endpoint_data = [
                 ["GetAllModuleData","BI","http://"+localhost+"/all-module-data/"],
                 ["GetAllModuleList","BI","http://"+localhost+"/all-modules-list/"],
                 ["GetAllData","BI","http://"+localhost+"/all-data/"],
                 ["NewModule","BI","http://"+localhost+"/new-module/"]
                ]

print("Adicionando endpoints... ", end="")
for data in endpoint_data:
    endpoint, created = Endpoint.objects.get_or_create(name=data[0], service=data[1], url=data[2])
    if created:
        print(endpoint.name)
    else:
        endpoint.save()
print("Ok!")