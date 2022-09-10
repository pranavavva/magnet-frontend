from typing import List
from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import Schema, fields, post_load


class UploadFormat:
    def __init__(
        self,
        material: str = "N87",
        temperature: float = 20.0,
        dc_bias: float = 0.0,
        b_field: List[int] = [0.0, 1.0, 2.0],
        **kwargs,
    ):
        self.material = material
        self.temperature = temperature
        self.dc_bias = dc_bias
        self.b_field = b_field

    def __repr__(self) -> str:
        return f"UploadFormat(material={self.material}, temperature={self.temperature}, dc_bias={self.dc_bias}, b_field={self.b_field})"


class UploadFormatSchema(Schema):
    material = fields.String(required=True)
    temperature = fields.Float(required=True)
    dc_bias = fields.Float(required=True)
    b_field = fields.List(fields.Float, required=True)

    @post_load
    def make_upload_format(self, data, **kwargs):
        return UploadFormat(**data, **kwargs)


blp = Blueprint("upload", __name__, url_prefix="/upload")


@blp.route("/")
class UploadView(MethodView):
    @blp.arguments(UploadFormatSchema, location="json")
    @blp.response(200, UploadFormatSchema)
    def post(self, args: UploadFormat):
        # return {
        #     "message": "Processing data...",
        # }
        return args


if __name__ == "__main__":
    schema = UploadFormatSchema()
    result = schema.load(
        {
            "material": "N87",
            "temperature": 300,
            "dc_bias": 0.5,
            "b_field": [0.0, 1.0, 2.0],
        }
    )
    print(result)
