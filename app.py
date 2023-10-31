user_roles: [int, str] = {
    0: "ADMIN",
    1: "EDITOR",
    2: "USER"
}

ADMIN = ["Read", "Write", "Delete"]
EDITOR = ["Read", "Write"]
USER = ["Read"]

roles = []


def display_permissions(user_role: str):
    for i in range(0, len(user_roles)):
        roles.append(user_roles.get(i))

    display_roles(user_role, roles)
    # print(f"Available roles: {roles}")


def display_roles(user_role: str, selected_user_roles: [str]):
    for i in range(0, len(selected_user_roles)):
        if user_role == selected_user_roles[i]:
            print(f"{selected_user_roles[i]}")

            print(f"Something{selected_user_roles}")
