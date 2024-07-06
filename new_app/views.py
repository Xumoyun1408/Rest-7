from rest_framework.viewsets import ModelViewSet
from .models import Category, TravelPackage, Header, Navbar
from .serializers import CategorySerializer, TravelPackageSerializer, HeaderSerializer, NavbarSerializer
from .permissions import CustomPermissions

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CustomPermissions]

class TravelPackageView(ModelViewSet):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer
    permission_classes = [CustomPermissions]

class HeadersView(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = [CustomPermissions]

class NavbarView(ModelViewSet):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer
    permission_classes = [CustomPermissions]
