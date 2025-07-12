# Decorador que comprueba si un empleado tiene un rol específico
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            # Si el rol de lempleado coincide con el rol requerido
            if employee.get("role") == required_role:
                return func(employee)
            else:
                print(
                    f"ACCESO DENEGAGO. Solo {required_role} pueden realizar esta acción"
                )

        return wrapper

    return decorator


def log_action(func):
    def wrapper(employee):
        print(f"Registrando acción para el empleado {employee['name']}")
        return func(employee)

    return wrapper


@check_access("user")
@log_action
def delete_employee(employee):
    print(f"El empleado {employee['name']}, ha sido eliminado")


employee1 = {"name": "Carlos", "role": "admin"}
employee2 = {"name": "Ana", "role": "user"}

print("Intentando eliminar empleado 1:")
delete_employee(employee1)

print("\nIntentando eliminar empleado 2:")
delete_employee(employee2)
