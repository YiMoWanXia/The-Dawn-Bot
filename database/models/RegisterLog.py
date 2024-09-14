from datetime import datetime
from tortoise import Model, fields


class RegisterLog(Model):
    email = fields.CharField(max_length=255)
    register_time = fields.DatetimeField(null=True)
    result = fields.IntField(null=False)

    class Meta:
        table = "register_log"

    @classmethod
    async def create_log(
            cls, email: str, register_time: datetime = None, result: bool = False
    ):
        log = await cls.create(email=email, register_time=register_time, result=result)
        log.save()
