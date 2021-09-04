all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 해시테이블은 시간을 극대화 하지만 공간을 대신 사용하는 자료구조
def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array: # O(N)
        student_dict[key] = True

    for key in present_array:# O(N)
        del student_dict[key]

    for key in student_dict.keys():
        return key

   #비효율적
    # for i in all_array:
    #     if i not in present_array:
    #         return i


print(get_absent_student(all_students, present_students))