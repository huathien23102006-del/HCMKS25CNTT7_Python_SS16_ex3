"""
    1. Phân tích và thiết kế giải pháp
    Hàm validate_gender(gender_input)

    Input:

    gender_input (str)

    Xử lý:

    .strip() loại bỏ khoảng trắng thừa.
    .lower() chuyển về chữ thường.
    Kiểm tra có phải "nam" hoặc "nu" hay không.

    Output:

    True nếu hợp lệ.
    False nếu không hợp lệ.
    validate_gender(" nam ") -> True
    validate_gender("Nu") -> True
    validate_gender("Không rõ") -> False
    Hàm find_patient_index(patient_list, patient_id)

    Input:

    patient_list (list)
    patient_id (str)

    Xử lý:

    Chuẩn hóa mã BN bằng .strip().upper()
    Duyệt danh sách tìm mã.

    Output:

    Trả về index nếu tìm thấy.
    Trả về -1 nếu không tìm thấy.
    find_patient_index(patients, "bn001")
    # return 0
    Hàm display_patients(patient_list)

    Input:

    patient_list (list)

    Output:

    Không return.
    In danh sách bệnh nhân.
    Hàm add_patient(patient_list)

    Input:

    patient_list (list)

    Output:

    Không return.
    Thêm bệnh nhân mới bằng .append().
    Hàm update_diagnosis(patient_list)

    Input:

    patient_list (list)

    Output:

    Không return.
    Cập nhật chẩn đoán bệnh.
    Hàm search_by_disease(patient_list)

    Input:

    patient_list (list)

    Output:

    Không return.
    Hiển thị danh sách bệnh nhân phù hợp.
    String và List tương tác như thế nào?

    Trong bài này:

    String dùng để lưu:
    Mã bệnh nhân
    Tên bệnh nhân
    Giới tính
    Chẩn đoán bệnh

    Các hàm:

    strip()
    upper()
    title()
    capitalize()
    lower()

    được dùng để chuẩn hóa dữ liệu trước khi lưu vào List.

    Ví dụ:

    name = "   le van cuong   "
    name = name.strip().title()

    Kết quả:

    Le Van Cuong
    Truyền List vào hàm là Reference hay Value?

    Python truyền tham chiếu đối tượng (reference).

    Ví dụ:

    def add_item(data):
        data.append("ABC")


    my_list = []
    add_item(my_list)

    print(my_list)

    Kết quả:

    ['ABC']

    Do đó khi truyền:

    add_patient(patients)

    thì hàm có thể thay đổi trực tiếp danh sách patients bên ngoài.
"""

patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


def validate_gender(gender_input):
    """
    Kiểm tra giới tính hợp lệ.
    """
    gender_input = gender_input.strip().lower()
    return gender_input in ["nam", "nu"]


def find_patient_index(patient_list, patient_id):
    """
    Tìm vị trí bệnh nhân theo mã.
    """
    patient_id = patient_id.strip().upper()

    for index, patient in enumerate(patient_list):
        if patient[0] == patient_id:
            return index

    return -1


def display_patients(patient_list):
    """
    Hiển thị danh sách bệnh nhân.
    """
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return

    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")

    for index, patient in enumerate(patient_list, start=1):
        print(
            f"{index}. Mã: {patient[0]} | "
            f"Tên: {patient[1]} | "
            f"Giới tính: {patient[2]} | "
            f"Bệnh: {patient[3]}"
        )


def add_patient(patient_list):
    """
    Tiếp nhận bệnh nhân mới.
    """
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip().title()

    if len(patient_name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        gender = input("Nhập giới tính Nam/Nu: ")

        if validate_gender(gender):
            gender = gender.strip().capitalize()
            break

        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    new_patient = [
        patient_id,
        patient_name,
        gender,
        diagnosis
    ]

    patient_list.append(new_patient)

    print("\nTiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    """
    Cập nhật chẩn đoán bệnh.
    """
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input(
        "Nhập mã bệnh nhân cần cập nhật: "
    ).strip().upper()

    if len(patient_id) == 0:
        print("Mã bệnh nhân không được để trống!")
        return

    patient_index = find_patient_index(
        patient_list,
        patient_id
    )

    if patient_index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return

    patient = patient_list[patient_index]

    print(f"Tìm thấy bệnh nhân: {patient[1]}")
    print(f"Chẩn đoán hiện tại: {patient[3]}")

    new_diagnosis = input(
        "Nhập chẩn đoán mới: "
    ).strip().capitalize()

    if len(new_diagnosis) == 0:
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[patient_index][3] = new_diagnosis

    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    """
    Tìm kiếm bệnh nhân theo tên bệnh.
    """
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input(
        "Nhập từ khóa tên bệnh: "
    ).strip()

    if len(keyword) == 0:
        print("Từ khóa tìm kiếm không được để trống!")
        return

    count = 0

    print("Kết quả tìm kiếm:")

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1

            print(
                f"{count}. Mã: {patient[0]} | "
                f"Tên: {patient[1]} | "
                f"Giới tính: {patient[2]} | "
                f"Bệnh: {patient[3]}"
            )

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(
        f"\nCó tổng cộng {count} bệnh nhân mắc bệnh "
        f"liên quan đến '{keyword}'."
    )


def main():
    """
    Hàm điều khiển chương trình.
    """
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")

        choice = input(
            "Nhập lựa chọn của bạn: "
        ).strip()

        if not choice.isdigit():
            print(
                "Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!"
            )
            continue

        choice = int(choice)

        match choice:
            case 1:
                display_patients(patients)

            case 2:
                add_patient(patients)

            case 3:
                update_diagnosis(patients)

            case 4:
                search_by_disease(patients)

            case 5:
                print(
                    "Cảm ơn bác sĩ đã sử dụng hệ thống!"
                )
                break

            case _:
                print(
                    "Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!"
                )


main()