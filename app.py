user_permissions: [int, str] = {
    0: "ADMIN",
    1: "EDITOR",
    2: "USER"
}

ADMIN = ["Read", "Write", "Delete"]
EDITOR = ["Read", "Write"]
USER = ["Read"]


def display_permissions(user_role: str):
    if user_role.upper() == user_permissions.get(0):
        print(f"User roles: {ADMIN}")
    elif user_role.upper() == user_permissions.get(1):
        print(f"User roles: {EDITOR}")
    elif user_role.upper() == user_permissions.get(2):
        print(f"User roles: {USER}")
    else:
        print(f"User roles: {USER}")
