def command_help(role):
    match role:
        case "bandung_bondowoso":
            print("bagian bandung bondowoso")
        case "roro_jonggrang":
            print("bagian roro")
        case "jin_pembangun":
            print("bagian jin pembangun")
        case "jin_pengumpul":
            print("bagian jin pengumpul")
        case _:
            print("login untuk masuk")
            print("load untuk membaca data")
            print("exit")
