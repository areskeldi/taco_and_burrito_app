from kivymd.uix.dialog import ListMDDialog

class TacoMenu(ListMDDialog):
    def __init__(self, taco_data):
        super().__init__()

        headers = 'address,categories,city,country,cuisines,keys,latitude,longitude,menupageurl,menuamountmax,menuamountmin,menucategory,menucurrency,menudateseen,menudescription,menuName,name,postalCode,province,websites'
        headers=headers.split(',')
        print(taco_data)

        for i in range(len(headers)):
            attribute_name=headers[i]
            attribute_value=taco_data[i]
            setattr(self,str(attribute_name),str(attribute_value))

