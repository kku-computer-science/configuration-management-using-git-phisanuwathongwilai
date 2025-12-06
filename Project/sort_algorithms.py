# ====================================================================
# ส่วนที่ 1: การเรียงลำดับแบบ Quick Sort (นาย ณัฐนันท์ ขำสม)
# ====================================================================

def quick_sort(data_list):
    """
    ฟังก์ชันสำหรับเรียงลำดับรายการตัวเลขโดยใช้วิธี Quick Sort
    เลือก Pivot แล้วแบ่งรายการออกเป็นรายการที่น้อยกว่า มากกว่า เทียบกับ Pivot
    แล้วเรียกซ้ำกับรายการที่แบ่งแล้ว ทำเรื่อยๆ
    """
    
    if len(data_list) <= 1:
        return data_list

    
    # เราเลือก Pivot เป็นตัวที่อยู่ตรงกลางเพื่อความง่าย
    pivot_index = len(data_list) // 2
    pivot_value = data_list[pivot_index]

    #แบ่งรายการออกเป็น 3 กลุ่ม (Partitioning)
    smaller_than_pivot = []  # ตัวเลขที่น้อยกว่า Pivot
    equal_to_pivot = []      # ตัวเลขที่เท่ากับ Pivot
    greater_than_pivot = []  # ตัวเลขที่มากกว่า Pivot

    for number in data_list:
        if number < pivot_value:
            smaller_than_pivot.append(number)
        elif number == pivot_value:
            equal_to_pivot.append(number)
        else:
            greater_than_pivot.append(number)

    # เรียกฟังก์ชัน Quick Sort ซ้ำ (Recursion)
    # รวมผลลัพธ์: เรียงรายการซ้าย + รายการกลาง + เรียงรายการขวา
    return quick_sort(smaller_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

# ====================================================================
# ส่วนที่ 2: ฟังก์ชัน Bubble Sort (ยังขาดอยู่ )
# ====================================================================

def bubble_sort(data_list):
    """
    ฟังก์ชันสำหรับเรียงลำดับรายการตัวเลขโดยใช้วิธี Bubble Sort (ต้อง implement)
    หลักการ: เปรียบเทียบตัวเลขที่อยู่ติดกันแล้วสลับตำแหน่งถ้าตัวหน้ามากกว่าตัวหลัง
    ต้องวนซ้ำหลายรอบจนกว่าจะไม่มีการสลับเกิดขึ้น
    """
    # ** สมาชิก B ต้องใส่โค้ด Bubble Sort ที่นี่ **
    # ตัวอย่างการคืนค่าชั่วคราว:
    # return sorted(data_list) # ไม่ควรใช้จริงในการส่งงาน
    pass # ควรลบ pass เมื่อใส่โค้ดจริง



# ====================================================================
# ส่วนที่ 3: ส่วนควบคุมหลักของโปรแกรม 
# ====================================================================



def main(): # นายณัฐนันท์ ขำสม
    """จัดการกับการรับ Input, การเลือก Algorithm และการแสดงผลลัพธ์"""
    print("--- โปรแกรมเรียงลำดับตัวเลข (Sorting Program) ---")

    # A. รับ Input จากผู้ใช้
    numbers_to_sort = []
    while True:
        try:
            # รับ Input เป็นข้อความ เช่น "10 5 8 2 1"
            input_string = input("กรุณาใส่ตัวเลขที่ต้องการเรียงลำดับ (คั่นด้วยช่องว่าง): ")
            # แปลงข้อความเป็น list ของ Integer
            numbers_to_sort = [int(num_str.strip()) for num_str in input_string.split()]

            if not numbers_to_sort:
                # ตรวจสอบว่ามีตัวเลขถูกป้อนหรือไม่
                print("กรุณาป้อนตัวเลขอย่างน้อยหนึ่งตัว")
                continue
            break
        except ValueError:
            print(" Input ไม่ถูกต้อง กรุณาใส่เฉพาะตัวเลขคั่นด้วยช่องว่างเท่านั้น")

    # B. รับตัวเลือก Algorithm
    selected_algorithm = None
    sorted_result = []

    while True:
        choice_input = input("โปรดเลือก Algorithm (quick sort (q) / bubble sort (q) ): ").lower().strip()

        data_copy = numbers_to_sort.copy()

        if choice_input in ["quick sort", "quicksort", "q"]:
            selected_algorithm = "Quick Sort"
            sorted_result = quick_sort(data_copy)
            break
        elif choice_input in ["bubble sort", "bubblesort", "b"]:
            selected_algorithm = "Bubble Sort"
            sorted_result = bubble_sort(data_copy)
            break
        else:
            print(" ตัวเลือกไม่ถูกต้อง! กรุณาเลือก 'quick sort' หรือ 'bubble sort'")

    # C. แสดงผลลัพธ์
    print("\n--- ผลลัพธ์ ---")
    print(f"Algorithm ที่เลือก: **{selected_algorithm}**")
    print(f"รายการเริ่มต้น: {numbers_to_sort}")
    print(f"รายการที่เรียงแล้ว: {sorted_result}")

if __name__ == "__main__":
    main()