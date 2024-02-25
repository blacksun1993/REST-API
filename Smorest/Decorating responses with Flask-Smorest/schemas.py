from marshmallow import Schema, fields

################################
#imput name price store_id are required
#id is generated
################################
class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)    

################################
#No specific import required because this section is for update
################################

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

