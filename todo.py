tasks = []
def main():
while True:
	print("\n--- TODO LIST ---")
	print("1. Thêm công việc")
	print("2. Xem danh sách")
	print("3. Đánh dấu hoàn thành")
	print("4. Thoát")
	choice = input("Chọn chức năng: ")
	if choice == '1':
		add_task()
	elif choice == '2':
		view_tasks()
	elif choice == '3':
		mark_task_done()
	elif choice == '4':
		print("Kết thúc chương trình.")
		break

if __name__ == "__main__":
	main()