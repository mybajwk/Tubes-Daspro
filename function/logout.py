import main_data


def logout():
    main_data.current_role = ""
    main_data.current_user = ""
    main_data.is_login = False
