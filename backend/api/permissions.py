from rest_framework.permissions import BasePermission

class IsSuperUser(BasePermission):
    """
    Permite el acceso solo a superusuarios.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class HasModuleAccess(BasePermission):
    """
    Permite el acceso solo si el usuario tiene asignado el módulo requerido o es superusuario.
    """
    def has_permission(self, request, view):
        # Superusuarios tienen acceso a todo
        if request.user.is_superuser:
            return True
            
        # Obtener el nombre del módulo requerido (puedes definirlo en la vista)
        required_module = getattr(view, 'required_module', None)
        
        if not required_module:
            return False
            
        # Verificar si el usuario tiene el módulo asignado
        return request.user.modulos.filter(codename=required_module, is_active=True).exists()