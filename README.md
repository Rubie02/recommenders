# Hệ thống gợi ý hỗ trợ cho website mua sắm
## Sử dụng 5 thuật toán chính: kNN, CoClustering, NMF, SVD, SVDpp
- Kiểm thử thuật toán với tập dữ liệu amazon
- Áp dụng các thuật toán vào tập dữ liệu tự sinh Hmart
- Đánh giá và lấy ra thuật toán tốt nhất dùng cho hệ thống gợi ý trên website

## Để tìm ra best parameters cho từng thuật toán. Nhóm đã chạy như sau:
- for training_rate in training_range(0.7, 0.8):
-   for param in param_range(start, end):
-       run algorithm
-       calcualte RMSE
-       save RMSE in array
- find min RMSE -> training rate and param

- Với training_rate là tỉ lệ tập train và 1-training_rate là tỉ lệ tập test
- param là tham số dựa theo từng thuật toán (tìm tham số tốt nhất)