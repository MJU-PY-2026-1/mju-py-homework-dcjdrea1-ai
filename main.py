# 파일이름 :
# 작 성 자 :
print("="*40)
print("     ☕ CAMPUS CAFE RECIPE v1.0     ")
print("="*40)

# 2. 입출력 및 형변환 (병합하여 효율화)
menu_name = input("▶ 음료 이름: ")
base_name = input("▶ 베이스 종류 (우유/물/콜드브루): ")

# 용량과 샷 수는 바로 숫자로 변환
base_ml = float(input("▶ 베이스 용량 (ml): "))
shot_count = int(input("▶ 에스프레소 샷 수 (개): "))
syrup_pump = int(input("▶ 시럽 펌프 횟수 (회): "))

# 3. 산술 연산 (디테일 추가)
shot_ml = shot_count * 35      # 1샷당 35ml
syrup_ml = syrup_pump * 10     # 1펌프당 10ml
total_volume = base_ml + shot_ml + syrup_ml

# 4. 출력 포맷팅 (f-string의 정렬 기능 활용)
print("\n" + "-"*15, "레시피 결과", "-"*15)
print(f"[{menu_name}] 상세 구성")
print(f"• 베이스: {base_name} ({base_ml}ml)")
print(f"• 추가액: 샷 {shot_ml}ml + 시럽 {syrup_ml}ml")
print(f"• 총 용량: {total_volume}ml")

# 산술 연산 응용: 100ml당 카페인 함량 (1샷당 75mg 가정)
total_caffeine = shot_count * 75
print(f"⚠️ 예상 카페인 함량: {total_caffeine}mg")
print("-" * 40)