def enter_club(name: str , age: int , has_id) -> None:
    if name.lower() == "sam":
        print("No Entry")
        return
    if age >= 21 and has_id:
        print("Allow Entry")
    else: 
        print("Not Allow")


def main() -> None: 
    enter_club("Sam",25, has_id = True)
    enter_club("Ram",29, has_id = True)
    enter_club("mhn",27, has_id = True)

if __name__ == '__main__':
    main()
