from Employee.viewsets import Employeeviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('employee', Employeeviewset)

