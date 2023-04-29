import main_data


def logout():
    # meriset current user dan role lalu merupab is login menjadi false
    main_data.current_role = ""
    main_data.current_user = ""
    main_data.is_login = False
