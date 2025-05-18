# Do_An_Ca_Nhan_AI

# Báo cáo Đồ án Cá nhân Trí tuệ Nhân tạo

## Đề tài: Giải bài toán 8-Puzzle bằng các thuật toán tìm kiếm

Giảng viên hướng dẫn: Phan Thị Huyền Trang

Sinh viên thực hiện: Nguyễn Phạm Bảo Trân - 23110348

Ngày báo cáo: Tháng 05 năm 2025

## 1. Mục tiêu
Mục tiêu của dự án này là xây dựng một ứng dụng mô phỏng việc giải trò chơi 8-Puzzle (hay Fifteen Puzzle trên bảng 3x3) bằng cách áp dụng và so sánh hiệu quả của các thuật toán tìm kiếm khác nhau trong Trí tuệ Nhân tạo. Ứng dụng cung cấp giao diện trực quan để người dùng nhập trạng thái ban đầu và trạng thái đích, chọn thuật toán, xem quá trình giải từng bước và so sánh hiệu suất giữa các thuật toán.

## 2. Nội dung
### 2.1. Các thuật toán Tìm kiếm không có thông tin (Uninformed Search)
**Khái niệm bài toán tìm kiếm và lời giải:**
Trong bối cảnh trò chơi 8-Puzzle, bài toán tìm kiếm được định nghĩa như sau:

Trạng thái (State): Một cấu hình cụ thể của bảng 3x3, biểu diễn vị trí của 8 ô số và ô trống (ký hiệu là 0). Ví dụ: ((1,2,3),(4,0,5),(6,7,8)).

Hành động (Action): Các di chuyển hợp lệ của ô trống: Lên (Up), Xuống (Down), Trái (Left), Phải (Right).

Môi trường (Environment): Tập hợp tất cả các trạng thái có thể đạt được từ trạng thái ban đầu bằng cách áp dụng các hành động hợp lệ.

Trạng thái ban đầu (Initial State): Cấu hình bắt đầu của bảng 8-Puzzle do người dùng nhập hoặc được tạo ngẫu nhiên.

Trạng thái đích (Goal State): Cấu hình mong muốn của bảng 8-Puzzle (thường là các số được sắp xếp theo thứ tự).

Chi phí bước đi (Step Cost): Chi phí để thực hiện một hành động (thường là 1 cho mỗi bước di chuyển).

Lời giải (Solution): Một chuỗi các hành động (di chuyển) từ trạng thái ban đầu dẫn đến trạng thái đích. Lời giải tối ưu là lời giải có tổng chi phí bước đi thấp nhất (trong 8-Puzzle, đây là chuỗi di chuyển ngắn nhất).

**Các thuật toán Tìm kiếm không có thông tin đã triển khai:**

Nhóm thuật toán này tìm kiếm lời giải mà không sử dụng bất kỳ thông tin bổ sung nào về "độ gần" của một trạng thái với trạng thái đích. Chúng khám phá không gian trạng thái một cách "mù quáng", chỉ dựa vào cấu trúc của không gian tìm kiếm. Các thuật toán được triển khai bao gồm:

BFS (Breadth-First Search): Tìm kiếm theo chiều rộng.

DFS (Depth-First Search): Tìm kiếm theo chiều sâu.

UCS (Uniform-Cost Search): Tìm kiếm chi phí đồng nhất.

IDDFS (Iterative Deepening Depth-First Search): Tìm kiếm theo chiều sâu lặp.

**Hình ảnh minh họa**
GIF minh họa quá trình chạy của từng thuật toán: 

 **Hình minh họa của BFS:**
 
![BFS](https://github.com/user-attachments/assets/b7e9f5b0-99f8-453d-aabb-d7b4e424a1f4)

**Hình minh họa của DFS:**

![DFS](https://github.com/user-attachments/assets/fb45dcbd-ae5c-4b2f-afc2-c7970e912370)

**Hình minh họa của UCS:**

![UCS](https://github.com/user-attachments/assets/7f2e6ca4-dd13-40b4-9027-e0e86080cb0a)

**Hình minh họa của IDDFS:**

![IDDFS](https://github.com/user-attachments/assets/488a24ea-03ae-4d07-8e96-8017542e7801)

Biểu đồ so sánh hiệu suất: 

![Screenshot 2025-05-18 125126](https://github.com/user-attachments/assets/a106874a-1b34-4ce2-b3dc-76b77961e6c5)

**Ưu điểm, Nhược điểm và Hiệu suất**

Tổng quan về hiệu suất trên trò chơi 8 ô chữ: Trên bài toán 8-Puzzle, không gian trạng thái là hữu hạn. BFS và UCS (với chi phí bước đi = 1) sẽ tìm thấy lời giải tối ưu nhưng có thể tốn rất nhiều bộ nhớ cho các trạng thái khó. DFS có thể nhanh hơn về thời gian và tiết kiệm bộ nhớ hơn nhưng không đảm bảo tối ưu. IDDFS thường là lựa chọn cân bằng tốt nhất trong nhóm này về cả thời gian và bộ nhớ.

BFS (Breadth-First Search):
BFS khám phá không gian tìm kiếm theo từng lớp, mở rộng tất cả các node ở độ sâu k trước khi chuyển sang độ sâu k+1.

Ưu điểm:

Đảm bảo tính đầy đủ (completeness) - luôn tìm thấy lời giải nếu có.

Đảm bảo tính tối ưu (optimality) - tìm thấy lời giải ngắn nhất/chi phí thấp nhất khi chi phí bước đi là như nhau (như trong 8-Puzzle).

Nhược điểm:

Yêu cầu lượng bộ nhớ rất lớn để lưu trữ hàng đợi và các trạng thái đã thăm, trong đó b là hệ số phân nhánh và d là độ sâu của lời giải.

Có thể tốn kém về thời gian nếu lời giải nằm ở độ sâu lớn.


DFS (Depth-First Search):
DFS khám phá không gian tìm kiếm theo chiều sâu nhất có thể trước khi quay lui.

Ưu điểm:

Yêu cầu bộ nhớ ít hơn đáng kể so với BFS (O(bm)).

Có thể tìm thấy lời giải nhanh chóng nếu lời giải nằm ở độ sâu nông.

Nhược điểm:

Không đảm bảo tính đầy đủ (có thể đi vào nhánh vô hạn nếu không có kiểm soát trạng thái đã thăm hoặc giới hạn độ sâu).

Không đảm bảo tính tối ưu (có thể tìm thấy lời giải dài hơn trước).


UCS (Uniform-Cost Search):
UCS mở rộng node dựa trên tổng chi phí từ trạng thái ban đầu đến trạng thái hiện tại. Nó sử dụng hàng đợi ưu tiên để luôn mở rộng node có chi phí đường đi thấp nhất.

Ưu điểm:

Đảm bảo tính đầy đủ và tính tối ưu (tìm thấy lời giải có chi phí thấp nhất).

Nhược điểm:

Có thể tốn kém về thời gian và bộ nhớ, đặc biệt nếu chi phí bước đi nhỏ, dẫn đến việc mở rộng nhiều node có chi phí thấp.

Trên 8-Puzzle với chi phí mỗi bước là 1, hiệu suất và kết quả tương tự BFS.


IDDFS (Iterative Deepening Depth-First Search):
IDDFS thực hiện chuỗi các lần tìm kiếm theo chiều sâu với giới hạn độ sâu tăng dần (1, 2, 3, ...).

Ưu điểm:

Kết hợp tính đầy đủ và tối ưu của BFS với hiệu quả bộ nhớ của DFS (O(bd)).

Thường là lựa chọn tốt cho tìm kiếm không có thông tin khi độ sâu lời giải không biết trước.

Nhược điểm:

Lặp lại việc mở rộng các node ở các độ sâu nông nhiều lần, có thể tốn kém thời gian hơn BFS một chút (nhưng thường không đáng kể trong thực tế so với lợi ích về bộ nhớ).


### 2.2. Các thuật toán Tìm kiếm có thông tin (Informed Search)
**Khái niệm bài toán tìm kiếm và lời giải:**
Tương tự như tìm kiếm không có thông tin, nhưng nhóm thuật toán này sử dụng thêm hàm heuristic để ước lượng "độ gần" của một trạng thái với trạng thái đích. Hàm heuristic giúp hướng dẫn quá trình tìm kiếm hiệu quả hơn. Trong dự án này, hàm heuristic Manhattan Distance (tổng khoảng cách Manhattan của mỗi ô số đến vị trí đích của nó) thường được sử dụng.

**Các thuật toán Tìm kiếm có thông tin đã triển khai:**

Greedy Best-First Search: Mở rộng node dựa trên giá trị heuristic thấp nhất.

A* Search: Mở rộng node dựa trên tổng chi phí từ trạng thái ban đầu đến trạng thái hiện tại (g) cộng với ước lượng chi phí từ trạng thái hiện tại đến đích (h), tức là f=g+h.

IDA* Search (Iterative Deepening A* Search): Kết hợp A* Search với tìm kiếm theo chiều sâu lặp.

**Hình ảnh minh họa**

GIF minh họa quá trình chạy của từng thuật toán: 

**Hình ảnh minh họa A_star:**

![A](https://github.com/user-attachments/assets/31b2ebfd-cadf-49ed-b54b-b1998c29dee2)

**Hình ảnh minh họa Greedy:**

![greedy](https://github.com/user-attachments/assets/acc1ee7e-3344-41e2-b113-ccbde7922c14)

**Hình ảnh minh họa IDA_star:**

![IDA](https://github.com/user-attachments/assets/c4a09a18-a6d9-4b97-a746-ae1e1e15242f)

Biểu đồ so sánh hiệu suất:

![Screenshot 2025-05-18 123150](https://github.com/user-attachments/assets/e2f6761c-f4c8-49a3-b4ac-5e330a1da284)

**Ưu điểm, Nhược điểm và Hiệu suất**

Tổng quan về hiệu suất trên trò chơi 8 ô chữ: Các thuật toán tìm kiếm có thông tin thường hiệu quả hơn các thuật toán không có thông tin trên bài toán 8-Puzzle vì chúng sử dụng heuristic để định hướng tìm kiếm. Với heuristic Manhattan Distance (là heuristic chấp nhận được và nhất quán), A* Search và IDA* Search là các thuật toán tìm kiếm có thông tin hiệu quả và đảm bảo tối ưu cho 8-Puzzle. Greedy Search có thể nhanh nhưng không chắc chắn tìm được lời giải tốt nhất. A* có thể tốn bộ nhớ cho các trạng thái khó, trong khi IDA* cân bằng tốt hơn giữa thời gian và bộ nhớ.

Greedy Best-First Search:
Thuật toán này luôn mở rộng node có giá trị heuristic (h) thấp nhất, tức là node được ước lượng là gần đích nhất.

Ưu điểm:

Thường tìm thấy lời giải rất nhanh chóng trong thực tế nếu heuristic tốt.

Hiệu quả bộ nhớ tốt hơn A* trong một số trường hợp.

Nhược điểm:

Không đảm bảo tính đầy đủ cũng như tính tối ưu.

Có thể bị mắc kẹt trong các "ngõ cụt" hoặc đi theo đường rất dài.


A* Search:
A* mở rộng node dựa trên hàm đánh giá f(n)=g(n)+h(n), trong đó g(n) là chi phí thực tế từ trạng thái ban đầu đến n, và h(n) là ước lượng chi phí từ n đến đích.

Ưu điểm:

Đảm bảo tính đầy đủ và tính tối ưu nếu hàm heuristic là nhất quán (consistent) hoặc chấp nhận được (admissible).

Rất hiệu quả trong thực tế với heuristic tốt.

Nhược điểm:

Yêu cầu bộ nhớ lớn để lưu trữ frontier (priority queue) và các trạng thái đã thăm, tương tự BFS trong trường hợp xấu nhất.


IDA* Search (Iterative Deepening A* Search):
IDA* thực hiện chuỗi các lần tìm kiếm theo chiều sâu với giới hạn chi phí f tăng dần. Giới hạn ban đầu là f(start), và ở mỗi lần lặp, giới hạn mới là giá trị f nhỏ nhất vượt quá giới hạn hiện tại.

Ưu điểm:

Đảm bảo tính đầy đủ và tối ưu (với heuristic phù hợp).

Hiệu quả bộ nhớ tốt (O(bd)).

Thường là lựa chọn tốt khi không gian trạng thái lớn và bộ nhớ hạn chế.

Nhược điểm:

Lặp lại việc mở rộng node như IDDFS, có thể tốn thời gian hơn A* một chút.


### 2.3. Các thuật toán Tìm kiếm cục bộ (Local Search)
**Khái niệm bài toán tìm kiếm và lời giải:**
Tìm kiếm cục bộ hoạt động trên một "không gian trạng thái" duy nhất, di chuyển từ trạng thái hiện tại sang một trạng thái lân cận tốt hơn theo một tiêu chí nào đó (thường là giảm giá trị hàm mục tiêu hoặc hàm heuristic). Mục tiêu là tìm kiếm một trạng thái tối ưu (thường là tối ưu cục bộ hoặc toàn cục). Lời giải ở đây là trạng thái đích được tìm thấy, không phải là đường đi.

**Các thuật toán Tìm kiếm cục bộ đã triển khai**

Simple Hill Climbing: Di chuyển đến trạng thái lân cận đầu tiên tốt hơn trạng thái hiện tại.

Steepest Ascent Hill Climbing: Di chuyển đến trạng thái lân cận tốt nhất trong tất cả các trạng thái lân cận.

Stochastic Hill Climbing: Chọn ngẫu nhiên một trạng thái lân cận tốt hơn.

Simulated Annealing: Sử dụng nhiệt độ để cho phép di chuyển đến trạng thái xấu hơn với xác suất giảm dần, giúp thoát khỏi tối ưu cục bộ.

Beam Search: Duy trì một tập hợp các trạng thái tốt nhất (beam) và mở rộng chúng ở mỗi bước.

Genetic Algorithm: Sử dụng các nguyên tắc tiến hóa (chọn lọc, lai ghép, đột biến) để tìm kiếm lời giải.

**Hình ảnh minh họa**

GIF minh họa quá trình chạy của từng thuật toán: 

**Hình ảnh minh họa Simple Hill Climbing:**

![Simple_HC](https://github.com/user-attachments/assets/adfba975-c993-42e1-992d-e7dfd7858d60)

**Hình ảnh minh họa Steepest Ascent Hill Climbing:**

![SA_HC](https://github.com/user-attachments/assets/bab3c2d7-7d16-4124-9b09-c3fc760bb198)

**Hình ảnh minh họa Stochastic Hill Climbing:**

![Stochastic_HC](https://github.com/user-attachments/assets/16656472-32a5-4c4c-8e4c-6f8b9609ccdc)

**Hình ảnh minh họa Simulated Annealing:**

![Screenshot 2025-05-18 124926](https://github.com/user-attachments/assets/19fcf05b-ee2d-4c50-8d96-3bfd671d609e)

**Hình ảnh minh họa Beam Search:**

![Beam](https://github.com/user-attachments/assets/2afc4afa-b56b-40d2-abd6-1b12ea12d071)

**Hình ảnh minh họa Genetic Algorithm:**

![Screenshot 2025-05-18 125014](https://github.com/user-attachments/assets/20211b2b-ccf7-4561-8422-22d3193ec126)

Biểu đồ so sánh hiệu suất: 

![Screenshot 2025-05-18 125026](https://github.com/user-attachments/assets/11d65dc7-68d5-42f7-bc50-27d8625e96a0)

**Ưu điểm, Nhược điểm và Hiệu suất**

Tổng quan về hiệu suất trên trò chơi 8 ô chữ: Đối với bài toán tìm đường đi trong 8-Puzzle, các thuật toán Hill Climbing và Simulated Annealing (khi được sử dụng để tìm trạng thái đích) có thể không hiệu quả bằng các thuật toán tìm kiếm truyền thống vì chúng không lưu lại đường đi. Beam Search và Genetic Algorithm (khi được điều chỉnh để tìm đường đi) có thể hoạt động, nhưng A* hoặc IDA* thường là lựa chọn tốt hơn cho việc tìm lời giải tối ưu.

Simple Hill Climbing:
Bắt đầu từ một trạng thái ngẫu nhiên và lặp đi lặp lại di chuyển đến một trạng thái lân cận có giá trị hàm mục tiêu (hoặc heuristic) tốt hơn. Dừng lại khi không tìm thấy trạng thái lân cận nào tốt hơn.

Ưu điểm:

Rất hiệu quả về bộ nhớ (O(1)).

Đơn giản, dễ hiểu và triển khai.

Nhược điểm:

Dễ bị mắc kẹt tại tối ưu cục bộ, cao nguyên (plateau) hoặc sườn dốc (ridge).

Không đảm bảo tính đầy đủ hay tối ưu.


Steepest Ascent Hill Climbing:
Tương tự Simple Hill Climbing, nhưng ở mỗi bước, nó xem xét tất cả các trạng thái lân cận và di chuyển đến trạng thái lân cận tốt nhất.

Ưu điểm:

Rất hiệu quả về bộ nhớ (O(1)).

Thường tìm được lời giải nhanh hơn Simple Hill Climbing nếu không bị mắc kẹt.

Nhược điểm:

Vẫn dễ bị mắc kẹt tại tối ưu cục bộ, cao nguyên hoặc sườn dốc.

Không đảm bảo tính đầy đủ hay tối ưu.

Việc đánh giá tất cả các trạng thái lân cận có thể tốn kém hơn Simple Hill Climbing ở mỗi bước.


Stochastic Hill Climbing:
Thay vì chọn trạng thái lân cận tốt nhất, nó chọn ngẫu nhiên một trong những trạng thái lân cận tốt hơn trạng thái hiện tại.

Ưu điểm:

Rất hiệu quả về bộ nhớ (O(1)).

Có thể thoát khỏi một số tối ưu cục bộ nhỏ do yếu tố ngẫu nhiên.

Nhược điểm:

Vẫn có khả năng bị mắc kẹt.

Không đảm bảo tính đầy đủ hay tối ưu.


Simulated Annealing:
Là một dạng mở rộng của Hill Climbing, cho phép di chuyển đến các trạng thái xấu hơn với một xác suất nhất định. Xác suất này giảm dần theo thời gian (giống như quá trình làm nguội kim loại), giúp thuật toán khám phá không gian tìm kiếm rộng hơn và thoát khỏi tối ưu cục bộ.

Ưu điểm:

Có khả năng thoát khỏi tối ưu cục bộ.

Có thể tìm thấy lời giải toàn cục nếu các tham số (lịch trình nhiệt độ) được chọn phù hợp.

Hiệu quả bộ nhớ (O(1)).

Nhược điểm:

Hiệu quả phụ thuộc nhiều vào lịch trình nhiệt độ.

Có thể mất nhiều thời gian để hội tụ, đặc biệt là khi nhiệt độ giảm chậm.

Không đảm bảo tính đầy đủ hay tối ưu trong mọi trường hợp.


Beam Search:
Duy trì một tập hợp cố định k trạng thái tốt nhất (beam) tại mỗi bước. Ở mỗi bước, nó tạo ra tất cả các trạng thái lân cận từ các trạng thái trong beam hiện tại, sau đó chọn ra k trạng thái tốt nhất từ tập hợp các trạng thái lân cận này để tạo thành beam cho bước tiếp theo.

Ưu điểm:

Duy trì sự đa dạng trong tìm kiếm bằng cách giữ lại nhiều trạng thái tốt nhất (beam).

Giảm khả năng bị mắc kẹt tại tối ưu cục bộ so với Hill Climbing đơn thuần.

Có thể tìm thấy lời giải nhanh chóng.

Nhược điểm:

Không đảm bảo tính đầy đủ hay tối ưu.

Hiệu quả phụ thuộc vào chiều rộng beam được chọn.


Genetic Algorithm:
Là một thuật toán tìm kiếm dựa trên quần thể, lấy cảm hứng từ quá trình tiến hóa sinh học. Nó duy trì một quần thể các "cá thể" (lời giải tiềm năng), áp dụng các toán tử như chọn lọc, lai ghép (crossover) và đột biến (mutation) để tạo ra các thế hệ mới với hy vọng tìm được cá thể tốt hơn (lời giải tốt hơn).

Ưu điểm:

Có khả năng tìm kiếm trong không gian rộng và thoát khỏi tối ưu cục bộ.

Phù hợp cho các bài toán tối ưu phức tạp.

Có thể tìm kiếm song song (khám phá nhiều vùng của không gian tìm kiếm cùng lúc).

Nhược điểm:

Không đảm bảo tính đầy đủ hay tối ưu.

Việc thiết kế hàm fitness, chọn lọc, lai ghép và đột biến rất quan trọng và có thể khó khăn.

Có thể mất nhiều thời gian để hội tụ.


### 2.4. Các thuật thuật toán Tìm kiếm dựa trên ràng buộc (Constraint-Based Search)
**Khái niệm bài toán tìm kiếm và lời giải:**
Trong bối cảnh 8-Puzzle, tìm kiếm dựa trên ràng buộc có thể được hiểu là việc tìm kiếm một cấu hình bảng (trạng thái đích) thỏa mãn các ràng buộc về vị trí của các ô số. Các thuật toán này thường được sử dụng cho các bài toán thỏa mãn ràng buộc (Constraint Satisfaction Problems - CSP). Trong triển khai này, các thuật toán này được điều chỉnh để tìm đường đi đến trạng thái đích.

**Các thuật toán Tìm kiếm dựa trên ràng buộc đã triển khai**

Backtracking Search: Một dạng tìm kiếm theo chiều sâu có quay lui để khám phá các khả năng.

Forward Checking: Một kỹ thuật duy trì tính nhất quán trong quá trình tìm kiếm, loại bỏ sớm các giá trị không khả thi.

Constraint Propagation (AC3): Một thuật toán đảm bảo tính nhất quán cung (Arc Consistency) giữa các biến. Trong triển khai này, AC3 được mô phỏng bằng BFS để tìm đường đi, tập trung vào việc khám phá các trạng thái.

Hình ảnh minh họa:

**Hình ảnh minh họa của Backtracking Search:**

![Backtracking](https://github.com/user-attachments/assets/842af70f-ebbf-4730-8109-690de65d4f26)

**Hình ảnh minh họa của Forward Checking:**

![forward_checking](https://github.com/user-attachments/assets/2d4543c1-125c-4050-bf44-0c8893e2d821)

**Hình ảnh minh họa của Constraint Propagation (AC3):**

![AC3](https://github.com/user-attachments/assets/16f03170-9591-41e8-a82d-657589ef1ab9)

Biểu đồ so sánh hiệu suất:

![Screenshot 2025-05-18 125206](https://github.com/user-attachments/assets/88d7104e-7f3a-4358-9126-cfb9d6e4a5b5)

**Ưu điểm, Nhược điểm và Hiệu suất**

Tổng quan về hiệu suất trên trò chơi 8 ô chữ: Khi được điều chỉnh để tìm đường đi trong 8-Puzzle, Backtracking và Forward Checking có thể hoạt động nhưng thường không hiệu quả bằng BFS hoặc A* trong việc tìm lời giải tối ưu. Việc mô phỏng AC3 bằng BFS có nghĩa là hiệu suất của nó sẽ tương đương với BFS.

Backtracking Search:
Là một thuật toán tìm kiếm đệ quy, thử gán giá trị cho các biến lần lượt. Nếu một gán giá trị dẫn đến vi phạm ràng buộc, thuật toán sẽ "quay lui" và thử một giá trị khác.

Ưu điểm:

Đơn giản để triển khai.

Có thể tìm thấy lời giải nếu lời giải nằm ở độ sâu nông.

Nhược điểm:

Có thể khám phá các nhánh không cần thiết.

Dễ bị mắc kẹt trong các "ngõ cụt" sâu.

Không đảm bảo tính tối ưu.


Forward Checking:
Là một cải tiến của Backtracking Search. Khi gán giá trị cho một biến, Forward Checking kiểm tra các ràng buộc liên quan đến biến đó và loại bỏ các giá trị không nhất quán trong miền giá trị của các biến chưa được gán.

Ưu điểm:

Cải thiện đáng kể hiệu quả của Backtracking bằng cách phát hiện sớm sự không nhất quán.

Giúp cắt tỉa không gian tìm kiếm hiệu quả hơn.

Nhược điểm:

Không phát hiện được tất cả các sự không nhất quán sớm nhất (chỉ kiểm tra ràng buộc liên quan đến biến hiện tại và các biến chưa được gán giá trị).

Không đảm bảo tính tối ưu.


Constraint Propagation (AC3 - mô phỏng bằng BFS):
AC3 (Algorithm for Maintaining Arc Consistency) là một thuật toán đảm bảo tính nhất quán cung giữa các biến trong bài toán CSP. Trong triển khai này, AC3 được mô phỏng bằng BFS để tìm đường đi, tập trung vào việc khám phá các trạng thái có thể đạt được.

Ưu điểm:

Đảm bảo tính nhất quán cung, giúp giảm không gian tìm kiếm (trong ngữ cảnh CSP truyền thống).

Khi mô phỏng bằng BFS để tìm đường đi, nó kế thừa các ưu điểm của BFS (đầy đủ, tối ưu).

Nhược điểm:

Việc đảm bảo tính nhất quán có thể tốn kém (trong ngữ cảnh CSP truyền thống).

Khi mô phỏng bằng BFS, nó kế thừa nhược điểm về bộ nhớ của BFS.


### 2.5. Các thuật toán Tìm kiếm phức tạp (Complex Search)
**Khái niệm bài toán tìm kiếm và lời giải:**
Nhóm này bao gồm các thuật toán xử lý các bài toán tìm kiếm trong môi trường không chắc chắn hoặc có quan sát một phần.

**Các thuật toán Tìm kiếm phức tạp đã triển khai**

AND-OR Search: Thường được sử dụng cho các bài toán có yếu tố lựa chọn (OR nodes) và yếu tố bắt buộc phải hoàn thành tất cả (AND nodes), ví dụ như trong lập kế hoạch. Trong triển khai này, nó có thể được điều chỉnh để xử lý các trường hợp có nhiều trạng thái ban đầu có thể xảy ra (niềm tin).

Belief State Search: Tìm kiếm trên không gian các "trạng thái niềm tin", trong đó mỗi trạng thái niềm tin là một phân phối xác suất trên các trạng thái thực tế có thể xảy ra.

Search with Partial Observation: Tìm kiếm khi hệ thống chỉ có thể quan sát một phần trạng thái thực tế của môi trường.

Hình ảnh minh họa:

**Hình ảnh minh họa của AND-OR Search:**

![AND_OR](https://github.com/user-attachments/assets/d0346595-d768-418f-8b5e-9e09e9de44ef)

**Hình ảnh minh họa của Belief State Search:**

![Belief](https://github.com/user-attachments/assets/722b81cd-adb0-41f9-a96c-ea6aa749573d)

**Hình ảnh minh họa của Search with Partial Observation:**

![SearchwithPO](https://github.com/user-attachments/assets/a8bc670f-3348-4d6f-8303-9d46eec47b2f)

Biểu đồ so sánh hiệu suất: 

![Screenshot 2025-05-18 125717](https://github.com/user-attachments/assets/7a2833b3-4e9c-4fab-91c6-6b97a31146eb)

**Ưu điểm, Nhược điểm và Hiệu suất**

Tổng quan về hiệu suất trên trò chơi 8 ô chữ: Các thuật toán trong nhóm này không được thiết kế tối ưu cho 8-Puzzle cổ điển. Việc áp dụng chúng trong dự án này có thể nhằm mục đích minh họa cách chúng có thể được điều chỉnh cho các biến thể của 8-Puzzle hoặc các bài toán phức tạp hơn. Hiệu suất thực tế của chúng trên 8-Puzzle (khi được mô phỏng) sẽ phụ thuộc vào cách mô hình hóa bài toán và số lượng "niềm tin" cần xử lý.

AND-OR Search, Belief State Search, Search with Partial Observation (mô phỏng bằng BFS):
Các thuật toán này giải quyết bài toán bằng cách tìm kiếm trong không gian các trạng thái niềm tin hoặc sử dụng cấu trúc AND-OR để biểu diễn bài toán. Trong triển khai này, chúng được mô phỏng bằng cách áp dụng BFS để tìm lời giải cho từng trạng thái ban đầu có thể xảy ra (niềm tin).

Ưu điểm:

Có khả năng xử lý các bài toán phức tạp hơn 8-Puzzle cổ điển, nơi có sự không chắc chắn hoặc thông tin không đầy đủ.

Cung cấp khung làm việc để suy luận dưới sự không chắc chắn.

Nhược điểm:

Không gian trạng thái (không gian niềm tin) có thể rất lớn, dẫn đến chi phí tính toán cao.

Các thuật toán này thường phức tạp hơn để triển khai và hiểu.

Việc mô phỏng bằng BFS có thể không phản ánh hết hiệu quả thực sự của chúng trên các bài toán phức tạp hơn.


### 2.6. Các thuật toán Học tăng cường (Reinforcement Learning Search)
**Khái niệm bài toán tìm kiếm và lời giải:**
Học tăng cường là một lĩnh vực của AI nơi tác nhân học cách đưa ra quyết định bằng cách thực hiện các hành động trong một môi trường để đạt được phần thưởng tối đa. Trong 8-Puzzle, tác nhân (thuật toán) học cách di chuyển các ô số để đạt được trạng thái đích thông qua thử và sai, nhận phản hồi (phần thưởng) từ môi trường. Lời giải là một chính sách (policy) hoặc một chuỗi hành động được học.

**Các thuật toán Học tăng cường đã triển khai:**

Q-Learning: Một thuật toán học tăng cường không mô hình (model-free) học giá trị Q (giá trị kỳ vọng của việc thực hiện một hành động trong một trạng thái cụ thể).

Hình ảnh minh họa:

![Qlearning](https://github.com/user-attachments/assets/27d8b9ae-3129-49c9-b582-94db8e5e9df3)

Biểu đồ so sánh hiệu suất: 

![image](https://github.com/user-attachments/assets/2e720703-b7b3-4018-a392-d148f79ea96c)

**Ưu điểm, Nhược điểm và Hiệu suất**

Tổng quan về hiệu suất trên trò chơi 8 ô chữ: Q-Learning là một cách tiếp cận khác biệt so với tìm kiếm truyền thống. Nó không trực tiếp tìm một đường đi cụ thể từ trạng thái ban đầu đến đích mà học một chiến lược hành động. Đối với 8-Puzzle, Q-Learning có thể học được cách giải sau một quá trình huấn luyện đủ dài, nhưng thường không hiệu quả bằng A* hoặc IDA* trong việc tìm lời giải tối ưu cho một trạng thái ban đầu cụ thể. Tuy nhiên, nó minh họa khả năng áp dụng học tăng cường cho các bài toán tìm kiếm.

Q-Learning:
Q-Learning học một hàm giá trị Q, Q(s,a), biểu thị giá trị kỳ vọng của việc thực hiện hành động a trong trạng thái s và sau đó tuân theo chính sách tối ưu. Tác nhân cập nhật giá trị Q dựa trên phần thưởng nhận được và giá trị Q tối đa của trạng thái tiếp theo.

Ưu điểm:

Có khả năng học cách giải quyết bài toán mà không cần mô hình môi trường rõ ràng.

Chính sách học được có thể áp dụng cho nhiều trạng thái ban đầu khác nhau (sau khi huấn luyện).

Có thể thích ứng với môi trường thay đổi (nếu quá trình học tiếp tục).

Nhược điểm:

Quá trình học có thể tốn nhiều thời gian (số lượng episode huấn luyện).

Hiệu quả phụ thuộc vào việc lựa chọn các tham số học (learning rate, discount factor, exploration rate).

Không đảm bảo tìm được lời giải tối ưu trong mọi trường hợp, đặc biệt với số lượng episode huấn luyện hạn chế.

Cần khám phá đủ không gian trạng thái-hành động để học hiệu quả.

### 3. Kết luận
Dự án đã thành công trong việc triển khai và tích hợp nhiều thuật toán tìm kiếm khác nhau (không có thông tin, có thông tin, cục bộ, dựa trên ràng buộc, phức tạp, học tăng cường) để giải bài toán 8-Puzzle. Ứng dụng cung cấp một nền tảng trực quan để người dùng:

Hiểu rõ hơn về cách hoạt động của từng thuật toán thông qua mô phỏng từng bước.

So sánh hiệu suất (thời gian thực thi, số node mở rộng) giữa các thuật toán trong cùng một nhóm hoặc khác nhóm.

Thử nghiệm các trạng thái ban đầu khác nhau và xem cách các thuật toán xử lý.

Kết quả đạt được bao gồm việc xây dựng một ứng dụng Python sử dụng thư viện Tkinter cho giao diện người dùng, tích hợp các triển khai thuật toán từ cơ bản đến nâng cao, và cung cấp khả năng trực quan hóa quá trình tìm kiếm cũng như so sánh số liệu hiệu suất.
