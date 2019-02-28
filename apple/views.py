from rest_framework.decorators import (
    api_view,
    permission_classes,
    renderer_classes
)
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import (AllowAny, )
from rest_framework.response import Response


@api_view(["GET"])
@renderer_classes([JSONRenderer])
@permission_classes((AllowAny,))
def test(request):
    return Response(data={"foo": "bar"})
